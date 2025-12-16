from models.dao_sql.dao import DAO
from models.aula import Aula

class AulaDAO(DAO):
    @classmethod
    def abrir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO aula (tipo, dt_inicio, dt_fim, id_instrutor)
            VALUES (?, ?, ?, ?)
        """
        cls.execute(sql, (obj.get_tipo(), obj.get_dt_incicio(), obj.get_dt_fim(), obj.get_id_instrutor()))
        cls.fechar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT id, tipo, dt_inicio, dt_fim, id_instrutor FROM aula"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [Aula(id, tipo, dt_inicio, dt_fim, id_instrutor) for (id, tipo, dt_inicio, dt_fim, id_instrutor) in rows]
        cls.fechar()
        return objs
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT id, tipo, dt_inicio, dt_fim, id_instrutor FROM aula WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        rows = cursor.fetchone()
        obj = Aula(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE aula SET tipo=?, dt_inicio=?, dt_fim=?, id_instrutor=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_tipo(), obj.get_dt_incicio(), obj.get_dt_fim(), obj.get_id_instrutor(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM aula WHERE id=?"
        cls.execute(sql, (obj.get_id(),))
        cls.fechar()