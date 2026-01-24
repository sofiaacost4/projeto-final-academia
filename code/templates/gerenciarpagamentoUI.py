# página de Pagamentos (Perfil Aluno) onde aparece as inscrições pendentes (que devem ser PAGAS) daquele aluno
import streamlit as st
from view import View
import time

class GerenciarPagamentoUI:
    def main():
        st.header("Minhas Inscrições Pendentes")

        # aluno logado
        aluno = st.session_state.get("aluno")

        if aluno is None:
            st.error("Aluno não autenticado.")
            return

        # filtra inscrições pendentes do aluno
        inscricoes = [
            i for i in View.inscricao_listar()
            if i.get_id_aluno() == aluno.get_id()
            and i.get_status() == "Pendente"
        ]

        if len(inscricoes) == 0:
            st.success("Você não possui inscrições pendentes 🎉")
            return

        for ins in inscricoes:
            with st.container(border=True):
                st.write(f"**Inscrição:** {ins.get_id()}")
                st.write(f"**Status:** {ins.get_status()}")

                if st.button(f"Pagar inscrição {ins.get_id()}"):
                    try:
                        View.pagamento_inserir(
                            status="Pago",
                            valor=100.0,  # valor fixo ou da inscrição
                            id_inscricao=ins.get_id()
                        )

                        View.inscricao_confirmar(ins.get_id())

                        st.success("Pagamento realizado com sucesso!")
                        time.sleep(1)
                        st.rerun()

                    except Exception as erro:
                        st.error(str(erro))
