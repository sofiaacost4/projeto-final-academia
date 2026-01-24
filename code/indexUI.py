from view import View
from templates.loginUI import LoginUI
from templates.abrircontaUI import AbrirContaUI
from templates.manteralunoUI import ManterAlunoUI
from templates.manterinstrutorUI import ManterInstrutorUI
from templates.manteresporteUI import ManterEsporteUI
from templates.manteraulaUI import ManterAulaUI
from templates.manterinscricaoUI import ManterInscricaoUI
from templates.gerenciarpagamentoUI import GerenciarPagamentoUI
from templates.perfilalunoUI import PerfilAlunoUI
from templates.perfilinstrutorUI import PerfilInstrutorUI
from templates.inscricoesUI import InscricoesAlunoUI
from models.dao_sql.dao import DAO

import streamlit as st

class IndexUI:
    def menu_gestor():
        op = st.sidebar.selectbox("Menu", ["Cadastro de Alunos", "Cadastro de Instrutores", "Cadastro de Esportes", "Cadastro de Aulas", "Cadastro de Inscrições", "Gerenciamento de Pagamento"])
        if op == "Cadastro de Alunos": ManterAlunoUI.main()
        if op == "Cadastro de Instrutores": ManterInstrutorUI.main()
        if op == "Cadastro de Esportes": ManterEsporteUI.main()
        if op == "Cadastro de Aulas": ManterAulaUI.main()
        if op == "Cadastro de Inscrições": ManterInscricaoUI.main()
        if op == "Gerenciamento de Pagamentos": GerenciarPagamentoUI.main()

    def menu_visitante():
        st.title("GymTime")
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_aluno():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Gerenciamento de Pagamento", "Inscrições"])
        if op == "Meus Dados": PerfilAlunoUI.main()
        if op == "Gerenciamento de Pagamento": GerenciarPagamentoUI.main()
        if op == "Inscrições": InscricoesAlunoUI.main()

    def menu_instrutor():
        op = st.sidebar.selectbox("Menu", ["Meus Dados"])
        if op == "Meus Dados": PerfilInstrutorUI.main()

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