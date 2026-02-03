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
        if aluno is None:
            raise ValueError("Aluno não encontrado.")
        if aluno.get_email() == "gestor":
            raise ValueError("Gestor não pode ser excluído.")
        for inscricao in View.inscricao_listar():
            if inscricao.get_id_aluno() == id:
                raise ValueError("Aluno não pode ser excluído, pois possui inscrições ativas.")
        for aula in View.aula_listar():
            if hasattr(aula, 'get_id_aluno') and aula.get_id_aluno() == id:
                raise ValueError("Aluno não pode ser excluído, pois está vinculado a uma aula.")
        for aa in View.aula_aluno_listar():
            if aa.get_id_aluno() == id:
                raise ValueError("Aluno não pode ser excluído, pois está vinculado a uma aula.")
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
            if i.get_id_esporte() == id_esporte}

        return[
            a for a in alunos
            if a.get_id() in ids_alunos]

    def esporte_excluir(id):
        for i in View.inscricao_listar():
            if i.get_id_esporte() == id:
                raise ValueError(
                    "Não é possível excluir este esporte, pois há alunos inscritos."
                )
        EsporteDAO.excluir(id)

    # AULA

    @staticmethod
    def aula_listar():
        return AulaDAO.listar()
    
    @staticmethod
    def aula_listar_id(id):
        return AulaDAO.listar_id(id)
    
    @staticmethod
    def aula_inserir(data_hora, esporte, instrutor):
        for a in View.aula_listar():
            if (
                a.get_id_esporte() == esporte and
                a.get_id_instrutor() == instrutor and
                a.get_dia() == data_hora):
                raise ValueError(
                    "Já existe uma aula desse esporte com esse instrutor nesse dia e horário.")
        AulaDAO.inserir(
            Aula(
                id=0,
                id_esporte=esporte,
                dia=data_hora,
                id_instrutor=instrutor))

    @staticmethod
    def aula_atualizar(id, id_esporte, dia, id_instrutor):
        for a in View.aula_listar():
            if (
                a.get_id() != id and
                a.get_dia() == dia and
                a.get_id_instrutor() == id_instrutor):
                raise ValueError(
                    "Essa data já está cadastrada na agenda deste instrutor.")
        aula = Aula(
            id=id,
            id_esporte=id_esporte,
            dia=dia,
            id_instrutor=id_instrutor)
        AulaDAO.atualizar(aula)

    @staticmethod
    def aula_excluir(id):
        aula = View.aula_listar_id(id)
        if aula is None:
            raise ValueError("Aula não encontrada.")

        vinculacoes = AulaAlunoDAO.listar()
        for v in vinculacoes:
            if v.get_id_aula() == id:
                raise ValueError("Aula não pode ser excluída pois possui alunos inscritos.")
        AulaDAO.excluir(id)

    @staticmethod
    def aula_adicionar_aluno(id_aula, id_aluno):
        aula = AulaDAO.listar_id(id_aula)
        if aula is None:
            raise ValueError("Aula não encontrada.")

        inscricao = next(
            (
                i for i in View.inscricao_listar()
                if i.get_id_aluno() == id_aluno
                and i.get_id_esporte() == aula.get_id_esporte()
                and i.get_status() == "Confirmado"
            ),
            None
        )

        if inscricao is None:
            raise ValueError("Aluno não possui inscrição paga neste esporte.")

        AulaAlunoDAO.inserir(AulaAluno(None, id_aula, id_aluno))

    @staticmethod
    def criar_aulas_em_lote(id_esporte, id_instrutor, datas):
        for dia in datas:
            AulaDAO.inserir(
                Aula(
                    id=0,
                    id_esporte=id_esporte,
                    dia=dia,
                    id_instrutor=id_instrutor))

    @staticmethod
    def aulas_por_esporte():
        resultado = {}
        for a in View.aula_listar():
            resultado.setdefault(a.get_id_esporte(), []).append(a)
        return resultado
    
    @staticmethod
    def aulas_do_instrutor(id_instrutor):
        return [a for a in View.aula_listar() if a.get_id_instrutor() == id_instrutor]

    @staticmethod
    def aluno_tem_conflito_horario(id_aluno, data_hora_aula):
        vinculos = View.aula_aluno_listar()
        aulas = View.aula_listar()
        
        ids_aulas_aluno = [v.get_id_aula() for v in vinculos if v.get_id_aluno() == id_aluno]
        
        for aula in aulas:
            if aula.get_id() in ids_aulas_aluno:
                data_existente = aula.get_dia().strftime("%Y-%m-%d %H:%M")
                data_nova = data_hora_aula.strftime("%Y-%m-%d %H:%M")
                
                if data_existente == data_nova:
                    return True
        return False

    @staticmethod
    def aula_criar_com_intervalo(id_esporte, id_instrutor, data_inicio, intervalo_tipo, intervalo_valor, quantidade):
        data_atual = data_inicio
        alunos_aptos = View.alunos_por_esporte(id_esporte)
        
        for _ in range(quantidade):
            aulas_existentes = View.aula_listar()
            data_formatada = data_atual.strftime('%d/%m/%Y às %H:%M')

            conflito_instrutor = any(
                a.get_id_instrutor() == id_instrutor and a.get_dia() == data_atual 
                for a in aulas_existentes
            )
            if conflito_instrutor:
                raise ValueError(f"Erro: O instrutor já possui uma aula em {data_formatada}!")

            for aluno in alunos_aptos:
                if View.aluno_tem_conflito_horario(aluno.get_id(), data_atual):
                    raise ValueError(f"Erro: O aluno(a) {aluno.get_nome()} já tem aula em {data_formatada}!")

            ja_existe_aula = any(
                a.get_id_esporte() == id_esporte and a.get_dia() == data_atual 
                for a in aulas_existentes
            )
            if ja_existe_aula:
                raise ValueError(f"Erro: Já existe uma aula deste esporte em {data_formatada}!")
            id_aula_gerado = AulaDAO.inserir(Aula(0, id_esporte, data_atual, id_instrutor))
            
            if id_aula_gerado:
                for aluno in alunos_aptos:
                    AulaAlunoDAO.inserir(AulaAluno(None, id_aula_gerado, aluno.get_id()))

            if intervalo_tipo == "dias": data_atual += timedelta(days=intervalo_valor)
            elif intervalo_tipo == "semanas": data_atual += timedelta(weeks=intervalo_valor)
            elif intervalo_tipo == "meses": data_atual += timedelta(days=30 * intervalo_valor)

    @staticmethod
    def aulas_do_aluno(aluno_id):
        aulas = View.aula_listar()
        aula_alunos = View.aula_aluno_listar() 
        ids_aulas_do_aluno = [
            aa.get_id_aula() for aa in aula_alunos if aa.get_id_aluno() == aluno_id]
        return [a for a in aulas if a.get_id() in ids_aulas_do_aluno]

    @staticmethod
    def alunos_da_aula(aula):
        vinculacoes = AulaAlunoDAO.listar()
        todos_alunos = View.aluno_listar()
        ids_alunos_na_aula = [v.get_id_aluno() for v in vinculacoes if v.get_id_aula() == aula.get_id()]
        
        return [a for a in todos_alunos if a.get_id() in ids_alunos_na_aula]

    @staticmethod
    def aula_aluno_listar():
        return AulaAlunoDAO.listar()

    # INSCRIÇÃO
    def inscricao_listar():
        return InscricaoDAO.listar()

    def inscricao_listar_id(id):
        return InscricaoDAO.listar_id()

    def inscricao_inserir(id_aluno, id_esporte, status):
            instrutores = View.instrutor_listar_obj()
            tem_instrutor = any(i.get_especialidade() == id_esporte for i in instrutores)

            if not tem_instrutor:
                raise ValueError("Não é possível se inscrever: este esporte não possui instrutores vinculados.")

            obj = Inscricao(
                id=None,
                id_aluno=id_aluno,
                id_esporte=id_esporte,
                status=status)
            InscricaoDAO.inserir(obj)
            
    def inscricao_excluir(id):
            inscricoes = View.inscricao_listar()
            inscricao = next((i for i in inscricoes if i.get_id() == id), None)
            if not inscricao:
                raise ValueError("Inscrição não encontrada.")
            status_atual = inscricao.get_status().lower()
            if status_atual in ["pago", "confirmado"]:
                raise ValueError(f"Não é possível cancelar uma inscrição com status '{inscricao.get_status()}'.")
            InscricaoDAO.excluir(id)

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
            id_inscricao=id_inscricao)
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
    @staticmethod
    def pagamento_confirmar_fluxo(id_inscricao, valor):
        """
        Realiza o fluxo completo: Cria o registro de pagamento e 
        atualiza o status da inscrição para 'Confirmado'.
        """
        try:
            View.pagamento_inserir(
                status="Pago",
                valor=valor,
                id_inscricao=id_inscricao)
            View.inscricao_confirmar(id_inscricao)
        except Exception as e:
            raise ValueError(f"Falha na operação: {e}")