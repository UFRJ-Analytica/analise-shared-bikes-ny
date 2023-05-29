import os
import pandas as pd
import numpy as np
import math
import datetime
from limpeza_dos_dados import Limpeza
from haversine import haversine
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import logging

# Configurando o logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
log = logger.info

os.chdir("../Scripts")
os.getcwd()


# Função para extrair dados
def extrair_dados() -> object:
    #  Objeto para limpeza dos dados
    limpeza = Limpeza()

    df_clean = (
        pd.read_parquet("../Dados/BikeData-Processed.parquet")
        .pipe(limpeza.valores_vazios)
        .pipe(limpeza.remove_outliers)
        .assign(

            distancia=lambda _df: _df.apply(
                lambda row: haversine(row['estacao_inicio_latitude'], row['estacao_inicio_longitude'],
                                      row['estacao_fim_latitude'], row['estacao_fim_longitude']), axis=1),
            # distancia=df.apply(lambda row: calculate_haversine(row), axis=1),
            dia_inicio=lambda _df: _df['inicio_viagem'].dt.day,
            mes_inicio=lambda _df: _df['inicio_viagem'].dt.month,
            ano_inicio=lambda _df: _df['inicio_viagem'].dt.year,
            dia_fim=lambda _df: _df['fim_viagem'].dt.day,
            mes_fim=lambda _df: _df['fim_viagem'].dt.month,
            ano_fim=lambda _df: _df['fim_viagem'].dt.year,
            hora_inicio=lambda _df: _df['inicio_viagem'].dt.hour,
            minuto_inicio=lambda _df: _df['inicio_viagem'].dt.minute,
            segundo_inicio=lambda _df: _df['inicio_viagem'].dt.second,
            hora_fim=lambda _df: _df['fim_viagem'].dt.hour,
            minuto_fim=lambda _df: _df['fim_viagem'].dt.minute,
            segundo_fim=lambda _df: _df['fim_viagem'].dt.second,
            dia_semana=lambda _df: _df['inicio_viagem'].dt.day_name(),
            idade=lambda _df: _df['ano_inicio'] - _df["ano_nascimento"],
        )
    )
    return df_clean


#=====================================#
#  Tarefas da Segunda semana Gustavo  #
#=====================================#


#=====================================#
#  Análise Exploratória de Dados:     #
#=====================================#
# Para visualizar as primeiras linhas do DataFrame e ter uma ideia dos dados:
# log(df.head)
# Para verificar as informações dos dados:
# log(f'informações dos dados{df.info}')
# log('# Para verificar estatísticas descritivas dos dados:')
# log(df.describe)
# Para verificar a quantidade de valores nulos em cada coluna:
# log(df.isnull().sum)
# Para verificar a quantidade de valores únicos em cada coluna:
# log(df.nunique)
# log('# Para verificar a correlação entre as variáveis:')
# log(df.corr)



# plt.imshow(df.corr(), cmap='coolwarm')
# plt.colorbar()
# plt.xticks(range(len(df.columns)), df.columns, rotation=90)
# plt.yticks(range(len(df.columns)), df.columns)
# plt.show()
#

#=====================================#
#  Análise Estatística                #
#=====================================#



#=====================================#
#  Visualização de Dados              #
#=====================================#


# Comece analisando os dados para compreender o uso e identificar erros.
# Realize todas as análises relevantes.
# Unificar o tratamento de dados
#================================================================
# Qual é a distribuição do uso de bicicletas (pickups)
# durante os dias da semana? Existem dias de pico?
#================================================================
# Qual é a distribuição do uso de bicicletas (pickups)
# durante os horários do dia? Existem horas de pico?
#================================================================
# Essa distribuição se mantém em todos os dias da semana?
# Há diferenças entre dias úteis e finais de semana?

# Não funciona
def distribuicao_uso_bicicletas_dias_semana(df):
    """
    Esta função plota um gráfico de barras para mostrar a distribuição do uso de bicicletas ao longo da semana.
    """
    # Verifica se o DataFrame está vazio
    if df.empty:
        print("Erro: DataFrame vazio.")
        return None

    # Criando um dataframe para contar a distância percorrida por dia da semana
    pickups_por_dia_semana = df.groupby('dia_semana')['distancia'].count().reset_index()

    # Definindo a ordem dos dias da semana para aparecer no gráfico
    dias_da_semana = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    pickups_por_dia_semana['dia_semana'] = pd.Categorical(pickups_por_dia_semana['dia_semana'],
                                                          categories=dias_da_semana, ordered=True)

    # Plotando o gráfico de barras
    fig = px.bar(pickups_por_dia_semana, x='dia semana', y='distancia')

    return fig


# Ok
def distribuicao_uso_bicicletas_horarios(df):
    pickups_por_horario = df.groupby('hora_inicio')['distancia'].count().reset_index()

    fig = px.histogram(pickups_por_horario, x="hora_inicio", y="distancia", nbins=24, width=700, height=400)
    fig.update_layout(
        title_text="Distribuição do uso das bicicletas por horário",
        xaxis_title_text="Horário de início da viagem",
        yaxis_title_text="Número de viagens",
        bargap=0.1,
    )
    fig.show()


def distribuicao_uso_bicicletas_dias_semana_horarios(df):
    # Cria um pivot table para contar o número de viagens por dia da semana e horário
    pivot_table = df.pivot_table(index='dia_semana', columns='hora_inicio', values='id', aggfunc='count')

    # Cria o gráfico de calor
    fig = go.Figure(data=go.Heatmap(
        z=pivot_table,
        x=pivot_table.columns,
        y=pivot_table.index,
        colorscale='Viridis'))

    # Define os eixos e o título
    fig.update_layout(
        title="Distribuição do uso de bicicletas por dia da semana e horário",
        xaxis_title="Horário",
        yaxis_title="Dia da semana",
        xaxis={'type': 'category'},
        yaxis={'type': 'category'}
    )

    # Mostra o gráfico
    fig.show()


def diferenca_dias_uteis_finais_semana(df):
    # Calcula a média de viagens por dia útil
    dias_uteis = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    media_dias_uteis = df[df['dia_semana'].isin(dias_uteis)]['id'].count() / len(dias_uteis)

    # Calcula a média de viagens por final de semana
    finais_semana = ['Saturday', 'Sunday']
    media_finais_semana = df[df['dia_semana'].isin(finais_semana)]['id'].count() / len(finais_semana)

    # Calcula a diferença entre as médias
    diferenca = media_dias_uteis - media_finais_semana

    return diferenca

#---------------------------------
# Novas plotagens
#---------------------------------


def distribuicao_uso_bicicletas_mes(df):
    pickups_por_mes = df.groupby('mes_inicio')['distancia'].count().reset_index()
    pickups_por_mes['mes_inicio'] = pickups_por_mes['mes_inicio'].apply(lambda x: str(x).zfill(2))

    fig = px.bar(pickups_por_mes, x='mes_inicio', y='distancia', color='mes_inicio')
    fig.update_layout(
        title_text="Distribuição do uso das bicicletas por mês",
        xaxis_title_text="Mês",
        yaxis_title_text="Número de viagens",
        bargap=0.1,
    )
    fig.show()


# Fazer Gráfico de Pizza
def distribuicao_uso_bicicletas_ano(df):
    pickups_por_ano = df.groupby('ano_inicio')['distancia'].count().reset_index()

    fig = go.Figure(data=[go.Pie(labels=pickups_por_ano['ano_inicio'], values=pickups_por_ano['distancia'])])
    fig.update_layout(
        title_text="Distribuição do uso das bicicletas por ano",
    )
    fig.show()


# Ok
def distribuicao_uso_bicicletas_genero(df):
    pickups_por_genero = df.groupby('genero')['distancia'].count().reset_index()

    fig = px.pie(pickups_por_genero, values='distancia', names='genero')
    fig.update_layout(
        title_text="Distribuição do uso das bicicletas por gênero",
        showlegend=False,
    )
    fig.show()


# Ok
def distribuicao_uso_bicicletas_idade(df):
    # Calculando a idade das pessoas que alugaram as bicicletas
    df['idade'] = 2023 - df['ano_nascimento']

    # Criando as faixas etárias
    bins = [0, 18, 25, 35, 50, 65, 120]
    labels = ['<18', '18-24', '25-34', '35-49', '50-64', '65+']
    df['faixa_etaria'] = pd.cut(df['idade'], bins=bins, labels=labels)

    pickups_por_faixa_etaria = df.groupby('faixa_etaria')['distancia'].count().reset_index()

    fig = px.bar(pickups_por_faixa_etaria, x='faixa_etaria', y='distancia')
    fig.update_layout(
        title_text="Distribuição do uso das bicicletas por faixa etária",
        xaxis_title_text="Faixa etária",
        yaxis_title_text="Número de viagens",
        bargap=0.1,
    )
    fig.show()


def distribuicao_uso_bicicletas_tipo_usuario(df):
    """
    Esta função plota um gráfico de pizza para mostrar a distribuição do uso de bicicletas por tipo de usuário.
    """
    # Verifica se o DataFrame está vazio
    if df.empty:
        print("Erro: DataFrame vazio.")
        return None

    # Criando um dataframe para contar o número de viagens por tipo de usuário
    contagem_usuarios = df.groupby('tipo_usuario')['distancia'].count().reset_index()

    # Plotando o gráfico de pizza
    fig = px.pie(contagem_usuarios, values='distancia', names='tipo_usuario', hole=0.5)
    fig.update_layout(
        title_text="Distribuição do uso das bicicletas por tipo de usuário",
    )
    fig.show()

# Mais ou menos
def correlacao_duracao_distancia(df):
    """
    Esta função plota um gráfico de dispersão para mostrar a correlação entre a duração da viagem e a distância percorrida.
    """

    # Plotando o gráfico de dispersão
    fig = px.scatter(df, x="duracao_viagem", y="distancia")
    fig.update_layout(
        title_text="Correlação entre duração da viagem e distância percorrida",
        xaxis_title_text="Duração da viagem (min)",
        yaxis_title_text="Distância percorrida (km)",
    )
    fig.show()


# def correlacao_horario_duracao(df):
#     """
#     Esta função plota um gráfico de dispersão para mostrar a correlação entre o horário de início da viagem e a duração da viagem.
#     """
#     # Verifica se o DataFrame está vazio
#     if df.empty:
#         print("Erro: DataFrame vazio.")
#         return None
#
#     # Calculando a duração da viagem em segundos
#     df['duracao'] = ((df['hora_fim'] - df['hora_inicio']))
#
#
#     # Plotando o gráfico de dispersão
#     fig = px.scatter(df, x="hora_inicio", y="duracao")
#     fig.update_layout(
#         title_text="Correlação entre horário de início da viagem e duração da viagem",
#         xaxis_title_text="Horário de início da viagem",
#         yaxis_title_text="Duração da viagem (segundos)",
#     )
#     fig.show()

# Not working properly
# Not working properly
def correlacao_horario_duracao(df):
    """
    Esta função plota um gráfico de dispersão para mostrar a correlação entre o horário de início da viagem e a duração da viagem.
    """
    # Verifica se o DataFrame está vazio
    if df.empty:
        print("Erro: DataFrame vazio.")
        return None

    # Plotando o gráfico de dispersão
    fig = px.scatter(df, x="hora_inicio", y="hora_fim")
    fig.update_layout(
        title_text="Correlação entre horário de início da viagem e duração da viagem",
        xaxis_title_text="Horário de início da viagem",
        yaxis_title_text="Duração da viagem (min)",
    )
    fig.show()


# Not working properly
def mapa_calor_horarios_uso(df):
    """
    Esta função plota um mapa de calor para mostrar a distribuição dos horários de uso das bicicletas ao longo dos dias da semana.
    """
    # Verifica se o DataFrame está vazio
    if df.empty:
        print("Erro: DataFrame vazio.")
        return None

    # Cria um novo dataframe com as colunas de dia da semana e hora de início
    df_mapa_calor = df[['dia_semana', 'hora_inicio']]

    # Cria uma coluna com o valor 1 para cada viagem
    df_mapa_calor['count'] = 1

    # Agrupa os valores por dia da semana e hora de início e soma o número de viagens
    df_mapa_calor = df_mapa_calor.groupby(['dia_semana', 'hora_inicio']).sum().reset_index()

    # Cria o mapa de calor
    fig = px.imshow(df_mapa_calor.pivot('dia_semana', 'hora_inicio', 'count'),
                    x=['00:00', '04:00', '08:00', '12:00', '16:00', '20:00'],
                    y=['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'],
                    color_continuous_scale='reds')

    fig.update_layout(
        title_text="Distribuição dos horários de uso das bicicletas ao longo dos dias da semana"
    )

    return fig

# Not working properly
def evolucao_num_viagens_ano(df):
    """
    Esta função plota um gráfico de linha para mostrar a evolução do número de viagens ao longo dos anos.
    """
    # Verifica se o DataFrame está vazio
    if df.empty:
        print("Erro: DataFrame vazio.")
        return None

    # Cria um novo dataframe com as colunas de data de início e número de viagens
    df_evolucao = df[['data_inicio', 'id']].copy()

    # Agrupa os valores por ano e conta o número de viagens
    df_evolucao = df_evolucao.groupby(df_evolucao['data_inicio'].dt.year)['id'].count().reset_index()

    # Cria o gráfico de linha
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_evolucao['data_inicio'], y=df_evolucao['id'], mode='lines+markers'))

    fig.update_layout(
        title_text="Evolução do número de viagens ao longo dos anos",
        xaxis_title="Ano",
        yaxis_title="Número de viagens"
    )

    return fig


# ok
def distribuicao_idades(df):
    """
    Esta função plota um gráfico de barras para mostrar a distribuição das idades dos usuários.
    """
    # Verifica se o DataFrame está vazio
    if df.empty:
        print("Erro: DataFrame vazio.")
        return None

    # Criando um histograma com a distribuição das idades
    fig = px.histogram(df, x='idade', nbins=20)
    fig.update_layout(title='Distribuição das idades dos usuários')
    fig.show()


# Not working properly
def relacao_idade_duracao_media(df):
    """
    Esta função plota um gráfico de dispersão para mostrar a relação entre a idade dos usuários e a duração média das viagens.
    """
    # Verifica se o DataFrame está vazio
    if df.empty:
        print("Erro: DataFrame vazio.")
        return None

    # Criando um scatter plot com a relação entre idade e duração média
    fig = px.scatter(df, x='idade', y='duracao_viagem_media')
    fig.update_layout(title='Relação entre idade dos usuários e duração média das viagens')
    fig.show()


# Not working properly
def relacao_idade_distancia_media(df):
    """
    Esta função plota um gráfico de dispersão para mostrar a relação entre a idade dos usuários e a distância média percorrida nas viagens.
    """
    # Verifica se o DataFrame está vazio
    if df.empty:
        print("Erro: DataFrame vazio.")
        return None

    # Criando um scatter plot com a relação entre idade e distância média percorrida
    fig = px.scatter(df, x='idade', y='distancia_media')
    fig.update_layout(title='Relação entre idade dos usuários e distância média percorrida nas viagens')
    fig.show()



def dispersao_idade_velocidade(df):
    """
    Esta função plota um gráfico de dispersão para mostrar a relação entre a idade dos usuários e a velocidade média das viagens.
    """
    # Verifica se o DataFrame está vazio
    if df.empty:
        print("Erro: DataFrame vazio.")
        return None

    # Cálculo da velocidade média das viagens
    df['velocidade_media'] = df['distancia_percorrida'] / df['duracao_viagem']

    # Criação do gráfico de dispersão
    fig = px.scatter(df, x='idade_usuario', y='velocidade_media', trendline='ols',
                     title='Relação entre Idade dos Usuários e Velocidade Média das Viagens')

    # Personalização do layout do gráfico
    fig.update_layout(xaxis_title='Idade do Usuário', yaxis_title='Velocidade Média (km/h)', font=dict(size=12))

    # Exibição do gráfico
    fig.show()




if __name__ == '__main__':
    df = pd.DataFrame()  # Or define df as the result of another function call, if applicable
    df = extrair_dados()
    # distribuicao_distancias(df)
    # relacao_idade_duracao_media(df)
    # correlacao_tipo_usuario_tipo_bicicleta(df)
    # evolucao_num_viagens_ano(df)
    # distribuicao_uso_bicicletas_mes(df)