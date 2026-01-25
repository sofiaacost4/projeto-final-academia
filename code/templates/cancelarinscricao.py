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
            if i.get_id_aluno() == id_aluno_logado and 
            i.get_status().lower() not in ["pago", "confirmado"]]
        if not inscricoes:
            st.info("Você não possui inscrições pendentes para cancelar.")
            st.caption("Inscrições confirmadas não podem ser canceladas por aqui.")
            return
        dados = []
        for i in inscricoes:
            esporte = View.esporte_listar_id(i.get_id_esporte())
            dados.append({
                "id": i.get_id(),
                "Esporte": esporte.get_tipo() if esporte else "Desconhecido",
                "Status Atual": i.get_status()
            })

        df = pd.DataFrame(dados)
        st.dataframe(
            df[["Esporte", "Status Atual"]],
            use_container_width=True,
            hide_index=True)
        inscricao_escolhida = st.selectbox(
            "Selecione o esporte para desistir da inscrição",
            df["Esporte"].tolist())
        id_cancelar = df[df["Esporte"] == inscricao_escolhida]["id"].iloc[0]

        st.warning("Ao cancelar, sua solicitação será removida e o esporte no qual a inscrição está vinculada voltará para a lista inscrições.")

        if st.button("Confirmar Cancelamento", type="primary"):
            try:
                View.inscricao_excluir(id_cancelar)
                st.success(f"Inscrição em {inscricao_escolhida} cancelada com sucesso!")
                time.sleep(1)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))