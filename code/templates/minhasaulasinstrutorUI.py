# página de Aulas (Perfil do Instrutor) onde aparece todas as aulas que aquele Instrutor irá ministrar
import streamlit as st
from view import View

class MinhasAulasInstrutorUI:
    def main():
        st.header("Minhas aulas")

        instrutor = st.session_state.get("instrutor")

        aulas = View.aula_listar()

        aulas_instrutor = [
            a for a in aulas
            if a.get_id_instrutor() == instrutor.get_id()
        ]

        if not aulas_instrutor:
            st.info("Você não possui nenhuma aula agendada.")
            return
        
        for aula in aulas_instrutor:
            aluno = View.aluno_listar_id(aula.get_id_aluno())
            esporte = View.esporte_listar_id(aula.get_id_esporte())

            col1, col2, col3 = st.columns(3)

            with col1:
                st.write(aula.get_dia().strftime("%d/%m/%Y %H:%M"))

            with col2:
                st.write(aluno.get_nome() if aluno else "—")

            with col3:
                st.write(esporte.get_tipo() if esporte else "—")


