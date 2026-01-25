from models.dao_sql.dao import DAO
from models.aula import Aula

class AulaDAO(DAO):

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO aula (id_esporte, id_instrutor, dia, confirmado)
            VALUES (?, ?, ?, ?)
        """
        cls.execute(sql, (
            obj.get_id_esporte(),
            obj.get_id_instrutor(),
            obj.get_dia().strftime("%Y-%m-%d %H:%M:%S"),
            int(obj.get_confirmada())
        ))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = """
            SELECT id, id_esporte, id_instrutor, dia, confirmado
            FROM aula
        """
        cursor = cls.execute(sql)
        rows = cursor.fetchall()

        objs = [
            Aula(
                id=id,
                id_esporte=id_esporte,
                id_instrutor=id_instrutor,
                dia=dia,
                confirmada=bool(confirmado)
            )
            for (id, id_esporte, id_instrutor, dia, confirmado) in rows
        ]

        cls.fechar()
        return objs


    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = """
            SELECT id, id_esporte, id_instrutor, dia, confirmado
            FROM aula WHERE id=?
        """
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()

        obj = (
            Aula(
                id=row[0],
                id_esporte=row[1],
                id_instrutor=row[2],
                dia=row[3],
                confirmada=bool(row[4])
            ) if row else None
        )

        cls.fechar()
        return obj
    
    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE aula
            SET id_esporte=?, id_instrutor=?, dia=?, confirmado=?
            WHERE id=?
        """
        cls.execute(sql, (
            obj.get_id_esporte(),
            obj.get_id_instrutor(),
            obj.get_dia().strftime("%Y-%m-%d %H:%M:%S"),
            int(obj.get_confirmada()),
            obj.get_id()
        ))
        cls.fechar()

    @classmethod
    def excluir(cls, id):
        cls.abrir()
        sql = "DELETE FROM aula WHERE id=?"
        cls.execute(sql, (id,))
        cls.fechar()
