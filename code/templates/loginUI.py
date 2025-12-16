import streamlit as st
from view import View

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            p = View.instrutor_autenticar(email, senha)
            c = View.aluno_autenticar(email, senha)
            if c == None and p == None: st.error("E-mail ou senha inválidos")
            elif c:
                st.session_state["usuario_id"] = c["id"]
                st.session_state["usuario_nome"] = c["nome"]
                st.session_state["usuario_tipo"] = "aluno" # pega o tipo de usuário que faz o login, nesse caso, aluno
                st.rerun()
            elif p:
                st.session_state["usuario_id"] = p["id"]
                st.session_state["usuario_nome"] = p["nome"]
                st.session_state["usuario_tipo"] = "instrutor" # pega o tipo de usuário que faz o login, nesse caso, instrutor
                st.rerun()