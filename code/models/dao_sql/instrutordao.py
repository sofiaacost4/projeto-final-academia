from models.dao_sql.dao import DAO
from models.instrutor import Instrutor

class InstrutorDAO(DAO):

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO instrutor (nome, email, fone, senha)
            VALUES (?, ?, ?, ?)
        """
        cls.execute(sql, (
            obj.get_nome(),
            obj.get_email(),
            obj.get_fone(),
            obj.get_senha()
        ))
        cls.fechar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT id, nome, email, fone, senha FROM instrutor"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [
            Instrutor(id, nome, email, fone, senha)
            for (id, nome, email, fone, senha) in rows
        ]
        cls.fechar()
        return objs
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT id, nome, email, fone, senha FROM instrutor WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Instrutor(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE instrutor
            SET nome=?, email=?, fone=?, senha=?
            WHERE id=?
        """
        cls.execute(sql, (
            obj.get_nome(),
            obj.get_email(),
            obj.get_fone(),
            obj.get_senha(),
            obj.get_id()
        ))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM instrutor WHERE id=?"
        cls.execute(sql, (obj.get_id(),))
        cls.fechar()
