import streamlit as st
from view import View

class VerInscricoesUI:
    def main():
        st.header("Minhas Inscrições")
        id_aluno = st.session_state.get("usuario_id")
        if id_aluno is None:
            st.error("Aluno não autenticado.")
            return
        inscricoes = [
            i for i in View.inscricao_listar()
            if i.get_id_aluno() == id_aluno]
        if not inscricoes:
            st.info("Você ainda não realizou nenhuma inscrição.")
            return
        for ins in inscricoes:
            esporte = View.esporte_listar_id(ins.get_id_esporte())
            with st.container(border=True):
                st.write(f"**Esporte:** {esporte.get_tipo()}")
                st.write(f"**Status:** {ins.get_status()}")
                if ins.get_status() == "Pendente":
                    st.warning("Aguardando pagamento")
                elif ins.get_status() == "Pago":
                    st.success("Inscrição confirmada!")

