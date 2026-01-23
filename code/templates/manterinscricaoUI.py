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
        with tab3: ManterInscricaoUI.atualizar()
        with tab4: ManterInscricaoUI.excluir()

    def listar():
        inscricoes = View.inscricao_listar()
        if len(inscricoes) == 0:
            st.write("Não há nenhuma inscrição cadastrada ainda.")
        else:
            dados = []
            for i in inscricoes:
                dados.append({
                    "id": i.get_id(),
                    "aluno": i.get_id_aluno(),
                    "esporte": i.get_id_esporte(),
                    "status": i.get_status()
                })
            df = pd.DataFrame(dados)
            st.dataframe(df)

    def inserir():
        alunos = View.aluno_listar()
        esportes = View.esporte_listar()

        aluno = st.selectbox("Aluno", alunos)
        esporte = st.selectbox("Esporte", esportes)

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

    def atualizar():
        inscricoes = View.inscricao_listar()
        if len(inscricoes) == 0:
            st.write("Nenhuma inscrição cadastrada.")
        else:
            op = st.selectbox("Selecione a inscrição", inscricoes)

            status = st.selectbox(
                "Status",
                ["Pendente", "Confirmada", "Cancelada"],
                index=["Pendente", "Confirmada", "Cancelada"].index(op.get_status())
            )

            if st.button("Atualizar"):
                try:
                    View.inscricao_atualizar(
                        op.get_id(),
                        status
                    )
                    st.success("Inscrição atualizada.")
                except ValueError as e:
                    st.error(str(e))

    def excluir():
        inscricoes = View.inscricao_listar()
        if len(inscricoes) == 0:
            st.write("Nenhuma inscrição cadastrada.")
        else:
            op = st.selectbox("Selecione a inscrição", inscricoes)
            if st.button("Excluir"):
                try:
                    View.inscricao_excluir(op.get_id())
                    st.success("Inscrição excluída.")
                    time.sleep(1)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))
