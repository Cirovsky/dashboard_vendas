import streamlit as st
import plotly.express as px
import pandas as pd
from dataset import df
from utils import format_number
from graphs import (grafico_map_estado, 
                    grafico_receita_mensal,
                    grafico_bar_rec_estado,
                    grafico_rec_categoria,
                    grafico_rec_vendedores, 
                    grafico_venda_vendedores,
                    grafico_avaliacao_vendedores
                    )

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
        st.plotly_chart(grafico_bar_rec_estado,use_container_width=True)
    with coluna2:
        st.metric(label="Total de Vendas",value=format_number(df.shape[0]))
        st.plotly_chart(grafico_receita_mensal, use_container_width=True)
        st.plotly_chart(grafico_rec_categoria, use_container_width=True)
with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(grafico_rec_vendedores, use_container_width=True)
        st.plotly_chart(grafico_avaliacao_vendedores, use_container_width=True)
    with coluna2:
        st.plotly_chart(grafico_venda_vendedores, use_container_width=True)

