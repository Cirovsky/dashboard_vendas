import json
import pandas as pd
from datetime import datetime

def define_mes(date)-> str:
    date = str(date)
    date = date.split("-")
    date.pop()
    return "-".join(date + ["01"])

file = open('dados/vendas.json')
data = json.load(file)
df:pd.DataFrame = pd.DataFrame.from_dict(data)
df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')
file.close()

#receita por estado
df_rec_estado:pd.DataFrame = df.groupby('Local da compra')[['Preço']].sum()
df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']].merge(df_rec_estado, left_on='Local da compra', right_index=True)
df_rec_estado.sort_values(by='Preço',ascending=False,inplace=True)

#receita por mês

df_rec_mensal:pd.DataFrame = df.set_index('Data da Compra').groupby(pd.Grouper(freq='ME'))[['Preço']].sum().reset_index()#reset é importante
df_rec_mensal['Ano'] = df_rec_mensal['Data da Compra'].dt.year
df_rec_mensal['Mês'] = df_rec_mensal['Data da Compra'].dt.month_name()

#Receita por categoria

df_rec_categoria:pd.DataFrame = df.groupby('Categoria do Produto')[['Preço']].sum()
df_rec_categoria = df.drop_duplicates(subset='Categoria do Produto')[['Categoria do Produto']].merge(df_rec_categoria, left_on='Categoria do Produto', right_index=True)


df_vendedores:pd.DataFrame = pd.DataFrame(df.groupby('Vendedor')['Preço'].agg(['sum','count'])).reset_index()
df_vendedores.rename(columns={'sum':'receita','count':'vendas'}, inplace=True)
df_vendedores['avaliação'] = df_vendedores['Vendedor'].map(lambda vendedor: df[df['Vendedor']== vendedor]['Avaliação da compra'].mean())
colunas_categorias:list[str] = df_rec_categoria['Categoria do Produto'].to_list()
print(df_vendedores)