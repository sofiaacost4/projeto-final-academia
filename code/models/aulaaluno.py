class AulaAluno:
    def __init__(self, id, id_aula, id_aluno):
        self.set_id(id)
        self.set_id_aula(id_aula)
        self.set_id_aluno(id_aluno)

    def get_id(self): return self.__id
    def get_id_aula(self): return self.__id_aula
    def get_id_aluno(self): return self.__id_aluno

    def set_id(self, id):
        self.__id = id

    def set_id_aula(self, id_aula):
        if id_aula is None:
            raise ValueError("Aula obrigatória")
        self.__id_aula = id_aula

    def set_id_aluno(self, id_aluno):
        if id_aluno is None:
            raise ValueError("Aluno obrigatório")
        self.__id_aluno = id_aluno

    def to_dic(self):
        return {
            "id": self.__id,
            "id_aula": self.__id_aula,
            "id_aluno": self.__id_aluno
        }

    @staticmethod
    def from_dic(dic):
        return AulaAluno(
            dic["id"],
            dic["id_aula"],
            dic["id_aluno"]
        )
