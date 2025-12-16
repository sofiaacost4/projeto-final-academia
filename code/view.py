from models.aluno import Aluno
from models.instrutor import Instrutor
from models.aula import Aula
from models.dao_sql.alunodao import AlunoDAO
from models.dao_sql.instrutordao import InstrutorDAO
from models.dao_sql.auladao import AulaDAO

class View:
    def criar_gestor():
        for obj in View.aluno_listar():
            if obj.get_email() == "gestor": return
        View.aluno_inserir("gestor", "gestor", "(84) 947479576", "123")

    def aluno_inserir(nome, email, fone, senha):
        try:
            for a in View.aluno_listar():
                if a.get_email() == email:
                    raise ValueError("Este email não está disponível.")
            for i in View.instrutor_listar():
                if i.get_email() == eamil:
                    raise ValueError("Este email não está disponível.")
            aluno = Aluno(0, nome, email, fone, senha)
            AlunoDAO.inserir(aluno)
        except ValueError as erro:
            raise erro
    def aluno_listar():
        r = AlunoDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r
    def aluno_excluir(id):
        try:
            for h in View.aula_listar():
                if h.get_id_aluno() == id:
                    raise ValueError("Esse aluno não pode ser excluído pois está inscrito em uma aula.")
            AlunoDAO.excluir(id)
        except ValueError as erro:
            raise erro
    def aluno_atualizar(id, nome, email, fone, senha):
        try:
            for a in View.aluno_listar():
                if a.get_id() != id:
                    if a.get_email() == email:
                        raise ValueError("Este email não está disponível.")
            for i in View.instrutor_listar():
                if i.get_email() == email:
                    raise ValueError("Este email não está disponível.")
            aluno = Aluno(id, nome, email, fone, senha)
            AlunoDAO.atualizar(aluno)
        except ValueError as erro:
            raise erro
    def aluno_listar_id(id):
        aluno = AlunoDAO.listar_id(id)
        return aluno
        
    def instrutor_listar():
        r = InstrutorDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r
    
    def aula_listar():
        r = AulaDAO.listar()
        r.sort(key = lambda obj : obj.get_data())
        return r