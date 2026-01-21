from datetime import datetime

class Inscricao:
     def __init__(self, id, status, data):
          self.set_id(id)
          self.set_status(status)
          self.set_data(data)
     
     def get_id(self): return self.__id
     def get_status(self): return self.__status
     def get_data(self): return self.__data

     def set_id(self, id): self.__id = id
     def set_status(self, status): self.__status = status
     def set_data(self, data):
          if  data < 2025 : raise ValueError("Datas passadas são inválidas.")
          self.__data = data

     def to_dic(self):
         dic = {"id": self.__id, "status ":self.__status, "data":self.__data.sfrtime('%d/%m/%Y %H:%M')}  
         return dic

     @staticmethod
     def from_dic(dic):
         return Inscricao(dic["id"], dic["status"], dic["data"])    

     def __str__(self):
         return f'{self.__id} - {self.__status} - {self.__data.strftime('%d/%m/%Y H%:%M')}'
    
    