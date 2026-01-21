from datetime import datetime

class Aula:
    def __init__(self, id, id_aluno, id_esporte, dia, confirmado, id_instrutor):
        self.set_id(id)
        self.set_id_aluno(id_aluno)
        self.set_id_esporte(id_esporte)
        self.set_dia(dia)
        self.set_confirmado(False)
        self.set_id_instrutor(id_instrutor)
        
    def get_id(self): return self.__id
    def get_id_aluno(self): return self.__id_aluno
    def get_id_esporte(self): return self.__id_esporte
    def get_dia(self): return self.__dia
    def get_confirmado(self): return self.__confirmado
    def get_id_instrutor(self): return self.__id_instrutor

    def set_id(self, id): self.__id = id
    def set_id_aluno(self, id_aluno): self.__id_aluno = id_aluno
    def set_id_esporte(self, id_esporte): self.__id_esporte = id_esporte
    def set_confirmado(self, confirmado): self.__confirmado = confirmado
    def set_id_instrutor(self, id_instrutor): self.__id_instrutor = id_instrutor
    def set_dia(self, dia): 
        ano_atual = datetime.now().year
        if dia.year < ano_atual:
            raise ValueError(f'O ano deve ser no mínimo {ano_atual}.')
        self.__dia = dia

    def to_dic(self):
        dic = {"id": self.__id, "id_aluno": self.__id_aluno, "id_esporte": self.__id_esporte, "dia": self.__dia, "confirmado": self.__confirmado, "id_instrutor": self.__id_instrutor}
        return dic
    
    @staticmethod
    def from_dic(self):
        return Aula(dic["id"], dic["id_aluno"], dic["id_esporte"], dic["dia"], dic["confirmado"], dic["id_instrutor"])

    def  __str__(self): 
        return f'{self.__id} - {self.__id_aluno} - {self.__id_esporte} - {self.__dia} - {self.__confirmado} - {self.__id_instrutor}'
    
    
