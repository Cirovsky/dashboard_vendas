import streamlit as st
import plotly.express as px
import pandas as pd
from dataset import df

st.set_page_config(layout="wide")
st.title("Dashboard de Vendas &#128722;")
aba1, ab2, aba3 = st.tabs(['Dataset', 'Receita','Vendedores'])
with aba1:
    st.dataframe(df)