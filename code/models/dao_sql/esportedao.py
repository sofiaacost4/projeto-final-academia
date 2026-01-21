
from models.dao_sql.dao import DAO
from models.esporte import Esporte

class EsporteDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO esporte (tipo)
            VALUES (?)
        """
        cls.execute(sql, (obj.get_tipo(),))
        cls.fechar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT id, tipo FROM esporte"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [Esporte(id, tipo) for (id, tipo) in rows]
        cls.fechar()
        return objs
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT id, tipo FROM esporte WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        rows = cursor.fetchone()
        obj = Esporte(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE esporte SET tipo=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_tipo(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM esporte WHERE id=?"
        cls.execute(sql, (obj.get_id(),))
        cls.fechar()
