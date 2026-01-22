import streamlit as st
import pandas as pd 
from view import View
import time

class ManterInstrutorUI:

    def main():
        st.header("Cadastro de Instrutores")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["Listar", "Inserir", "Atualizar", "Excluir"]
        )
        with tab1: ManterInstrutorUI.listar()
        with tab2: ManterInstrutorUI.inserir()
        with tab3: ManterInstrutorUI.atualizar()
        with tab4: ManterInstrutorUI.excluir()

    def listar():
        instrutores = View.instrutor_listar_obj()
        if len(instrutores) == 0:
            st.write("Nenhum instrutor cadastrado.")
        else:
            esportes = View.esporte_listar()
            mapa_esportes = {int(e.get_id()): e.get_tipo() for e in esportes}
            list_dic = []
            for obj in instrutores:
                esp_id = int(obj.get_especialidade())
                dic = obj.to_dic()
                dic["especialidade"] = (
                    mapa_esportes[esp_id]
                    if esp_id in mapa_esportes
                    else f"Especialidade inexistente (id={esp_id})")
                list_dic.append(dic)
            df = pd.DataFrame(list_dic)
            st.dataframe(
                df,
                hide_index=True,
                column_order=["id", "nome", "email", "especialidade", "fone"])

    def inserir():
        especialidades = View.esporte_listar()

        nome = st.text_input("Informe o nome:", key="inst_nome")
        email = st.text_input("Informe o e-mail:", key="inst_email")

        esporte_selecionado = st.selectbox(
            "Informe a especialidade:",
            especialidades,
            format_func=lambda e: e.get_tipo(),
            key="inst_esporte_inserir"
        )

        fone = st.text_input("Informe o telefone:", key="inst_fone")
        senha = st.text_input("Informe a senha:", type="password", key="inst_senha")

        if st.button("Inserir", key="btn_inserir_instrutor"):
            try:
                View.instrutor_inserir(
                    nome,
                    email,
                    esporte_selecionado.get_id(),
                    fone,
                    senha
                )
                st.success("Instrutor inserido com sucesso.")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)

    def atualizar():
        instrutores = View.instrutor_listar_obj()
        if len(instrutores) == 0:
            st.write("Nenhum instrutor cadastrado.")
        else:
            especialidades = View.esporte_listar()

            op = st.selectbox(
                "Selecione o instrutor:",
                instrutores,
                format_func=lambda i: f"{i.get_nome()} ({i.get_email()})",
                key="inst_atualizar_select"
            )

            nome = st.text_input("Novo nome:", op.get_nome(), key="inst_nome_att")
            email = st.text_input("Novo e-mail:", op.get_email(), key="inst_email_att")

            esporte_sel = st.selectbox(
                "Nova especialidade:",
                especialidades,
                index=next(
                    (i for i, e in enumerate(especialidades)
                     if e.get_id() == op.get_especialidade()),
                    0
                ),
                format_func=lambda e: e.get_tipo(),
                key="inst_esporte_atualizar"
            )

            fone = st.text_input("Novo telefone:", op.get_fone(), key="inst_fone_att")
            senha = st.text_input(
                "Nova senha:",
                op.get_senha(),
                type="password",
                key="inst_senha_att"
            )

            if st.button("Atualizar", key="btn_atualizar_instrutor"):
                try:
                    View.instrutor_atualizar(
                        op.get_id(),
                        nome,
                        email,
                        esporte_sel.get_id(),
                        fone,
                        senha
                    )
                    st.success("Instrutor atualizado com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)

    def excluir():
        instrutores = View.instrutor_listar_obj()
        if len(instrutores) == 0:
            st.write("Nenhum instrutor cadastrado.")
        else:
            op = st.selectbox(
                "Selecione o instrutor:",
                instrutores,
                format_func=lambda i: f"{i.get_nome()} - {i.get_email()}",
                key="instrutor_excluir"
            )

            if st.button("Excluir", key="btn_excluir_instrutor"):
                try:
                    View.instrutor_excluir(op.get_id())
                    st.success("Instrutor excluído com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
