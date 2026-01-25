import streamlit as st
from view import View

class InscricoesAlunoUI:
    def main():
        st.header("Inscrições")
        id_aluno = st.session_state["usuario_id"]
        esportes_disponiveis = View.esportes_disponiveis_para_aluno(id_aluno)
        if not esportes_disponiveis:
            st.info("Você já está inscrito em todos os esportes disponíveis.")
            return
        for esporte in esportes_disponiveis:
            InscricoesAlunoUI.card_esporte(id_aluno, esporte)
    def card_esporte(id_aluno, esporte):
        # Instrutores associados
        instrutores = [
            i.get_nome()
            for i in View.instrutor_listar_obj()
            if i.get_especialidade() == esporte.get_id()]
        with st.container(border=True):
            st.subheader(f"Esporte: {esporte.get_tipo()}")
            
            st.markdown("**Instrutor(es):**")
            if instrutores:
                for nome in instrutores:
                    st.write(f"- {nome}")
            else:
                st.write("Nenhum instrutor associado.")

            if st.button(
                "Inscrever-se",
                key=f"inscrever_{esporte.get_id()}"
            ):
                try:
                    View.inscricao_inserir(
                        id_aluno,
                        esporte.get_id(),
                        "Pendente"
                    )
                    st.success("Inscrição realizada com sucesso!")
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))
