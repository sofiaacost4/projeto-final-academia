from models.dao_sql.dao import DAO
from models.aulaaluno import AulaAluno

class AulaAlunoDAO(DAO):

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO aula_aluno (id_aula, id_aluno)
            VALUES (?, ?)
        """
        cls.execute(sql, (
            obj.get_id_aula(),
            obj.get_id_aluno()
        ))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT id, id_aula, id_aluno FROM aula_aluno"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        cls.fechar()
        return [
            AulaAluno(id, id_aula, id_aluno)
            for (id, id_aula, id_aluno) in rows
        ]

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT id, id_aula, id_aluno FROM aula_aluno WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        cls.fechar()
        return AulaAluno(*row) if row else None

    @classmethod
    def listar_por_aula(cls, id_aula):
        cls.abrir()
        sql = "SELECT id, id_aula, id_aluno FROM aula_aluno WHERE id_aula = ?"
        cursor = cls.execute(sql, (id_aula,))
        rows = cursor.fetchall()
        cls.fechar()
        return [
            AulaAluno(id, id_aula, id_aluno)
            for (id, id_aula, id_aluno) in rows
        ]

    @classmethod
    def excluir(cls, id):
        cls.abrir()
        sql = "DELETE FROM aula_aluno WHERE id = ?"
        cls.execute(sql, (id,))
        cls.fechar()

    @classmethod
    def excluir_aluno_da_aula(cls, id_aula, id_aluno):
        cls.abrir()
        sql = """
            DELETE FROM aula_aluno
            WHERE id_aula = ? AND id_aluno = ?
        """
        cls.execute(sql, (id_aula, id_aluno))
        cls.fechar()
