from datetime import datetime

class Aula:
    def __init__(self, id, id_esporte, id_instrutor, dia, confirmada=False):
        self.set_id(id)
        self.set_id_esporte(id_esporte)
        self.set_id_instrutor(id_instrutor)
        self.set_dia(dia)
        self.set_confirmada(confirmada)

    def get_id(self): return self.__id
    def get_id_esporte(self): return self.__id_esporte
    def get_id_instrutor(self): return self.__id_instrutor
    def get_dia(self): return self.__dia
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

    def set_confirmada(self, confirmada):
        self.__confirmada = confirmada

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

    def to_dic(self):
        return {
            "id": self.__id,
            "id_esporte": self.__id_esporte,
            "id_instrutor": self.__id_instrutor,
            "dia": self.__dia.strftime("%Y-%m-%d %H:%M:%S"),
            "confirmada": self.__confirmada}

    @staticmethod
    def from_dic(dic):
        return Aula(
            dic["id"],
            dic["id_esporte"],
            dic["id_instrutor"],
            dic["dia"],
            dic["confirmada"])
    def __str__(self):
        return (
            f'{self.__id} | Esporte: {self.__id_esporte} | '
            f'Instrutor: {self.__id_instrutor} | '
            f'Data: {self.__dia} | Confirmada: {self.__confirmada}')
