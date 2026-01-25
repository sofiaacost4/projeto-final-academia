class Pagamento:
    def __init__(self, id, status, valor, id_inscricao):
        self.set_id(id)
        self.set_status(status)
        self.set_valor(valor)
        self.set_id_inscricao(id_inscricao)

    def get_id(self): return self.__id
    def get_status(self): return self.__status
    def get_valor(self): return self.__valor
    def get_id_inscricao(self): return self.__id_inscricao

    def set_id(self, id): self.__id = id 
    def set_status(self, status): self.__status = status
    def set_valor(self, valor): self.__valor = valor
    def set_id_inscricao(self, id_inscricao): self.__id_inscricao = id_inscricao

    def to_dic(self):
        dic = {"id": self.__id, "status": self.__status, "valor": self.__valor, "id_inscricao": self.__id_inscricao}
        return dic
    
    @staticmethod
    def from_dic(dic):
       return Pagamento(dic["id"], dic["status"], dic["valor"], dic["id_inscricao"])
    
    def __str__(self):
        return f'{self.__id} - {self.__status} - {self.__valor} - {self.__id_inscricao}'
    
    
    