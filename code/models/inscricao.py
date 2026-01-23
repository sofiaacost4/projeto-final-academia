class Inscricao:
    def __init__(self, id=None, id_aluno=None, id_esporte=None, status=None):
        self.set_id(id)
        self.set_id_aluno(id_aluno)
        self.set_id_esporte(id_esporte)
        self.set_status(status)

    # GETTERS
    def get_id(self): return self.__id
    def get_id_aluno(self): return self.__id_aluno
    def get_id_esporte(self): return self.__id_esporte
    def get_status(self): return self.__status

    # SETTERS
    def set_id(self, id):
        self.__id = id

    def set_id_aluno(self, id_aluno):
        if id_aluno is None:
            raise ValueError("Aluno é obrigatório.")
        self.__id_aluno = id_aluno

    def set_id_esporte(self, id_esporte):
        if id_esporte is None:
            raise ValueError("Esporte é obrigatório.")
        self.__id_esporte = id_esporte

    def set_status(self, status):
        self.__status = status

    # UTIL
    def to_dic(self):
        return {
            "id": self.__id,
            "id_aluno": self.__id_aluno,
            "id_esporte": self.__id_esporte,
            "status": self.__status
        }

    @staticmethod
    def from_dic(dic):
        return Inscricao(
            dic["id"],
            dic["id_aluno"],
            dic["id_esporte"],
            dic["status"]
        )

    def __str__(self):
        return f"{self.__id} - Aluno {self.__id_aluno} - Esporte {self.__id_esporte} - {self.__status}"
