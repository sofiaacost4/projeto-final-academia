import streamlit as st
import pandas as pd
from view import View
import time

class CancelarInscricaoUI:
    def main():
        st.header("Minhas inscrições")

        id_aluno_logado = st.session_state.get("usuario_id")

        inscricoes = [
            i for i in View.inscricao_listar()
            if i.get_id_aluno() == id_aluno_logado
        ]

        if not inscricoes:
            st.write("Você não possui inscrições para cancelar.")
            return

        dados = []
        for i in inscricoes:
            esporte = View.esporte_listar_id(i.get_id_esporte())
            dados.append({
                "id": i.get_id(),
                "esporte": esporte.get_tipo() if esporte else "Desconhecido"
            })

        df = pd.DataFrame(dados)

        df["Display"] = df["esporte"]

        st.dataframe(
            df[["esporte"]],
            use_container_width=True,
            hide_index=True
        )

        inscricao_escolhida = st.selectbox(
            "Selecione a inscrição para cancelar",
            df["Display"].tolist()
        )

        id_cancelar = df[df["Display"] == inscricao_escolhida]["id"].iloc[0]

        st.warning("Esta ação não pode ser desfeita.")

        if st.button("Cancelar inscrição", type="primary"):
            try:
                View.inscricao_excluir(id_cancelar)
                st.success("Inscrição cancelada com sucesso.")
                time.sleep(1.5)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))
