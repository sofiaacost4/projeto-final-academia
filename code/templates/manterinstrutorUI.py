import streamlit as st
import pandas as pd 
from view import View
import time

class ManterInstrutorUI:
    def main():
        st.header("Cadastro de Instrutores")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterInstrutorUI.listar()
        with tab2: ManterInstrutorUI.inserir()
        with tab3: ManterInstrutorUI.atualizar()
        with tab4: ManterInstrutorUI.excluir()

    def listar():
        instrutores = View.instrutor_listar()
        if len(instrutores) == 0: st.write("Nenhum instrutor cadastrado.")
        else:
            list_dic = []
            for obj in instrutores: list_dic.append(obj.to_dic())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id", "nome", "especialidade", "email", "fone"])

    def inserir():
        especialidades = View.esporte_listar()
        nome = st.text_input("Informe o nome:")
        email = st.text_input("Informe o e-mail:")
        esporte_selecionado = st.selectbox(
            "Informe a especialidade de acordo com os esportes cadastrados:",
            especialidades,
            format_func=lambda e: e.get_tipo())
        fone = st.text_input("Informe o telefone:")
        senha = st.text_input("Informe a senha:", type="password")
        if st.button("Inserir"):
            try:
                View.instrutor_inserir(
                    nome, email, esporte_selecionado.get_id(), fone, senha)
                st.success("Instrutor inserido com sucesso.")
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

    def atualizar():
        instrutores = View.instrutor_listar()
        if len(instrutores) == 0: st.write("Nenhum instrutor cadastrado.")
        else:
            especialidades = View.esporte_listar()
            op = st.selectbox("Atualização de instrutores", instrutores)
            nome = st.text_input("Informe o novo nome: ", op.get_nome())
            email = st.text_input("Informe o novo e-mail: ", op.get_email())
            especialidade = st.selectbox("Informe a especialidade de acordo com os esportes já cadastrados: ", especialidades)
            fone = st.text_input("Informe o novo telefone: ", op.get_fone())
            senha = st.text_input("Informe a nova senha: ", op.get_senha(), type="password")
            if st.button("Atualizar"):
                id = op.get_id()
                View.instrutor_atualizar(id, nome, email, especialidade, fone, senha)
                st.success("Instrutor atualizado com sucesso.")
                time.sleep(2)
                st.rerun() # criar erro mais a frente que impeça o instrutor de atualizar a própria especialidade se o instrutor estiver associado a uma aula/horário;
    
    def excluir():
        instrutores = View.instrutor_listar()
        if len(instrutores) == 0: st.write("Nenhum instrutor cadastrado")
        else: 
            op = st.selectbox("Exclusão de Instrutores", instrutores)
            if st.button("Excluir"):
                try:
                    id = op.get_id()
                    View.instrutor_excluir(id)
                    st.success("Instrutor excluído com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun() # criar erro mais a frente pra não poder excluir instrutores associados a uma aula(horário);
