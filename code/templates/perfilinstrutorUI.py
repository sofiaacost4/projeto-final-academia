import streamlit as st
from view import View
import time

class PerfilInstrutorUI:
    def main():
        especialidades = View.esporte_listar()
        st.header("Meus Dados")
        op = View.instrutor_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        especialidade = st.selectbox("Informe a especialidade com base nos esportes já cadastrados", especialidades)
        fone = st.text_input("Informe o novo fone", op.get_fone())
        senha = st.text_input("Informe a nova senha", op.get_senha(),
        type="password")
        if st.button("Atualizar"):
            try:
                id = op.get_id()
                View.instrutor_atualizar(id, nome, email, especialidade, fone, senha)
                st.success("Instrutor atualizado com sucesso")
            except ValueError as erro:
                st.error(str(erro))
