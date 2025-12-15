from dao_sql import DAO
from models.aluno import Aluno

class AlunoDAO(DAO):
    @classmethod
    def abrir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO aluno (nome, email, fone, senha)
            VALUES (?, ?, ?, ?)
        """
        cls.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_senha()))
        cls.fechar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT id, nome, email, fone, senha FROM aluno"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [Aluno(id, nome, email, fone, senha) for (id, nome, email, fone, senha) in rows]
        cls.fechar()
        return objs
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT id, nome, email, fone, senha FROM aluno WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        rows = cursor.fetchone()
        obj = Aluno(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE aluno SET nome=?, email=?, fone=?, senha=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_senha(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM aluno WHERE id=?"
        cls.execute(sql, (obj.get_id(),))
        cls.fechar()