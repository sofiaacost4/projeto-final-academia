import sqlite3

class Database:
    conn = None
    nome_bd ="academia.db"

    @classmethod
    def abrir(cls):
        cls.conn = sqlite3.connect(cls.nome_bd)
        cls.conn.execute("PRAGMA foreign_keys = ON")

    @classmethod
    def fechar(cls):
        cls.conn.close()

    @classmethod
    def execute(cls, sql, params = None):
        cursor = cls.conn.cursor()
        cursor.execute(sql, params or [])
        cls.conn.commit()
    
    @classmethod
    def criar_tabelas(cls):
        # tabela Aluno
        cls.execute("""
            CREATE TABLE IF NOT EXISTS aluno (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                fone TEXT,
                senha TEXT NOT NULL
            );
        """)

        # tabela Instrutor
        cls.execute("""
            CREATE TABLE IF NOT EXISTS instrutor (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                especialidade TEXT NOT NULL,
                fone TEXT,
                senha TEXT NOT NULL
            );
        """)

        # tabela Esporte
        cls.execute("""
            CREATE TABLE IF NOT EXISTS esporte (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL,
                dt_inicio TEXT NOT NULL, 
                dt_fim TEXT,
                id_instrutor INTEGER,

                FOREIGN KEY (id_instrutor) REFERENCES instrutor(id) ON DELETE CASCADE
            );
        """)

        # tabela Inscricao
        cls.execute("""
            CREATE TABLE IF NOT EXISTS inscricao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                status TEXT NOT NULL,
                data TEXT NOT NULL
            );
        """)

        # tabela Pagamento
        cls.execute("""
            CREATE TABLE IF NOT EXISTS pagamento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                status TEXT NOT NULL,
                valor REAL NOT NULL,
                id_inscricao INTEGER,

                FOREIGN KEY (id_inscricao) REFERENCES inscricao(id) ON DELETE CASCADE
            );
        """)

if __name__ == "__main__":
    Database.abrir()
    Database.criar_tabelas()
    Database.fechar()

        
        
