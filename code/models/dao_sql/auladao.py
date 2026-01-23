from models.dao_sql.dao import DAO
from models.aula import Aula

class AulaDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO aula (id_aluno, id_esporte, dia, confirmado, id_instrutor)
            VALUES (?, ?, ?, ?, ?)
        """
        cls.execute(sql, (obj.get_id_aluno(), obj.get_id_esporte(), obj.get_dia(), obj.get_confirmado(), obj.get_id_instrutor()))
        cls.fechar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT id, id_aluno, id_esporte, dia, confirmado, id_instrutor FROM aula"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [
            Aula(id, id_aluno, id_esporte, dia, confirmado, id_instrutor)
            for (id, id_aluno, id_esporte, dia, confirmado, id_instrutor) in rows
        ]
        cls.fechar()
        return objs
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT id, id_aluno, id_esporte, dia, confirmado, id_instrutor FROM aula WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Aula(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE aula SET id_aluno=?, id_esporte=?, dia=?, confirmado=?, id_instrutor=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_id_aluno(), obj.get_id_esporte(), obj.get_dia(), obj.get_confirmado(), obj.get_id_instrutor(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM aula WHERE id=?"
        cls.execute(sql, (obj.get_id(),))
        cls.fechar()