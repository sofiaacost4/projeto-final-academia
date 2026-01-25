from models.aluno import Aluno
from models.aula import Aula
from models.aulaaluno import AulaAluno
from models.instrutor import Instrutor
from models.esporte import Esporte
from models.inscricao import Inscricao
from models.pagamento import Pagamento
from models.dao_sql.alunodao import AlunoDAO
from models.dao_sql.auladao import AulaDAO
from models.dao_sql.aulaalunodao import AulaAlunoDAO
from models.dao_sql.instrutordao import InstrutorDAO
from models.dao_sql.esportedao import EsporteDAO
from models.dao_sql.inscricaodao import InscricaoDAO
from models.dao_sql.pagamentodao import PagamentoDAO
from datetime import timedelta

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
            for i in View.instrutor_listar_obj():
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
    
    def instrutor_listar_obj():
        return InstrutorDAO.listar()
    
    def instrutor_listar_id(id):
        instrutor = InstrutorDAO.listar_id(id)
        return instrutor
    
    def instrutor_inserir(nome, email, especialidade, fone, senha):
        try:
            for a in View.aluno_listar():
                if a.get_email() == email:
                    raise ValueError("Este email não está disponível.")
            for i in View.instrutor_listar_obj():
                if i.get_email() == email:
                    raise ValueError("Este email não está disponível.")
            instrutor = Instrutor(0, nome, email, especialidade, fone, senha)
            InstrutorDAO.inserir(instrutor)
        except ValueError as erro:
            raise erro
        
    def instrutor_atualizar(id, nome, email, especialidade, fone, senha):
        if email == "gestor":
            raise ValueError("Este email é de uso exclusivo do gestor.")
        for a in View.aluno_listar():
            if a.get_id() != id:
                if a.get_email() == email:
                    raise ValueError("Este email não está disponível.")
        for i in View.instrutor_listar_obj():
            if i.get_email() == email and i.get_id() != id:
                raise ValueError("Este email não está disponível.")
        instrutor = Instrutor(id, nome, email, especialidade, fone, senha)
        InstrutorDAO.atualizar(instrutor)

    def instrutor_excluir(id):
        instrutor = View.instrutor_listar_id(id)
        if instrutor is None:
            raise ValueError("Instrutor não encontrado.")
        InstrutorDAO.excluir(id)

    def instrutor_autenticar(email, senha):
        for p in View.instrutor_listar_obj():
            if p.get_email() == email and p.get_senha() == senha:
                return {
                    "id": p.get_id(),
                    "nome": p.get_nome()
                }
        return None

    # ESPORTE
    # Novas funcionalidades

    def esporte_listar():
        r = EsporteDAO.listar()
        return r
    
    def esporte_listar_id(id):
        esporte = EsporteDAO.listar_id(id)
        return esporte

    def esporte_inserir(tipo, valor):
        for a in View.esporte_listar():
            if a.get_tipo() == tipo:
                raise ValueError("Este esporte não está disponível.")
        esporte = Esporte(0, tipo, valor)
        EsporteDAO.inserir(esporte)

    def esporte_atualizar(id, tipo, valor):
        for e in View.esporte_listar():
            if e.get_id() != id and e.get_tipo() == tipo:
                raise ValueError("Este esporte não está disponível.")
        esporte = Esporte(id, tipo, valor)
        EsporteDAO.atualizar(esporte)

    def esporte_com_alunos_instrutores():
        esportes = View.esporte_listar()
        inscricoes = View.inscricao_listar()
        alunos = View.aluno_listar()
        instrutores = View.instrutor_listar_obj()

        resultado = []

        for e in esportes:
            alunos_do_esporte = [
                a.get_nome()
                for i in inscricoes
                if i.get_id_esporte() == e.get_id()
                for a in alunos
                if a.get_id() == i.get_id_aluno()
            ]

            instrutores_do_esporte = [
                i.get_nome()
                for i in instrutores
                if i.get_especialidade() == e.get_id()
            ]

            resultado.append({
                "esporte": e,
                "alunos": alunos_do_esporte,
                "instrutores": instrutores_do_esporte
            })

        return resultado

    def esportes_disponiveis_para_aluno(id_aluno):
        todos_esportes = View.esporte_listar()
        inscricoes = View.inscricao_listar()
        esportes_inscritos = {i.get_id_esporte() for i in inscricoes if i.get_id_aluno() == id_aluno}
        return [e for e in todos_esportes if e.get_id() not in esportes_inscritos]
    
    def instrutores_por_esporte(id_esporte):
        instrutores = View.instrutor_listar_obj()
        return [
            i for i in instrutores
            if i.get_especialidade() == id_esporte
        ]

    def alunos_por_esporte(id_esporte):
        inscricoes = View.inscricao_listar()
        alunos = View.aluno_listar()

        ids_alunos = {
            i.get_id_aluno()
            for i in inscricoes
            if i.get_id_esporte() == id_esporte
        }

        return [
            a for a in alunos
            if a.get_id() in ids_alunos
        ]

    def esporte_excluir(id):
        for i in View.inscricao_listar():
            if i.get_id_esporte() == id:
                raise ValueError(
                    "Não é possível excluir este esporte, pois há alunos inscritos."
                )
        EsporteDAO.excluir(id)

    # AULA

    def aula_listar():
        return AulaDAO.listar()
    def aula_listar_id(id):
        return AulaDAO.listar_id()
    def aula_inserir(id_esporte, dia, id_instrutor, confirmada=False):
        for a in View.aula_listar():
            if a.get_dia() == dia and a.get_id_instrutor() == id_instrutor:
                raise ValueError(
                    "Essa data já está cadastrada na agenda deste instrutor."
                )

        aula = Aula(
            0,       
            id_esporte,
            dia,
            id_instrutor,
            confirmada
        )

        AulaDAO.inserir(aula)


    def aula_atualizar(id, id_esporte, dia, confirmado, id_instrutor):
        for a in View.aula_listar():
            if (
                a.get_id() != id and
                a.get_dia() == dia and
                a.get_id_instrutor() == id_instrutor):
                raise ValueError(
                    "Essa data já está cadastrada na agenda deste instrutor.")
        aula = Aula(
            id,
            id_esporte,
            dia,
            confirmado,
            id_instrutor)
        AulaDAO.atualizar(aula)

    def aula_excluir(id):
        aula = View.aula_listar_id(id)
        if aula is None:
            raise ValueError("Aula não encontrada.")
        if aula.get_id_aluno() is not None or aula.get_id_esporte() is not None or aula.get_id_instrutor() is not None:
            raise ValueError("Aula não pode ser excluída.")
        AulaDAO.excluir(id)
    def aula_adicionar_aluno(id_aula, id_aluno):
        aula = AulaDAO.listar_id(id_aula)
        if aula is None:
            raise ValueError("Aula não encontrada.")

        inscricao = next(
            (
                i for i in View.inscricao_listar()
                if i.get_id_aluno() == id_aluno
                and i.get_id_esporte() == aula.get_id_esporte()
                and i.get_status() == "Pago"
            ),
            None
        )

        if inscricao is None:
            raise ValueError("Aluno não possui inscrição paga neste esporte.")

        AulaAlunoDAO.inserir(AulaAluno(None, id_aula, id_aluno))
    def criar_aulas_em_lote(id_esporte, id_instrutor, datas):
        for dia in datas:
            AulaDAO.inserir(
                Aula(
                    0,
                    id_esporte,
                    id_instrutor,
                    dia,
                    False))
    def aulas_por_esporte():
        resultado = {}
        for a in View.aula_listar():
            resultado.setdefault(a.get_id_esporte(), []).append(a)
        return resultado
    def aulas_do_instrutor(id_instrutor):
        return [a for a in View.aula_listar() if a.get_id_instrutor() == id_instrutor]
    def aulas_do_aluno(id_aluno):
        aulas = View.aula_listar()
        vinculacoes = AulaAlunoDAO.listar()
        ids_aulas = {v.get_id_aula() for v in vinculacoes if v.get_id_aluno() == id_aluno}
        return [a for a in aulas if a.get_id() in ids_aulas]
    from datetime import timedelta
    def aula_criar_com_intervalo(
        id_esporte,
        id_instrutor,
        data_inicio,
        intervalo_tipo,
        intervalo_valor,
        quantidade
    ):
        """
        intervalo_tipo: 'dias', 'semanas', 'meses'
        intervalo_valor: int
        quantidade: número de aulas a criar
        """
        aulas_criadas = []
        data_atual = data_inicio
        for _ in range(quantidade):
            for a in View.aula_listar():
                if a.get_dia() == data_atual and a.get_id_instrutor() == id_instrutor:
                    raise ValueError(
                        f"Conflito de horário em {data_atual.strftime('%d/%m/%Y %H:%M')}")
            aula = Aula(
                id=0,
                id_esporte=id_esporte,
                id_instrutor=id_instrutor,
                dia=data_atual,
                confirmada=False)
            AulaDAO.inserir(aula)
            aulas_criadas.append(data_atual)
            if intervalo_tipo == "dias":
                data_atual += timedelta(days=intervalo_valor)
            elif intervalo_tipo == "semanas":
                data_atual += timedelta(weeks=intervalo_valor)
            elif intervalo_tipo == "meses":
                data_atual += timedelta(days=30 * intervalo_valor)
            else:
                raise ValueError("Tipo de intervalo inválido.")
        return aulas_criadas

    # INSCRIÇÃO

    def inscricao_listar():
        return InscricaoDAO.listar()

    def inscricao_listar_id(id):
        return InscricaoDAO.listar_id()

    def inscricao_inserir(id_aluno, id_esporte, status):
        obj = Inscricao(
            id=None,
            id_aluno=id_aluno,
            id_esporte=id_esporte,
            status=status)
        InscricaoDAO.inserir(obj)
        
    def inscricao_excluir():
        for a in View.inscricao_listar():
            if a.get_status() == "confirmado": 
                raise ValueError("Inscrição não pode ser excluída, pois ainda está ativa.")

    def inscricao_confirmar(id_inscricao):
        ins = InscricaoDAO.listar_id(id_inscricao)
        if ins is None:
            raise ValueError("Inscrição não encontrada.")
        ins.set_status("Confirmado")
        InscricaoDAO.atualizar(ins)

    @staticmethod
    def pagamento_listar():
        return PagamentoDAO.listar()

    @staticmethod
    def pagamento_listar_id(id):
        return PagamentoDAO.listar_id(id)

    @staticmethod
    def pagamento_inserir(status, valor, id_inscricao):
        p = Pagamento(
            id=None,
            status=status,
            valor=valor,
            id_inscricao=id_inscricao
        )
        PagamentoDAO.inserir(p)
        return p

    @staticmethod
    def pagamento_atualizar(id, status=None, valor=None, id_inscricao=None):
        p = PagamentoDAO.listar_id(id)
        if p is None:
            raise ValueError("Pagamento não encontrado.")
        if status: p.set_status(status)
        if valor: p.set_valor(valor)
        if id_inscricao: p.set_id_inscricao(id_inscricao)
        PagamentoDAO.atualizar(p)

    @staticmethod
    def pagamento_excluir(id):
        p = PagamentoDAO.listar_id(id)
        if p is None:
            raise ValueError("Pagamento não encontrado.")
        PagamentoDAO.excluir(id)