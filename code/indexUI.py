from view import View
from templates.manteralunoUI import ManterAlunoUI
from models.dao_sql.dao import DAO
import streamlit as st

class IndexUI:
    def menu_gestor():
        op = st.sidebar.selectbox("Menu", [
            "Cadastro de Alunos"
        ])
        if op == "Cadastro de Alunos": ManterAlunoUI.main()

    def menu_aluno():
        op = st.sidebar.selectbox("Menu", [
            "Listar alunos",
            "Inserir alunos",
            "Atualizar alunos",
            "Excluir alunos"
        ])
        if op == "Listar alunos": ManterAlunoUI.listar()
        if op == "Inserir alunos": ManterAlunoUI.inserir()
        if op == "Atualizar alunos": ManterAlunoUI.atualizar()
        if op == "Excluir alunos": ManterAlunoUI.excluir()

    def sidebar():
        if "aluno_id" not in st.session_state: IndexUI.menu_visitante()
        else: st.sidebar.write("Bem-vindo(a), " + st.session_state["aluno_nome"])
        gestor = st.session_state["aluno_nome"] == "gestor"
        if gestor: IndexUI.menu_gestor()
        else: IndexUI.menu_aluno()
        IndexUI.sair_do_sistema()
    
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["aluno_id"]
            del st.session_state["aluno_nome"]
            st.rerun()

    def main():
        View.criar_gestor()
        IndexUI.sidebar()

DAO.criar_tabelas()
IndexUI.main()