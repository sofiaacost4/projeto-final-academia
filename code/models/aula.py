from datetime import datetime

class Aula:
    def __init__(self, id, id_esporte, dt_inicio, dt_fim, id_instrutor, dia):
        self.set_id(id)
        self.set_id_esporte(id_esporte)
        self.set_dt_inicio(dt_inicio)
        self.set_dt_fim(dt_fim)
        self.set_id_instrutor(id_instrutor)
        self.set_dia(dia)
    
    def get_id(self): return self.__id
    def get_id_esporte(self): return self.__id_esporte
    def get_dt_inicio(self): return self.__dt_inicio
    def get_dt_fim(self): return self.__dt_fim
    def get_id_instrutor(self): return self.__id_instrutor
    def get_dia(self): return self.__dia

    def set_id(self, id): self.__id = id
    def set_tipo(self, id_esporte): self.__id_esporte = id_esporte
    def set_tipo(self, dt_inicio): self.__dt_inicio = dt_inicio
    def set_tipo(self, dt_fim): self.__dt_fim = dt_fim
    def set_tipo(self, id_instrutor): self.__id_instrutor = id_instrutor
    def set_tipo(self, dia): self.__dia = dia

    def to_dic(self):
        dic = {"id": self.__id, "id_esporte": self.__id_esporte, "dt_inicio": self.__dt_inicio, "dt_fim": self.__dt_fim, "id_instrutor": self.__id_instrutor, "dia": self.__dia}
        return dic
    
    @staticmethod
    def from_dic(self):
        return Esporte(dic["id"], dic["id_esporte"], dic["dt_inicio"], dic["dt_fim"], dic["id_instrutor"], dic["dia"])

    def  __str__(self): 
        return f'{self.__id} - {self.__id_esporte} - {self.__dt_inicio} - {self.__dt_fim} - {self.__id_instrutor} - {self.__dia}'
    
    
