import streamlit as st
import pandas as pd
import plotly.express as px

tabela_vendas = pd.read_csv("vendas.csv")

st.write("# SISTEMA DE VENDAS")

st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data", min_value="today")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carlos", "Ricardo", "Maria", "Joana", "João"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Monitor", "Teclado", "Tablet"])
qtde = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor", )
botao_cadastrar = st.sidebar.button("Cadastrar Venda")
if botao_cadastrar:
    if valor <= 0 or qtde <= 0 or produto == "":
        st.warning("Erro no preenchimento!")
    else:
        nova_venda = [str(data), vendedor, produto, qtde, valor]
        ultima_linha = len(tabela_vendas)
        tabela_vendas.loc[ultima_linha] = nova_venda
        tabela_vendas.to_csv("vendas.csv", index=False)
        st.success("Venda Cadastrada")

st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)
st.write('<span style="color:lightblue; font-weight:bold; font-size:42px">Dashboard</span>', unsafe_allow_html=True)
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento:_.2f}".replace(".", ",").replace("_", "."))
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5)
st.plotly_chart(grafico2)
