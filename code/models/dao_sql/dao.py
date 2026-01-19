import sqlite3
from datetime import datetime

class DAO:
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
        return cursor
    @classmethod

    def criar_tabelas(cls):
        cls.abrir()

        sql_aluno = """
        CREATE TABLE IF NOT EXISTS aluno (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            fone TEXT,
            senha TEXT NOT NULL
        )
        """
        sql_instrutor = """
        CREATE TABLE IF NOT EXISTS instrutor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            fone TEXT,
            senha TEXT NOT NULL
        )
        """
        cls.execute(sql_aluno)
        cls.execute(sql_instrutor)
        cls.fechar()


