import streamlit as st
import plotly.express as px
import pandas as pd
from dataset import df
from utils import format_number
from graphs import grafico_map_estado

st.set_page_config(layout="wide")
st.title("Dashboard de Vendas &#128722;")
aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita','Vendedores'])

with aba1:
    st.dataframe(df)

#inserindo métricas
with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric(label="Receita Total",value=format_number(df["Preço"].sum(),"R$"))
        st.plotly_chart(grafico_map_estado)
    with coluna2:
        st.metric(label="Total de Vendas",value=format_number(df.shape[0]))
        
with aba3:
    st.table(set(df["Vendedor"]))