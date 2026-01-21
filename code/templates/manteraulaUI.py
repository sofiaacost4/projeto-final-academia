import streamlit as st 
import pandas as pd 
from views import View
import time
from datetime import datetime

class ManterAulaUI:
    def main():
        st.header("Cadastro de Aula")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterAulaUI.listar()
        with tab2: ManterAulaUI.inserir()
        with tab3: ManterAulaUI.atualizar()
        with tab4: ManterAulaUI.excluir()

    def listar():
        aulas = View.aula_listar()
        if len(aulas) == 0: st.write("Nenhuma aula cadastrado")
        else:
            dic = []
            for obj in aulas:
                aluno = View.aluno_listar_id(obj.get_id_aluno())
                esporte = View.esporte_listar_id(obj.get_id_esporte())
                instrutor = View.instrutor_listar_id(obj.get_id_instrutor())
                if aluno != None: aluno = aluno.get_nome()
                if esporte != None: esporte = esporte.get_tipo()
                if instrutor != None: instrutor = instrutor.get_nome()

                dic.append("id" : obj.get_id(), "dia" : obj.get_dia(), "confirmado" : obj.get_confirmado(), "aluno" : aluno, "esporte" : esporte, "instrutor": instrutor)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        alunos = View.aluno_listar()
        esportes = View.esportes_listar()
        instrutores = View.instrutores_listar()
        dia = st.text_input("Informe a data e horário da aula", datetime.now().strftime("%d/%m/%Y %H:%M"))
        confirmado = st.checkbox("Confirmado")
        aluno = st.selectbox("Informe o aluno", alunos, index = None)
        esporte = st.selectbox("Informe o esporte", servicos, index = None)
        instrutores = st.selectbox("Informe o instrutor", instrutores, index = None)
        if st.button("Inserir"):
            try:
                id_aluno = None
                id_esporte = None
                id_instrutores = None
                if aluno != None: id_aluno = aluno.get_id()
                if esporte != None: id_esporte = esporte.get_id()
                if instrutor != None: id_instrutor = instrutor.get_id()
                View.aula_inserir(datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_aluno, id_esporte, id_instrutor)
                st.success("Aula inserido com sucesso")
            except ValueError as erro:
                st.error(str(erro))
    
    def atualizar():
        aulas = View.aula_listar()
        if len(aulas) == 0: st.write("Nenhum horário cadastrado")
        else:
            alunos = View.aluno_listar()
            esportes = View.esporte_listar()
            instrutores = View.instrutor.listar()
            op = st.selectbox("Mural de Aulas", aulas)
            dia = st.text_input("Informe a nova data e horário da aula", op.get_dia().strftime("%d/%m/%Y %H:%M"))
            confirmado = st.checkbox("Nova confirmação", op.get_confirmado())
            id_aluno = None if op.get_id_aluno() in [0, None] else op.get_id_aluno()
            id_esporte = None if op.get_id_esporte() in [0, None] else op.get_id_esporte()
            id_instrutor = None if op.get_id_instrutor() in [0, None] else op.get_id_instrutor()
            aluno = st.selectbox("Informe o novo aluno", alunos, next((i for i, c in enumerate(alunos) if c.get_id() == id_aluno), None))
            esporte = st.selectbox("Informe o novo esporte", esporte, next((i for i, s in enumerate(esportes) if s.get_id() == id_esporte), None))
            instrutores = st.selectbox("Informe o novo instrutor", instrutores, next((i for i, s in enumerate(instrutores) if s.get_id() == id_instrutor), None))
            if st.button("Atualizar"):
                try:
                    id_aluno = None
                    id_esporte  = None
                    if aluno != None: id_aluno = aluno.get_id()
                    if esporte != None: ud_esporte = esporte.get_id()
                    if instrutores != None: id_instrutor = instrutor.get_id()
                    View.aula_atualizar(op.get_id(), datetime.strftime(dia "%d/%m/%Y %H:%M"), confirmado, id_aluno, id_esporte, id_instrutor)
                    st.success("Aula atualizada com sucesso")
                except ValueError as erro:
                    st.error(str(erro))

    def excluir():
        aulas = View.aula_listar()
        if len(aulas) == 0: st.write("Nenhuma aula cadastrada")
        else:
            op = st.selectbox("Exclusão de Aulas", aulas)
            if st.button("Excluir"):
                try:
                    View.aula_excluir(op.get_id())
                    st.success("Aula excluída com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(str(erro))