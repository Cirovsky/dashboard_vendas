import plotly.express as px
import pandas as pd


def cria_grafico_mapa(df:pd.DataFrame,title: str, lat:str, lon:str,size:str,hover_name:str, hover_data:dict, scope:str = 'world', template:str = 'seaborn', sort:str|None = None):
    '''Cria gráfico estilo mapa (scatter_geo) a partir dos parametros enviados'''
    if sort is not None:
        df.sort_values(by=sort, ascending=False, inplace=True)

    grafico_map_estado = px.scatter_geo(
        data_frame=df,
        title=title,
        lat= lat,
        lon= lon,
        scope=scope,
        size= size,
        template=template,
        hover_name=hover_name,
        hover_data=hover_data,
    )
    return grafico_map_estado

def cria_grafico_linha(df:pd.DataFrame,title:str, x:str, y:str, color:str, markers:bool = True):
    '''Cria gráfico de linha a partir dos parametros enviados'''
    grafico_linha = px.line(
        data_frame=df,
        title=title,
        x= x,
        y= y,
        markers=markers,
        range_y=(0, df.max()),
        color= color,
    )

    grafico_linha.update_layout(yaxis_title = 'Receita')

    return grafico_linha

def criar_grafico_barra(df:pd.DataFrame
                      ,x:str, 
                      y:str, 
                      title:str,
                      y_title:str|None = None, 
                      sort:str|None = None, 
                      length_values:int = 7, 
                      text_auto:bool = False,
                      range_x:tuple = None,
                      range_y:tuple = None
                      ):
    '''Cria gráfico de barras a partir dos parametros enviados'''
    if sort != None:
        df.sort_values(by=sort, ascending=False, inplace=True)
    grafico_barra= px.bar(
        data_frame=df.head(length_values),
        title=title,
        x = x,
        y = y,
        text_auto=text_auto
    )
    if y_title != None:
        grafico_barra.update_layout(yaxis_title = y_title)
    if range_x != None:
        grafico_barra.update_xaxes({"range":range_x})
    if range_y != None:
        grafico_barra.update_yaxes({"range":range_y})

    return grafico_barra

def criar_grafico_pizza(df:pd.DataFrame,title:str, names:str, values:str):
    grafico_pizza = px.pie(
        data_frame=df,
        title=title,
        names=names,
        values=values
    )
    return grafico_pizza