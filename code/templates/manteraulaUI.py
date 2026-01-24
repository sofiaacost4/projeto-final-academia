import streamlit as st
import pandas as pd
from view import View
import time
from datetime import datetime


class ManterAulaUI:

    def main():
        st.header("Cadastro de Aulas")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["Listar", "Inserir", "Atualizar", "Excluir"]
        )
        with tab1: ManterAulaUI.listar()
        with tab2: ManterAulaUI.inserir()
        with tab3: ManterAulaUI.atualizar()
        with tab4: ManterAulaUI.excluir()

    # ---------------- LISTAR ----------------

    def listar():
        aulas = View.aula_listar()
        if len(aulas) == 0:
            st.write("Nenhuma aula cadastrada.")
        else:
            alunos = View.aluno_listar()
            esportes = View.esporte_listar()
            instrutores = View.instrutor_listar_obj()

            mapa_alunos = {a.get_id(): a.get_nome() for a in alunos}
            mapa_esportes = {e.get_id(): e.get_tipo() for e in esportes}
            mapa_instrutores = {i.get_id(): i.get_nome() for i in instrutores}

            lista = []
            for a in aulas:
                dia = a.get_dia()
                if isinstance(dia, datetime):
                    dia = dia.strftime("%d/%m/%Y %H:%M")
                lista.append({
                    "id": a.get_id(),
                    "dia": dia,
                    "confirmado": a.get_confirmado(),
                    "aluno": mapa_alunos.get(a.get_id_aluno()),
                    "esporte": mapa_esportes.get(a.get_id_esporte()),
                    "instrutor": mapa_instrutores.get(a.get_id_instrutor())
                })

            df = pd.DataFrame(lista)
            st.dataframe(df, hide_index=True)

    # ---------------- INSERIR ----------------

    def inserir():
        alunos = View.aluno_listar()
        esportes = View.esporte_listar()
        instrutores = View.instrutor_listar_obj()

        dia = st.text_input(
            "Informe a data e horário da aula:",
            datetime.now().strftime("%d/%m/%Y %H:%M"),
            key="aula_dia_inserir"
        )

        confirmado = st.checkbox("Confirmado", key="aula_confirmado_inserir")

        aluno = st.selectbox(
            "Aluno:",
            alunos,
            format_func=lambda a: a.get_nome(),
            index=None,
            key="aula_aluno_inserir"
        )

        esporte = st.selectbox(
            "Esporte:",
            esportes,
            format_func=lambda e: e.get_tipo(),
            index=None,
            key="aula_esporte_inserir"
        )

        instrutor = st.selectbox(
            "Instrutor:",
            instrutores,
            format_func=lambda i: i.get_nome(),
            index=None,
            key="aula_instrutor_inserir"
        )

        if st.button("Inserir", key="btn_inserir_aula"):
            try:
                data = datetime.strptime(dia, "%d/%m/%Y %H:%M")

                View.aula_inserir(
                    aluno.get_id() if aluno else None,
                    esporte.get_id() if esporte else None,
                    data,
                    confirmado,
                    instrutor.get_id() if instrutor else None
                )

                st.success("Aula inserida com sucesso.")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))

    # ---------------- ATUALIZAR ----------------

    def atualizar():
        aulas = View.aula_listar()
        if len(aulas) == 0:
            st.write("Nenhuma aula cadastrada.")
        else:
            alunos = View.aluno_listar()
            esportes = View.esporte_listar()
            instrutores = View.instrutor_listar_obj()

            op = st.selectbox(
                "Selecione a aula:",
                aulas,
                format_func=lambda a: f"{a.get_id()} - {a.get_dia().strftime('%d/%m %H:%M')}",
                key="aula_atualizar_select"
            )

            dia = st.text_input(
                "Nova data e horário:",
                op.get_dia().strftime("%d/%m/%Y %H:%M"),
                key="aula_dia_atualizar"
            )

            confirmado = st.checkbox(
                "Confirmado",
                op.get_confirmado(),
                key="aula_confirmado_atualizar"
            )

            aluno = st.selectbox(
                "Novo aluno:",
                alunos,
                index=next(
                    (i for i, a in enumerate(alunos)
                     if a.get_id() == op.get_id_aluno()),
                    None
                ),
                format_func=lambda a: a.get_nome(),
                key="aula_aluno_atualizar"
            )

            esporte = st.selectbox(
                "Novo esporte:",
                esportes,
                index=next(
                    (i for i, e in enumerate(esportes)
                     if e.get_id() == op.get_id_esporte()),
                    None
                ),
                format_func=lambda e: e.get_tipo(),
                key="aula_esporte_atualizar"
            )

            instrutor = st.selectbox(
                "Novo instrutor:",
                instrutores,
                index=next(
                    (i for i, i2 in enumerate(instrutores)
                     if i2.get_id() == op.get_id_instrutor()),
                    None
                ),
                format_func=lambda i: i.get_nome(),
                key="aula_instrutor_atualizar"
            )

            if st.button("Atualizar", key="btn_atualizar_aula"):
                try:
                    data = datetime.strptime(dia, "%d/%m/%Y %H:%M")

                    View.aula_atualizar(
                        op.get_id(),
                        data,
                        confirmado,
                        aluno.get_id() if aluno else None,
                        esporte.get_id() if esporte else None,
                        instrutor.get_id() if instrutor else None
                    )

                    st.success("Aula atualizada com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(str(erro))

    # ---------------- EXCLUIR ----------------

    def excluir():
        aulas = View.aula_listar()
        if len(aulas) == 0:
            st.write("Nenhuma aula cadastrada.")
        else:
            op = st.selectbox(
                "Selecione a aula:",
                aulas,
                format_func=lambda a: f"{a.get_id()} - {a.get_dia().strftime('%d/%m %H:%M')}",
                key="aula_excluir_select"
            )

            if st.button("Excluir", key="btn_excluir_aula"):
                try:
                    View.aula_excluir(op.get_id())
                    st.success("Aula excluída com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(str(erro))
