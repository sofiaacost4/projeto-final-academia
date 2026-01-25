import streamlit as st
from view import View

class VerTurmasUI:
    def main():
        st.header("Ver Turmas")
        esportes = View.esporte_listar()
        for e in esportes:
            with st.container(border=True):
                st.subheader(f"Esporte: {e.get_tipo()}")
                instrutores = View.instrutores_por_esporte(e.get_id())
                alunos = View.alunos_por_esporte(e.get_id())
                st.markdown("**Instrutor(es):**")
                if instrutores:
                    for i in instrutores:
                        st.write(f"- {i.get_nome()}")
                else:
                    st.write("Nenhum instrutor associado.")
                st.markdown("**Alunos:**")
                if alunos:
                    for a in alunos:
                        st.write(f"- {a.get_nome()}")
                else:
                    st.write("Nenhum aluno inscrito.")
