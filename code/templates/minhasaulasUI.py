import streamlit as st
from view import View

class MinhasAulasUI:
    def main():
        if "usuario_id" not in st.session_state or st.session_state["usuario_tipo"] != "aluno":
            st.error("Aluno não logado!")
            return

        aluno_id = st.session_state["usuario_id"]
        st.header("Minhas Aulas")

        aulas = View.aulas_do_aluno(aluno_id)
        if not aulas:
            st.info("Você não possui aulas cadastradas.")
            return

        for a in aulas:
            esporte = View.esporte_listar_id(a.get_id_esporte())
            instrutor = View.instrutor_listar_id(a.get_id_instrutor())
            st.write(
                f"Esporte: {esporte.get_tipo()} | "
                f"Instrutor: {instrutor.get_nome()} | "
                f"Data: {a.get_dia().strftime('%d/%m/%Y %H:%M')} | "
                f"Confirmada: {'Sim' if a.get_confirmada() else 'Não'}"
            )
