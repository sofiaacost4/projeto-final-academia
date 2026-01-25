from datetime import datetime

class Aula:
    def __init__(self, id, id_esporte, dia, id_instrutor, confirmada=False):
        self.__id = id
        self.__id_esporte = id_esporte
        self.__dia = dia
        self.__id_instrutor = id_instrutor
        self.__confirmada = confirmada

    def get_id(self): return self.__id
    def get_id_esporte(self): return self.__id_esporte
    def get_dia(self):
        from datetime import datetime
        if isinstance(self.__dia, str):
            return datetime.strptime(self.__dia, "%Y-%m-%d %H:%M:%S")
        return self.__dia
    def get_id_instrutor(self): return self.__id_instrutor
    def get_confirmada(self): return self.__confirmada

    def set_id(self, id):
        self.__id = id

    def set_id_esporte(self, id_esporte):
        if id_esporte is None:
            raise ValueError("Esporte é obrigatório")
        self.__id_esporte = id_esporte

    def set_id_instrutor(self, id_instrutor):
        if id_instrutor is None:
            raise ValueError("Instrutor é obrigatório")
        self.__id_instrutor = id_instrutor

    def set_dia(self, dia):
        if isinstance(dia, datetime):
            self.__dia = dia
            return
        if isinstance(dia, str):
            try:
                self.__dia = datetime.strptime(dia, "%d/%m/%Y %H:%M")
                return
            except ValueError:
                pass
            try:
                self.__dia = datetime.strptime(dia, "%Y-%m-%d %H:%M:%S")
                return
            except ValueError:
                pass
        raise ValueError("Formato de data/hora inválido para aula.")

    def set_confirmada(self, confirmada):
        self.__confirmada = confirmada


    def to_dic(self):
        return {
            "id": self.__id,
            "id_esporte": self.__id_esporte,
            "dia": self.__dia.strftime("%Y-%m-%d %H:%M:%S"),
            "id_instrutor": self.__id_instrutor,
            "confirmada": self.__confirmada
        }

    @staticmethod
    def from_dic(dic):
        return Aula(
            id=dic["id"],
            id_esporte=dic["id_esporte"],
            dia=datetime.strptime(dic["dia"], "%Y-%m-%d %H:%M:%S"),
            id_instrutor=dic["id_instrutor"],
            confirmada=dic["confirmada"]
        )

    def __str__(self):
        return (
            f'{self.__id} | Esporte: {self.__id_esporte} |'
            f'Data: {self.__dia} | Instrutor: {self.__id_instrutor} | Confirmada: {self.__confirmada}')
