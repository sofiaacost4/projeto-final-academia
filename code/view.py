from models.aluno import Aluno, AlunoDAO
class View:
    def aluno_listar():
        r = AlunoDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r
    def aluno_listar_objetos():
        return AlunoDAO.listar_id()
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
    def aluno_atualizar(id, nome, email, fone, senha):
        try:
            for a in View.aluno_listar():
                if a.get_id() != id:
                    if a.get_email() == email:
                        raise ValueError("Este email não está disponível.")
            for i in View.instrutor_listar():
                if i.get_email() == email:
                    raise ValueError("Este email não está disponível.")
                    
