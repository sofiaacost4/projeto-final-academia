# Página em que o gestor visualiza o histórico dos pagamentos confirmados.
import streamlit as st
import pandas as pd
from view import View

class VerPagamentoUI:
    @staticmethod
    def main():
        st.header("Ver Pagamentos")
        st.write("Histórico geral de pagamentos efetuados pelos alunos da academia GymTime.")
        pagamentos = View.pagamento_listar()
        if not pagamentos:
            st.info("Nenhum pagamento registrado no sistema até o momento.")
            return
        inscricoes = View.inscricao_listar()
        alunos = View.aluno_listar()
        esportes = View.esporte_listar()
        mapa_alunos = {a.get_id(): a.get_nome() for a in alunos}
        mapa_esportes = {e.get_id(): e.get_tipo() for e in esportes}
        mapa_inscricoes = {
            i.get_id(): (mapa_alunos.get(i.get_id_aluno(), "Desconhecido"), 
                         mapa_esportes.get(i.get_id_esporte(), "Desconhecido"))
            for i in inscricoes}
        dados_relatorio = []
        total_arrecadado = 0
        for p in pagamentos:
            info_inscricao = mapa_inscricoes.get(p.get_id_inscricao(), ("N/A", "N/A"))
            nome_aluno, nome_esporte = info_inscricao
            valor = p.get_valor()
            total_arrecadado += valor
            dados_relatorio.append({
                "ID Pagamento": p.get_id(),
                "Inscrição Ref.": p.get_id_inscricao(),
                "Aluno": nome_aluno,
                "Esporte": nome_esporte,
                "Valor": f"R$ {valor:.2f}",
                "Status": p.get_status()})
        col1, col2 = st.columns(2)
        col1.metric("Total de Pagamentos", len(pagamentos))
        col2.metric("Lucro:", f"R$ {total_arrecadado:.2f}")
        df = pd.DataFrame(dados_relatorio)
        st.dataframe(df, use_container_width=True, hide_index=True)