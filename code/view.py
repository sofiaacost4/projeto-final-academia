from models.aluno import Aluno
from models.aula import Aula
from models.instrutor import Instrutor
from models.esporte import Esporte
from models.dao_sql.alunodao import AlunoDAO
from models.dao_sql.auladao import AulaDAO
from models.dao_sql.instrutordao import InstrutorDAO
from models.dao_sql.esportedao import EsporteDAO
from models.dao_sql.inscricaodao import InscricaoDAO

class View:
    def criar_gestor():
        for obj in View.aluno_listar():
            if obj.get_email() == "gestor":
                return
        View.aluno_inserir("gestor", "gestor", "(84) 947479576", "123")

    # ALUNO
    def aluno_listar():
        r = AlunoDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r
    def aluno_inserir(nome, email, fone, senha):
        try:
            for a in View.aluno_listar():
                if a.get_email() == email:
                    raise ValueError("Este email não está disponível.")
            for i in View.instrutor_listar():
                if i.get_email() == email:
                    raise ValueError("Este email não está disponível.")
            aluno = Aluno(0, nome, email, fone, senha)
            AlunoDAO.inserir(aluno)
        except ValueError as erro:
            raise erro
    def aluno_atualizar(id, nome, email, fone, senha):
        try:
            for a in View.aluno_listar():
                if email == "gestor":
                    raise ValueError("Este email é de uso exclusivo do gestor.")
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
    def aluno_excluir(id):
        aluno = View.aluno_listar_id(id)
        if aluno.get_email() == "gestor":
            raise ValueError("Gestor não pode ser excluído.")
        AlunoDAO.excluir(id)
    def aluno_listar_id(id):
        aluno = AlunoDAO.listar_id(id)
        return aluno
    def aluno_autenticar(email, senha):
        for c in View.aluno_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id" : c.get_id(), "nome" : c.get_nome()}
        return None
        
    # INSTRUTOR
    def instrutor_listar():
        instrutores = InstrutorDAO.listar()
        esportes = EsporteDAO.listar()
        mapa_esportes = {
            e.get_id(): e.get_tipo()
            for e in esportes}
        resultado = []
        for i in instrutores:
            nome_esporte = mapa_esportes.get(
                i.get_especialidade(),
                "Não informado"
            )
            resultado.append((
                i.get_nome(),
                i.get_email(),
                nome_esporte,
                i.get_fone()
            ))

        return resultado
    def instrutor_listar_id():
        instrutor = InstrutorDAO.listar_id(id)
        return instrutor
    def instrutor_inserir(nome, email, especialidade, fone, senha):
        try:
            for a in View.aluno_listar():
                if a.get_email() == email:
                    raise ValueError("Este email não está disponível.")
            for i in View.instrutor_listar():
                if i.get_email() == email:
                    raise ValueError("Este email não está disponível.")
            instrutor = Instrutor(0, nome, email, especialidade, fone, senha)
            InstrutorDAO.inserir(instrutor)
        except ValueError as erro:
            raise erro
    def instrutor_atualizar(id, nome, email, especialidade, fone, senha):
        try:
            for a in View.aluno_listar():
                if email == "gestor":
                    raise ValueError("Este email é de uso exclusivo do gestor.")
                if a.get_id() != id:
                    if a.get_email() == email:
                        raise ValueError("Este email não está disponível.")
            for i in View.instrutor_listar():
                if i.get_email() == email:
                    raise ValueError("Este email não está disponível.")
            instrutor = Instrutor(id, nome, email, especialidade, fone, senha)
            InstrutorDAO.atualizar(instrutor)
        except ValueError as erro:
            raise erro
    def instrutor_excluir():
        instrutor = View.instrutor_listar_id(id)
        InstrutorDAO.excluir(instrutor) # erro = não pode excluir um instrutor com AULA agendada
    def instrutor_autenticar(email, senha):
        for p in View.instrutor_listar():
            if p.get_email() == email and p.get_senha() == senha:
                return {"id" : p.get_id(), "nome" : p.get_nome()}
        return None

    # ESPORTE
    def esporte_listar():
        r = EsporteDAO.listar()
        return r
    
    def esporte_listar_id(id):
        esporte = EsporteDAO.listar_id(id)
        return esporte

    def esporte_inserir(tipo):
        for a in View.esporte_listar():
            if a.get_tipo() == tipo:
                raise ValueError("Este esporte não está disponível.")
        esporte = Esporte(0, tipo)
        EsporteDAO.inserir(esporte)

    def esporte_atualizar(id, tipo):
        for e in View.esporte_listar():
            if e.get_id() != id:
                if e.get_tipo() == tipo:
                    raise ValueError("Este esporte não está disponível.")
        esporte = Esporte(id, tipo)
        EsporteDAO.atualizar(esporte)

    def esporte_excluir(id): 
        EsporteDAO.excluir(id) # aqui fazer um erro futuramente para não permitir excluir os esportes que tiverem pelo menos um aluno cadastrado.


    # AULA
    def aula_listar():
        return AulaDAO.listar()
    def aula_listar_id(id):
        return AulaDAO.listar_id()
    def aula_inserir():
        for a in View.aula_listar():
            if a.get_dia() == dia and a.get_id_instrutor() == id_instrutor:
                raise ValueError("Esse data já está cadastrada na agenda de um profissional.")
        c = Aula(0, data)
        c.set_id_aluno(id_aluno)
        c.set_confirmado(confirmado)
        c.set_id_esporte(id_esporte)
        c.set_id_instrutor(id_instrutor)
        AulaDAO.inserir(c)
    def aula_atualizar():
        for a in View.aula_listar():
            if a.get_id() != id and a.get_dia() == dia and a.get_id_instrutor() == id_instrutor: 
                raise ValueError("Esse data já está cadastrada na agenda de um instrutor.")
        c = Aula(id, dia)
        c.set_id_aluno(id_aluno)
        c.set_confirmado(confirmado)
        c.set_id_esporte(id_esporte)
        c.set_id_instrutor(id_instrutor)
        AulaDAO.atualizar(c)
    def aula_excluir():
        for a in View.aula_listar():
            if a.get_id_aluno() != None and a.get_id_aluno() != None and a.get_id_esporte() != None:
                raise ValueError("Aula não pode ser excluída.")
        c = Aula(id, None)
        AulaDAO.excluir(c)

    # INSCRIÇÃO
    def inscricao_listar():
        return inscricaoDAO.listar()

    def inscricao_listar_id(id):
        return inscricaoDAO.listar_id()

    def inscricao_inserir(status, data):
        c = Inscricao(status, data)
        InscricaoDAO.inserir(c)

    def inscricao_atualizar():
        for a in View.inscricao_listar():
            

    def inscricao_excluir():
        pass


    def pagamento_listar():
        pass

    def pagamento_listar_id(id):
        pass

    def pagamento_inserir():
        pass

    def pagamento_atualizar():
        pass

    def pagamento_excluir():
        pass