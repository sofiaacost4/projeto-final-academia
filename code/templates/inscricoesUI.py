# página de Inscrições (Perfil do Aluno) onde aparecerão as Inscrições (Esporte, Instrutor, botão Inscrever-se) para que ele possa se inscrever;
    # ao inscrever-se, aquela aula automaticamente "some" da página e aparece na página Minhas Aulas
import streamlit as st
from view import View


class InscricoesAlunoUI:
    def main():
        st.header("Inscrições")

        id_aluno = st.session_state["usuario_id"]
        aulas = View.aula_listar()
        inscricoes = View.inscricao_listar()

        # esportes já inscritos pelo aluno
        esportes_inscritos = {
            i.get_id_esporte()
            for i in inscricoes
            if i.get_id_aluno() == id_aluno
        }

        # só aulas disponíveis
        aulas_disponiveis = [
            a for a in aulas
            if a.get_id_esporte() not in esportes_inscritos
        ]

        if len(aulas_disponiveis) == 0:
            st.info("Você já está inscrito em todas as aulas disponíveis.")
            return

        for aula in aulas_disponiveis:
            InscricoesAlunoUI.card_aula(id_aluno, aula)

    def card_aula(id_aluno, aula):
        esporte = View.esporte_listar_id(aula.get_id_esporte())
        instrutor = View.instrutor_listar_id(aula.get_id_instrutor())

        with st.container(border=True):
            st.subheader(esporte.get_tipo())
            st.write(f"Instrutor: {instrutor.get_nome()}")
            st.write(f"Dia: {aula.get_dia()}")

            if st.button(
                "Inscrever-se",
                key=f"inscrever_{aula.get_id()}"
            ):
                try:
                    View.inscricao_inserir(
                        id_aluno,
                        aula.get_id_esporte(),
                        "Pendente"
                    )
                    st.success("Inscrição realizada com sucesso!")
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))      
