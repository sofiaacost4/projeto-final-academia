import streamlit as st
from view import View
import pandas as pd

class MinhasAulasInstrutorUI:
    def main():
        st.header("Minhas Aulas")
        usuario_id = st.session_state.get("usuario_id")
        usuario_tipo = st.session_state.get("usuario_tipo")
        if usuario_tipo != "instrutor":
            st.error("Instrutor não autenticado.")
            return
        instrutor = View.instrutor_listar_id(usuario_id)
        aulas = View.aula_listar()
        aulas_instrutor = [
            a for a in aulas 
            if a.get_id_instrutor() == instrutor.get_id()]
        if not aulas_instrutor:
            st.info("Você não possui nenhuma aula agendada.")
            return
        dados_tabela = []
        for aula in aulas_instrutor:
            esporte = View.esporte_listar_id(aula.get_id_esporte())        
            dados_tabela.append({
                "Data e Horário": aula.get_dia().strftime("%d/%m/%Y %H:%M"),
                "Esporte": esporte.get_tipo() if esporte else "—"})

        st.dataframe(dados_tabela, use_container_width=True)
