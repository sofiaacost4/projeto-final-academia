from view import View
from templates.loginUI import LoginUI
from templates.abrircontaUI import AbrirContaUI
from templates.manteralunoUI import ManterAlunoUI
from templates.manterinstrutorUI import ManterInstrutorUI
from templates.manteresporteUI import ManterEsporteUI
from templates.manteraulaUI import ManterAulaUI
from templates.manterinscricaoUI import ManterInscricaoUI
from templates.gerenciarpagamentoUI import GerenciarPagamentoUI
from templates.minhasaulasUI import MinhasAulasUI
from templates.minhasaulasinstrutorUI import MinhasAulasInstrutorUI
from templates.verturmasUI import VerTurmasUI
from templates.verpagamentosUI import VerPagamentoUI
from templates.verinscricoesUI import VerInscricoesUI
from templates.perfilalunoUI import PerfilAlunoUI
from templates.perfilinstrutorUI import PerfilInstrutorUI
from templates.inscricoesUI import InscricoesAlunoUI
from templates.cancelarinscricao import CancelarInscricaoUI
from models.dao_sql.dao import DAO

import streamlit as st

class IndexUI:
    def menu_gestor():
        menu_principal = st.sidebar.selectbox("Navegação", ["Cadastros", "Gerenciamento"])

        if menu_principal == "Cadastros":
            sub_op = st.sidebar.selectbox(
                "Cadastro de", 
                ["Alunos", "Instrutores", "Esportes", "Aulas", "Inscrições"]
            )
            
            if sub_op == "Alunos": ManterAlunoUI.main()
            if sub_op == "Instrutores": ManterInstrutorUI.main()
            if sub_op == "Esportes": ManterEsporteUI.main()
            if sub_op == "Aulas": ManterAulaUI.main()
            if sub_op == "Inscrições": ManterInscricaoUI.main()

        elif menu_principal == "Gerenciamento":
            sub_op = st.sidebar.selectbox("Ver", ["Pagamentos", "Turmas"])
            
            if sub_op == "Pagamentos": VerPagamentoUI.main()
            if sub_op == "Turmas": VerTurmasUI.main()

    def menu_visitante():
        st.title("GymTime")
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_aluno():
        menu_principal = st.sidebar.selectbox("Navegação", ["Perfil e Pagamentos", "Atividades e Inscrições"])

        if menu_principal == "Perfil e Pagamentos":
            sub_op = st.sidebar.selectbox(
                "Opções:", 
                ["Meus Dados", "Gerenciamento de Pagamento"]
            )
            if sub_op == "Meus Dados": PerfilAlunoUI.main()
            if sub_op == "Gerenciamento de Pagamento": GerenciarPagamentoUI.main()

        elif menu_principal == "Atividades e Inscrições":
            sub_op = st.sidebar.selectbox(
                "Opções:", 
                ["Inscreva-se", "Ver minhas aulas", "Ver minhas inscrições", "Cancelar inscrições"]
            )
            if sub_op == "Inscreva-se": InscricoesAlunoUI.main()
            if sub_op == "Ver minhas aulas": MinhasAulasUI.main()
            if sub_op == "Ver minhas inscrições": VerInscricoesUI.main()
            if sub_op == "Cancelar inscrições": CancelarInscricaoUI.main()

    def menu_instrutor():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Ver minhas aulas"])
        if op == "Meus Dados": PerfilInstrutorUI.main()
        if op == "Ver minhas aulas": MinhasAulasInstrutorUI.main()

    def sidebar():
        if "usuario_nome" not in st.session_state: 
            IndexUI.menu_visitante()
        else:
            aluno = st.session_state["usuario_tipo"] == "aluno"
            instrutor = st.session_state["usuario_tipo"] == "instrutor"
            gestor = st.session_state["usuario_nome"] == "gestor"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if gestor: IndexUI.menu_gestor()
            elif aluno: IndexUI.menu_aluno()
            elif instrutor: IndexUI.menu_instrutor()
            IndexUI.sair_do_sistema()
        return None

    def main():
        IndexUI.sidebar()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()
            
View.criar_gestor()

IndexUI.main()