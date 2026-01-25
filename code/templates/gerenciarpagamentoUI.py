import streamlit as st
from view import View
import time

class GerenciarPagamentoUI:
    def main():
        st.header("Minhas Inscrições Pendentes")
        id_aluno = st.session_state.get("usuario_id")
        if id_aluno is None:
            st.error("Aluno não autenticado.")
            return
        inscricoes = [
            i for i in View.inscricao_listar()
            if i.get_id_aluno() == id_aluno
            and i.get_status() == "Pendente"]
        if not inscricoes:
            st.success("Você não possui inscrições pendentes! °˖✧◝(⁰▿⁰)◜✧˖°")
            return

        for ins in inscricoes:
            with st.container(border=True):
                esporte = View.esporte_listar_id(ins.get_id_esporte())
                st.write(f"**Inscrição** ")
                st.write(f"**Esporte:** {esporte.get_tipo()}")
                st.write(f"**Status:** {ins.get_status()}")
                valor = esporte.get_valor()
                st.write(f"**Valor:** R$ {valor:.2f}")
                if st.button(
                    f"Confirmar pagamento da inscrição {ins.get_id()}",
                    key=f"pagar_{ins.get_id()}"):
                    try:
                        View.pagamento_inserir(
                            status="Pago",
                            valor=valor,
                            id_inscricao=ins.get_id())
                        View.inscricao_confirmar(ins.get_id())
                        st.success("Pagamento confirmado com sucesso!")
                        time.sleep(1)
                        st.rerun()
                    except ValueError as erro:
                        st.error(str(erro))
