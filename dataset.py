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
df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()
df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']].merge(df_rec_estado, left_on='Local da compra', right_index=True)
df_rec_estado.sort_values(by='Preço',ascending=False,inplace=True)

#receita por mês

#df["mês"] = df["Data da Compra"].map(lambda date: define_mes(date))
df_rec_mensal:pd.DataFrame = df.set_index('Data da Compra').groupby(pd.Grouper(freq='M'))[['Preço']].sum().reset_index()#reset é importante

df_rec_mensal['Ano'] = df_rec_mensal['Data da Compra'].dt.year
df_rec_mensal['Mês'] = df_rec_mensal['Data da Compra'].dt.month_name()
#df_rec_mes = df.groupby("mês")[['Preço']].sum()
#df_rec_mes = df.drop_duplicates(subset='mês')[["mês"]].merge(df_rec_mes, left_on='mês', right_index=True)
print(df_rec_mensal)