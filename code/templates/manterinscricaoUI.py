import streamlit as st
import pandas as pd 
from view import View
import time

class ManterInscricaoUI:
    def main():
        st.header("Cadastro de inscrições")
        tab1, tab2, tab3, tb4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterInscricaoUI.listar()
        with tab2: ManterInscricaoUI.inserir()
        with tab3: ManterInscricaoUI.atualizar()
        with tab4: ManterInscricaoUI.excluir()
    
    def listar():
        inscricoes = View.inscricao_listar()
        if len(inscricoes) == 0: st.write("Não há nenhuma inscrição cadastrada ainda.")
        else:
            list_dic []
            for obj in inscricoes: list_dic.append(obj.to_dic())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, colunm_order=["id", "status", "data"])
    
    def inserir():
        status = st.selectbox(
            "Selecione o status da inscrição:",
            ["Pendente", "Confirmada", "Cancelada"]
        )
        if st.button("Inserir"):
            try:
                View.inscricao_inserir(status)
                st.sucess("Inscrição inserida com sucesso!")
            except Exception as erro:
                st.error(str(error))
    
    def atualizar():
        inscricoes 