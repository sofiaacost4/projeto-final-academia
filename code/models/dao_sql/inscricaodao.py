from models.dao_sql.dao import DAO
from models.inscricao import Inscricao

class InscricaoDAO(DAO):

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO inscricao (id_aluno, id_esporte, status)
            VALUES (?, ?, ?)
        """
        cls.execute(sql, (
            obj.get_id_aluno(),
            obj.get_id_esporte(),
            obj.get_status()
        ))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT id, id_aluno, id_esporte, status FROM inscricao"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [
            Inscricao(id, id_aluno, id_esporte, status)
            for (id, id_aluno, id_esporte, status) in rows
        ]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT id, id_aluno, id_esporte, status FROM inscricao WHERE id=?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        cls.fechar()
        return Inscricao(*row) if row else None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = "UPDATE inscricao SET status=? WHERE id=?"
        cls.execute(sql, (obj.get_status(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, id_inscricao):
        cls.abrir()
        sql = "DELETE FROM inscricao WHERE id = ?"
        cls.execute(sql, (int(id_inscricao),))
        cls.fechar()
