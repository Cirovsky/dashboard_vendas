import streamlit as st
import plotly.express as px
import pandas as pd
from dataset import df
from utils import format_number
from dataset import df_rec_estado,df_rec_mensal,df_rec_categoria,df_vendedores
from graphs import (cria_grafico_mapa,
                    cria_grafico_linha,
                    criar_grafico_pizza,
                    criar_grafico_barra
                    )

st.set_page_config(layout="wide")
st.title("Dashboard de Vendas &#128722;")
aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita','Vendedores'])

sidebar = st.sidebar.title('Filtros')
estados:list[str] = sidebar.multiselect(label='Local da compra', options=df_rec_estado["Local da compra"].to_list())

if len(estados) > 0:
    df_rec_estado = df_rec_estado[df_rec_estado["Local da compra"].isin(estados)]


with aba1:
    st.dataframe(df)

#inserindo métricas
with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric(label="Receita Total",value=format_number(df["Preço"].sum(),"R$"))
        st.plotly_chart(cria_grafico_mapa(
            df=df_rec_estado,
            title="receitas por estado",
            lat='lat',
            lon = 'lon',
            size="Preço",
            scope='south america',
            template='seaborn',
            hover_name='Local da compra',
            hover_data={'lat':False, 'lon':False}
            ))
        st.plotly_chart(criar_grafico_barra(
            df=df_rec_estado,
            title="receitas por estado",
            x='Local da compra',
            y ='Preço'
            ),
            use_container_width=True)
    with coluna2:
        st.metric(label="Total de Vendas",value=format_number(df.shape[0]))
        st.plotly_chart(cria_grafico_linha(
            df=df_rec_mensal,
            title="Histórico de vendas por mês",
            x='Mês',
            y='Preço',
            color='Ano',
            ), use_container_width=True)
        st.plotly_chart(criar_grafico_pizza(
            df = df_rec_categoria,
            title="Porcentagem de receita por categoria de produto vendido.",
            names='Categoria do Produto',
            values='Preço'
        ), use_container_width=True)
with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart( criar_grafico_barra(
            df=df_vendedores,
            title="receita por vendedores",
            x='receita',
            range_x=(300000,500000),
            y='Vendedor',
            sort='receita',
            ), use_container_width=True)
        st.plotly_chart( criar_grafico_barra(
            df=df_vendedores,
            title="avaliação dos vendedores",
            x='avaliação',
            range_x=(4,4.2),
            y='Vendedor',
            sort='avaliação',
            ), use_container_width=True)
    with coluna2:
        st.plotly_chart( criar_grafico_barra(
            df=df_vendedores,
            title="vendas por vendedores",
            x='vendas',
            range_x=(400,800),
            y='Vendedor',
            sort='vendas',
            text_auto=True,
            ), use_container_width=True)
'''
        st.plotly_chart(grafico_venda_vendedores, use_container_width=True)

'''
