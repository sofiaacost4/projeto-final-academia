from datetime import datetime

class Esporte:
    def __init__(self, id, tipo, valor):
        self.set_id(id)
        self.set_tipo(tipo)
        self.set_valor(valor)

    def get_id(self):
        return self.__id

    def get_tipo(self):
        return self.__tipo

    def get_valor(self):
        return self.__valor

    def set_id(self, id):
        self.__id = id

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def set_valor(self, valor):
        if valor < 0:
            raise ValueError("O valor do esporte não pode ser negativo.")
        self.__valor = valor

    def to_dic(self):
        return {
            "id": self.__id,
            "tipo": self.__tipo,
            "valor": self.__valor
        }

    @staticmethod
    def from_dic(dic):
        return Esporte(
            dic["id"],
            dic["tipo"],
            dic["valor"]
        )

    def __str__(self):
        return f"{self.__id} - {self.__tipo} (R$ {self.__valor:.2f})"
