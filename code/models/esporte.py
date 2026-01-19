from datetime import datetime

class Esporte:
    def __init__(self, id, tipo):
        self.set_id(id)
        self.set_tipo(tipo)
    
    def get_id(self): return self.__id
    def get_tipo(self): return self.__tipo

    def set_id(self, id): self.__id = id
    def set_tipo(self, tipo): self.__tipo = tipo

    def to_dic(self):
        dic = {"id": self.__id, "tipo": self.__tipo}
        return dic
    
    @staticmethod
    def from_dic(self):
        return Esporte(dic["id"], dic["tipo"])

    def  __str__(self): 
        return f'{self.__id} - {self.__tipo}'
    
    
