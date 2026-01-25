import sqlite3
import os

class Database:
    conn = None

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    nome_bd = os.path.join(BASE_DIR, "academia.db")

    @classmethod
    def abrir(cls):
        cls.conn = sqlite3.connect(cls.nome_bd)
        cls.conn.execute("PRAGMA foreign_keys = ON")

    @classmethod
    def fechar(cls):
        cls.conn.close()

    @classmethod
    def execute(cls, sql, params=None):
        cursor = cls.conn.cursor()
        cursor.execute(sql, params or [])
        cls.conn.commit()
        return cursor   # importante

    @classmethod
    def criar_tabelas(cls):

        # ---------------- ALUNO ----------------
        cls.execute("""
            CREATE TABLE IF NOT EXISTS aluno (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                fone TEXT,
                senha TEXT NOT NULL
            );
        """)

        # ---------------- INSTRUTOR ----------------
        cls.execute("""
            CREATE TABLE IF NOT EXISTS instrutor (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                especialidade INTEGER NOT NULL,
                fone TEXT,
                senha TEXT NOT NULL,

                FOREIGN KEY (especialidade) REFERENCES esporte(id)
            );
        """)

        # ---------------- ESPORTE ----------------
        cls.execute("""
            CREATE TABLE IF NOT EXISTS esporte (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL,
                valor REAL NOT NULL
            );
        """)

        # ---------------- AULA ----------------
        cls.execute("""
            CREATE TABLE IF NOT EXISTS aula (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_esporte INTEGER NOT NULL,
                dia TEXT NOT NULL,
                confirmado INTEGER,
                id_instrutor INTEGER NOT NULL,

                FOREIGN KEY (id_esporte) REFERENCES esporte(id),
                FOREIGN KEY (id_instrutor) REFERENCES instrutor(id)
            );
        """)
        # -------------- AULA_ALUNO ----------------
        cls.execute("""
            CREATE TABLE IF NOT EXISTS aula_aluno (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_aula INTEGER NOT NULL,
                id_aluno INTEGER NOT NULL,

                FOREIGN KEY (id_aula) REFERENCES aula(id) ON DELETE CASCADE,
                FOREIGN KEY (id_aluno) REFERENCES aluno(id) ON DELETE CASCADE,
                UNIQUE (id_aula, id_aluno)
            );
        """)

        # ---------------- INSCRIÇÃO ----------------
        cls.execute("""
            CREATE TABLE IF NOT EXISTS inscricao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_aluno INTEGER NOT NULL,
                id_esporte INTEGER NOT NULL,
                status TEXT NOT NULL,

                FOREIGN KEY (id_aluno) REFERENCES aluno(id),
                FOREIGN KEY (id_esporte) REFERENCES esporte(id)
            );
        """)

        # ---------------- PAGAMENTO ----------------
        cls.execute("""
            CREATE TABLE IF NOT EXISTS pagamento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                status TEXT NOT NULL,
                valor REAL NOT NULL,
                id_inscricao INTEGER NOT NULL,

                FOREIGN KEY (id_inscricao) REFERENCES inscricao(id)
            );
        """)

if __name__ == "__main__":
    Database.abrir()
    Database.criar_tabelas()
    Database.fechar()