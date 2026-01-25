import streamlit as st
from view import View
import pandas as pd

class MinhasAulasUI:
    @staticmethod
    def main(): 
        if "usuario_id" not in st.session_state or st.session_state["usuario_tipo"] != "aluno":
            st.error("Acesso restrito. Por favor, faça login como aluno.")
            return
        aluno_id = st.session_state["usuario_id"]
        st.header("Minhas Aulas")
        aulas = View.aulas_do_aluno(aluno_id) 
        if not aulas:
            st.info("Você ainda não possui aulas agendadas. Verifique se há pagamentos pendentes.")
            return
        dados_tabela = []
        for a in aulas:
            esporte = View.esporte_listar_id(a.get_id_esporte())
            instrutor = View.instrutor_listar_id(a.get_id_instrutor())
            dados_tabela.append({
                "Data e Hora": a.get_dia().strftime('%d/%m/%Y %H:%M'),
                "Esporte": esporte.get_tipo() if esporte else "N/A",
                "Instrutor": instrutor.get_nome() if instrutor else "N/A"})
        df = pd.DataFrame(dados_tabela)
        st.dataframe(
            df, 
            use_container_width=True, 
            hide_index=True)