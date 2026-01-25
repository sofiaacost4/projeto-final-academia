import streamlit as st
from view import View
import pandas as pd

class MinhasAulasInstrutorUI:
    @staticmethod
    def main():
        st.header("Minha Agenda de Aulas")
        usuario_id = st.session_state.get("usuario_id")
        usuario_tipo = st.session_state.get("usuario_tipo")       
        if usuario_tipo != "instrutor":
            st.error("Acesso restrito. Por favor, faça login como instrutor.")
            return
        aulas_instrutor = View.aulas_do_instrutor(usuario_id)
        if not aulas_instrutor:
            st.info("Você não possui nenhuma aula agendada no momento.")
            return
        dados_tabela = []
        for aula in aulas_instrutor:
            esporte = View.esporte_listar_id(aula.get_id_esporte())
            alunos = View.alunos_da_aula(aula)
            nomes_alunos = ", ".join([aluno.get_nome() for aluno in alunos]) or "Nenhum aluno vinculado"
            dados_tabela.append({
                "Data e Horário": aula.get_dia().strftime("%d/%m/%Y %H:%M"),
                "Esporte": esporte.get_tipo() if esporte else "—",
                "Alunos Matriculados": nomes_alunos})
        df = pd.DataFrame(dados_tabela)
        st.dataframe(
            df, 
            use_container_width=True, 
            hide_index=True)
        st.caption(f"Total de {len(aulas_instrutor)} aula(s) agendada(s).")