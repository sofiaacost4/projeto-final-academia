import streamlit as st
import pandas as pd 
from view import View
import time

class ManterEsporteUI:
    def main():
        st.header("Cadastro de Esportes")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["Listar", "Inserir", "Atualizar", "Excluir"]
        )
        with tab1: ManterEsporteUI.listar()
        with tab2: ManterEsporteUI.inserir()
        with tab3: ManterEsporteUI.atualizar()
        with tab4: ManterEsporteUI.excluir()

    def listar():
        esportes = View.esporte_listar()
        if len(esportes) == 0:
            st.write("Nenhum esporte cadastrado.")
        else:
            list_dic = [obj.to_dic() for obj in esportes]
            df = pd.DataFrame(list_dic)
            st.dataframe(
                df,
                hide_index=True,
                column_order=["id", "tipo", "valor"]
            )

    def inserir():
        tipo = st.text_input("Informe o esporte:")
        valor = st.number_input(
            "Informe o valor (R$):",
            min_value=0.0,
            step=1.0,
            format="%.2f"
        )

        if st.button("Inserir"):
            try:
                View.esporte_inserir(tipo, valor)
                st.success("Esporte inserido com sucesso.")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)

    def atualizar():
        esportes = View.esporte_listar()
        if len(esportes) == 0:
            st.write("Nenhum esporte cadastrado.")
        else:
            op = st.selectbox("Atualização de esportes", esportes)

            tipo = st.text_input(
                "Informe o novo tipo do esporte:",
                op.get_tipo()
            )

            valor = st.number_input(
                "Informe o novo valor (R$):",
                min_value=0.0,
                value=op.get_valor(),
                step=1.0,
                format="%.2f"
            )

            if st.button("Atualizar"):
                View.esporte_atualizar(
                    op.get_id(),
                    tipo,
                    valor
                )
                st.success("Esporte atualizado com sucesso.")
                time.sleep(2)
                st.rerun()

    def excluir():
        esportes = View.esporte_listar()
        if len(esportes) == 0:
            st.write("Nenhum esporte cadastrado.")
        else: 
            op = st.selectbox("Exclusão de Esportes", esportes)
            if st.button("Excluir"):
                try:
                    View.esporte_excluir(op.get_id())
                    st.success("Esporte excluído com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
