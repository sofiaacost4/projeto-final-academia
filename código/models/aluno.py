class Aluno:
    def __init__(self, id, nome, email, fone, senha):
         self.set_id(id)
         self.set_nome(nome)
         self.set_email(email)
         self.set_fone(fone) 
         self.set_senha(senha)
    
    def __str__(self):
         return f'{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__senha}'
    
    # GETS
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone

    # SETS
    def set_id(self, id): self.__id = id
    def set_nome(self, nome): 
         if nome == "": raise ValueError("O nome é obrigatório")
         self.__nome = nome
    def set_email(self, email):
         if email == "": raise ValueError("O email é obrigatório")
         self.__email = email
    def set_fone(self, fone): self.__fone = fone
    def set_senha(self, senha): 
         if senha == "": raise ValueError("A senha é obrigatória")
         self.__senha = senha

    # ARMAZENANDO DADOS COM JSON
    def to_json(self):
         dic = {"id": self.__id, "nome":self.__nome, "email":self.__email, "senha": self.__senha}  
         return dic

    @staticmethod
    def from_json(dic):
         return Aluno(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["senha"])    
    
    import json
    from models.dao import DAO

    class AlunoDAO(DAO):
         @classmethod
         def abrir(cls):
              cls._objetos = []
              try:
                   with open("alunos.json", mode="r") as arquivo:
                        list_dic = json.load(arquivo)
                        for dic in list_dic:
                             obj = Aluno.from_json(dic)
                             cls.objetos.append(obj)
              except FileNotFoundError:
                   pass