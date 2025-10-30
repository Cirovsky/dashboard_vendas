import plotly.express as px
from dataset import df_rec_estado,df_rec_mensal
grafico_map_estado = px.scatter_geo(
    data_frame=df_rec_estado,
    lat= 'lat',
    lon= 'lon',
    scope='south america',
    size= 'Preço',
    template='seaborn',
    hover_name='Local da compra',
    hover_data={'lat': False, 'lon': False},
    title='receita por estado',
)

grafico_vendas_mes = px.area(
    data_frame=df_rec_mensal,
    x= 'Data da Compra',
    y= 'Preço',
    labels='mês/ano',
    title='Histórico de receita de vendas por mês'
)