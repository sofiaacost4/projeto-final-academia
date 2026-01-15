from datetime import datetime

class Esporte:
    def __init__(self, id, tipo, dt_inicio, dt_fim, id_instrutor, dia):
        self.set_id(id)
        self.set_tipo(tipo)
        self.set_dt_inicio(dt_inicio)
        self.set_dt_fim(dt_fim)
        self.set_id_instrutor(id_instrutor)
        self.set_dia(dia)
    
    
    def get_id(self): return self.__id
    def get_tipo(self): return self.__tipo
    def get_dt_inicio(self): return self.__dt_inicio
    def get_dt_fim(self): return self.__dt_fim
    def get_id_instrutor(self): return self.__id_instrutor
    def get_dia(self): return self.__dia

    def set_id(self, id): self.__id = id
    def set_tipo(self, tipo): self.__tipo = tipo
    def set_dt_inicio(self, dt_inicio): self.__dt_inicio = dt_inicio
    def set_dt_fim(self, dt_fim): self.__dt_fim = dt_fim
    def set_id_instrutor(self, id_instrutor): self.__id_instrutor = id_instrutor
    def set_dia(self, dia): self.__dia = dia

    def to_dic(self):
        dic = {"id": self.__id, "tipo": self.__tipo, "inicio": self.__dt_inicio, "fim": self.__dt_fim, "id_instrutor": self.__id_instrutor, "dia": self.__dia}
        return dic
    
    @staticmethod
    def from_dic(self):
        return Esporte(dic["id"], dic["tipo"], dic["inicio"], dic["fim"], dic["instrutor"], dic["dia"])

    def  __str__(self): 
        return f'{self.__id} - {self.__tipo} - {self.__dt_inicio.strftime('%d/%m/%Y %H:%M')} - {self.__dt_fim.strftime('%d/%m/%Y %H:%M')} - {self.__id_instrutor} - {self.__dia.strftime('%d/%m/%Y %H:%M')}'
    
    
