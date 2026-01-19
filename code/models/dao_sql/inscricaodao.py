from models.dao_sql.dao import DAO
from models.dao_sql.database import Database
from models.inscricao import Inscricao

class InscricaoDAO(DAO):
    @classmethod
    def abrir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO inscricao (status, data)
            VALUES (?, ?, ?, ?)
        """
        cls.execute(sql, (obj.get_status(), obj.get_data()))
        cls.fechar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT id, status, data FROM inscricao"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [Inscricao(id, status, data) for (id, status, data) in rows]
        cls.fechar()
        return objs
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT id, status, data FROM inscricao WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        rows = cursor.fetchone()
        obj = Inscricao(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE inscricao SET status=?, data=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_status, obj.get_data(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM inscricao WHERE id=?"
        cls.execute(sql, (obj.get_id(),))
        cls.fechar()