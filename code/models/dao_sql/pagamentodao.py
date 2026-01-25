from models.dao_sql.dao import DAO
from models.dao_sql.database import Database
from models.pagamento import Pagamento

class PagamentoDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO pagamento (status, valor, id_inscricao)
            VALUES (?, ?, ?)
        """
        cls.execute(sql, (obj.get_status(), obj.get_valor(), obj.get_id_inscricao()))
        cls.fechar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT id, status, valor, id_inscricao FROM pagamento"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [Pagamento(id, status, valor, id_inscricao) for (id, status, valor, id_inscricao) in rows]
        cls.fechar()
        return objs
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT id, status, valor, id_inscricao FROM pagamento WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        rows = cursor.fetchone()
        obj = Pagamento(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE pagamento SET status=?, valor=?, id_instrutor=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_status, obj.get_valor(), obj.get_id_instrutor(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM pagamento WHERE id=?"
        cls.execute(sql, (obj.get_id(),))
        cls.fechar()