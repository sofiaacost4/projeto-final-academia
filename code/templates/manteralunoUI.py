import streamlit as st
import pandas as pd 
from view import View
import time

class ManterAlunoUI:
    def main():
        st.header("Cadastro de Alunos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterAlunoUI.listar()
        with tab2: ManterAlunoUI.inserir()
        with tab3: ManterAlunoUI.atualizar()
        with tab4: ManterAlunoUI.excluir()

    def listar():
        alunos = View.aluno_listar()
        if len(alunos) == 0: st.write("Nenhum aluno cadastrado.")
        else:
            list_dic = []
            for obj in alunos: list_dic.append(obj.to_dic())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id", "nome", "email", "fone"])

    def inserir():
        nome = st.text_input("Informe o nome: ")
        email = st.text_input("Informe o e-mail: ")
        fone = st.text_input("Informe o telefone: ")
        senha = st.text_input("Informe a senha: ", type="password")
        if st.button("Inserir"):
            try:
                View.aluno_inserir(nome, email, fone, senha)
                st.success("Aluno inserido com sucesso.")
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

    def atualizar():
        alunos = View.aluno_listar()
        if len(alunos) == 0: st.write("Nenhum aluno cadastrado.")
        else:
            op = st.selectbox("Atualização de alunos", alunos)
            nome = st.text_input("Informe o novo nome: ", op.get_nome())
            email = st.text_input("Informe o novo e-mail: ", op.get_email())
            fone = st.text_input("Informe o novo telefone: ", op.get_fone())
            senha = st.text_input("Informe a nova senha: ", op.get_senha(), type="password")
            if st.button("Atualizar"):
                id = op.get_id()
                View.aluno_atualizar(id, nome, email, fone, senha)
                st.success("Aluno atualizado com sucesso.")
                time.sleep(2)
                st.rerun()
    
    def excluir():
        alunos = View.aluno_listar()
        if len(alunos) == 0: st.write("Nenhum aluno cadastrado")
        else: 
            op = st.selectbox("Exclusão de Alunos", alunos)
            if st.button("Excluir"):
                try:
                    id = op.get_id()
                    View.aluno_excluir(id)
                    st.success("Aluno excluído com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()
