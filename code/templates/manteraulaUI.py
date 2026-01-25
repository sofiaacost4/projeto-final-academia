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
        if not aulas:
            st.info("Nenhuma aula cadastrada.")
            return

        esportes = View.esporte_listar()
        instrutores = View.instrutor_listar_obj()

        mapa_esportes = {e.get_id(): e.get_tipo() for e in esportes}
        mapa_instrutores = {i.get_id(): i.get_nome() for i in instrutores}

        lista = []
        for a in aulas:
            lista.append({
                "ID": a.get_id(),
                "Data": a.get_dia().strftime("%d/%m/%Y %H:%M"),
                "Esporte": mapa_esportes.get(a.get_id_esporte()),
                "Instrutor": mapa_instrutores.get(a.get_id_instrutor())
            })

        df = pd.DataFrame(lista)
        st.dataframe(df, hide_index=True)

    # ---------------- INSERIR ----------------

    def inserir():
        esportes = View.esporte_listar()
        instrutores = View.instrutor_listar_obj()

        dia = st.text_input(
            "Data e horário da aula:",
            datetime.now().strftime("%d/%m/%Y %H:%M")
        )

        esporte = st.selectbox(
            "Esporte:",
            esportes,
            format_func=lambda e: e.get_tipo(),
            index=None
        )

        instrutor = None

        if esporte:
            instrutores = View.instrutores_por_esporte(esporte.get_id())

            if not instrutores:
                st.warning("Nenhum instrutor cadastrado para este esporte.")
                return

            instrutor = st.selectbox(
                "Instrutor:",
                instrutores,
                format_func=lambda i: i.get_nome()
            )
            intervalo_tipo = st.selectbox(
                "Intervalo:",
                ["dias", "semanas", "meses"]
            )

        intervalo_valor = st.number_input(
            "Intervalo (quantidade):",
            min_value=1,
            value=1
        )

        quantidade = st.number_input(
            "Quantidade de aulas:",
            min_value=1,
            value=4
        )
        if st.button("Criar aulas"):
            try:
                if not esporte or not instrutor:
                    raise ValueError("Selecione esporte e instrutor.")
                data_inicio = datetime.strptime(dia, "%d/%m/%Y %H:%M")

                View.aula_criar_com_intervalo(
                    id_esporte=esporte.get_id(),
                    id_instrutor=instrutor.get_id(),
                    data_inicio=data_inicio,
                    intervalo_tipo=intervalo_tipo,
                    intervalo_valor=intervalo_valor,
                    quantidade=quantidade
                )

                st.success(f"{quantidade} aulas criadas com sucesso!")
                time.sleep(1)
                st.rerun()

            except ValueError as erro:
                st.error(str(erro))

    # ---------------- ATUALIZAR ----------------

    def atualizar():
        aulas = View.aula_listar()
        if not aulas:
            st.info("Nenhuma aula cadastrada.")
            return

        esportes = View.esporte_listar()
        instrutores = View.instrutor_listar_obj()

        op = st.selectbox(
            "Selecione a aula:",
            aulas,
            format_func=lambda a: f"{a.get_id()} - {a.get_dia().strftime('%d/%m %H:%M')}",
            key="atualizar_aula_select"
        )

        dia = st.text_input(
            "Nova data:",
            op.get_dia().strftime("%d/%m/%Y %H:%M")
        )

        esporte = st.selectbox(
            "Novo esporte:",
            esportes,
            index=next(i for i, e in enumerate(esportes) if e.get_id() == op.get_id_esporte()),
            format_func=lambda e: e.get_tipo(),
            key="atualizar_esporte_select"
        )

        instrutor = st.selectbox(
            "Novo instrutor:",
            instrutores,
            index=next(i for i, ins in enumerate(instrutores) if ins.get_id() == op.get_id_instrutor()),
            format_func=lambda i: i.get_nome(),
            key="atualizar_instrutor_select"
        )

        if st.button("Atualizar"):
            try:
                data = datetime.strptime(dia, "%d/%m/%Y %H:%M")

                View.aula_atualizar(
                    id=op.get_id(),
                    dia=data,
                    id_esporte=esporte.get_id(),
                    id_instrutor=instrutor.get_id()
                )

                st.success("Aula atualizada.")
                time.sleep(1)
                st.rerun()

            except ValueError as erro:
                st.error(str(erro))

    # ---------------- EXCLUIR ----------------

    def excluir():
        aulas = View.aula_listar()
        if not aulas:
            st.info("Nenhuma aula cadastrada.")
            return

        op = st.selectbox(
            "Selecione a aula:",
            aulas,
            format_func=lambda a: f"{a.get_id()} - {a.get_dia().strftime('%d/%m %H:%M')}"
        )

        if st.button("Excluir"):
            try:
                View.aula_excluir(op.get_id())
                st.success("Aula excluída.")
                time.sleep(1)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))
