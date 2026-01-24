import streamlit as st
import pandas as pd
from view import View
import time

class ManterInscricaoUI:

    def main():
        st.header("Cadastro de Inscrições")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterInscricaoUI.listar()
        with tab2: ManterInscricaoUI.inserir()
        with tab3: ManterInscricaoUI.excluir()

    def listar():
        inscricoes = View.inscricao_listar()
        if len(inscricoes) == 0:
            st.write("Não há nenhuma inscrição cadastrada ainda.")
        else:
            alunos = View.aluno_listar()

            mapa_alunos = {a.get_id(): a.get_nome() for a in alunos}
            # para aparecer o nome do aluno no listar
            dados = []
            for i in inscricoes:
                dados.append({
                    "id": i.get_id(),
                    "aluno": mapa_alunos.get(i.get_id_aluno()),
                    "esporte": i.get_id_esporte(),
                    "status": i.get_status()
                })
            df = pd.DataFrame(dados)
            st.dataframe(df)

    def inserir():
        alunos = View.aluno_listar()
        esportes = View.esporte_listar()

        aluno = st.selectbox("Aluno", alunos, key="inscricao_aluno")
        esporte = st.selectbox("Esporte", esportes, key='inscricao_esporte')

        if st.button("Inscrever"):
            try:
                View.inscricao_inserir(
                    aluno.get_id(),
                    esporte.get_id(),
                    "Pendente"
                )
                st.success("Inscrição realizada! Aguardando pagamento.")
            except ValueError as e:
                st.error(str(e))

    def excluir():
        inscricoes = View.inscricao_listar()
        if len(inscricoes) == 0:
            st.write("Nenhuma inscrição cadastrada.")
        else:
            op = st.selectbox("Selecione a inscrição", 
                              inscricoes,
                              key="inscricao_excluir")
            if st.button("Excluir"):
                try:
                    View.inscricao_excluir(op.get_id())
                    st.success("Inscrição excluída.")
                    time.sleep(1)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))
