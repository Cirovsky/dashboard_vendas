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

grafico_receita_mensal = px.line(
    data_frame=df_rec_mensal,
    x= 'Mês',
    y= 'Preço',
    markers=True,
    range_y=(0, df_rec_mensal.max()),
    color= 'Ano',
    line_dash='Ano',
    title='Histórico de receita de vendas por mês'
)