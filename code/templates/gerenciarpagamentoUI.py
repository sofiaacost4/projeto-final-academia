import streamlit as st
from view import View
import time

class GerenciarPagamentoUI:
    @staticmethod
    def main():
        st.header("Minhas Inscrições Pendentes")
        id_aluno = st.session_state.get("usuario_id")
        if id_aluno is None:
            st.error("Por favor, realize o login para acessar seus pagamentos.")
            return
        inscricoes = [
            i for i in View.inscricao_listar()
            if i.get_id_aluno() == id_aluno and i.get_status() == "Pendente"
        ]
        if not inscricoes:
            st.info("Você não possui inscrições pendentes.")
            return
        for ins in inscricoes:
            esporte = View.esporte_listar_id(ins.get_id_esporte())
            valor = esporte.get_valor()
            with st.container(border=True):
                col_info, col_btn = st.columns([3, 1])
                with col_info:
                    st.markdown(f"### {esporte.get_tipo()}")
                    st.write(f"**ID da Inscrição:** {ins.get_id()}")
                    st.write(f"**Valor a pagar:** :green[R$ {valor:.2f}]")
                with col_btn:
                    st.write("")
                    if st.button(f"Confirmar Pagamento", key=f"pagar_{ins.get_id()}", use_container_width=True):
                        try:
                            View.pagamento_confirmar_fluxo(ins.get_id(), valor)
                            st.balloons()
                            st.success(f"Pagamento de {esporte.get_tipo()} confirmado!")
                            time.sleep(1.5)
                            st.rerun()
                        except Exception as erro:
                            st.error(f"Erro ao processar pagamento: {erro}")