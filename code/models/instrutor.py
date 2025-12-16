class Instrutor:
     def __init__(self, id, nome, email, especialidade, fone, senha):
          self.set_id(id)
          self.set_nome(nome)
          self.set_email(email)
          self.set_especialidade(especialidade)
          self.set_fone(fone) 
          self.set_senha(senha)
     
     def get_id(self): return self.__id
     def get_nome(self): return self.__nome
     def get_email(self): return self.__email
     def get_especialidade(self): return self.__especialidade
     def get_fone(self): return self.__fone
     def get_senha(self): return self.__senha

     def set_id(self, id): self.__id = id
     def set_nome(self, nome): 
          if nome == "": raise ValueError("O nome é obrigatório")
          self.__nome = nome
     def set_email(self, email):
          if email == "": raise ValueError("O email é obrigatório")
          self.__email = email
     def set_especialidade(self, especialidade):
          if especialidade == "": raise ValueError("A especialidade é obrigatória")
          self.__especialidade == especialidade
     def set_fone(self, fone): self.__fone = fone
     def set_senha(self, senha): 
          if senha == "": raise ValueError("A senha é obrigatória")
          self.__senha = senha

     def to_dic(self):
          dic = {"id": self.__id, "nome":self.__nome, "email":self.__email, "especialidade": self.__especialidade, "senha": self.__senha}  
          return dic

     @staticmethod
     def from_dic(dic):
          return Aluno(dic["id"], dic["nome"], dic["email"], dic["especialidade"], dic["fone"], dic["senha"])    
     
     def __str__(self):
         return f'{self.__id} - {self.__nome} - {self.__email} - {self.__especialidade} - {self.__fone} - {self.__senha}'
    
    