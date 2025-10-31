import plotly.express as px
from dataset import df_rec_estado,df_rec_mensal,df_rec_categoria,df_vendedores

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
    title='Histórico de receita de vendas por mês',
)

grafico_receita_mensal.update_layout(yaxis_title = 'Receita')

grafico_bar_rec_estado= px.bar(
    data_frame=df_rec_estado.head(7),
    x='Local da compra',
    y = 'Preço',
    title='Receita por estado'
)

grafico_bar_rec_estado.update_layout(yaxis_title = "Receita")

grafico_rec_categoria = px.pie(
    data_frame=df_rec_categoria,
    names='Categoria do Produto',
    values="Preço",
    title='Parcela de Receitas por categoria'
)
df_vendedores.sort_values(by="receita", ascending=False, inplace=True)
grafico_rec_vendedores = px.bar(
    data_frame=df_vendedores.head(7),
    x= 'vendas',
    y= 'Vendedor',
    title='Receita por vendedor'
)
df_vendedores.sort_values(by="vendas", ascending=False, inplace=True)
grafico_venda_vendedores = px.bar(
    data_frame=df_vendedores.head(7),
    x= 'vendas',
    y= 'Vendedor',
    text_auto=True,
    title='Vendas por vendedor'
)
df_vendedores.sort_values(by="avaliação", ascending=False, inplace=True)

grafico_avaliacao_vendedores = px.bar(
    data_frame=df_vendedores.head(7),
    x= 'avaliação',
    y= 'Vendedor',
    text_auto=True,
    title='Avaliação por vendedor'
)