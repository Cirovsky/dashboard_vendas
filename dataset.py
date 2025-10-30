import json
import pandas as pd

file = open('dados/vendas.json')
data = json.load(file)
df:pd.DataFrame = pd.DataFrame.from_dict(data)
df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')
file.close()

df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()
df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']].merge(df_rec_estado, left_on='Local da compra', right_index=True)
df_rec_estado.sort_values(by='Preço',ascending=False,inplace=True)
