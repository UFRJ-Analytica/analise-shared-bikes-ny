import os
import requests
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import statsmodels.api as sm
from limpeza_dos_dados import Limpeza
import logging

# Configurando o logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
log = logger.info


# =================================================================
# Unidades de Tempo
# =================================================================


class Tempo:

    def __init__(self, df):

        # separando o datetime em unidades de tempo
        df['dia_inicio'] = df['inicio_viagem'].dt.day
        df['mes_inicio'] = df['inicio_viagem'].dt.month
        df['ano_inicio'] = df['inicio_viagem'].dt.year
        df['dia_fim'] = df['fim_viagem'].dt.day
        df['mes_fim'] = df['fim_viagem'].dt.month
        df['ano_fim'] = df['fim_viagem'].dt.year
        df['hora_inicio'] = df['inicio_viagem'].dt.hour
        df['minuto_inicio'] = df['inicio_viagem'].dt.minute
        df['segundo_inicio'] = df['inicio_viagem'].dt.second
        df['hora_fim'] = df['fim_viagem'].dt.hour
        df['minuto_fim'] = df['fim_viagem'].dt.minute
        df['segundo_fim'] = df['fim_viagem'].dt.second
        df['idade'] = df['ano_inicio'] - df['ano_nascimento']

        log(df)


    def calculo_idade(self, df):
        df['idade'] = df['ano_inicio'] - df['ano_nascimento']
        return df



if __name__ == '__main__':
    limpeza = Limpeza()

    # Ler Dataset
    df = pd.read_parquet("../Dados/BikeData-Processed.parquet")
    # Tratar dados vazios
    df_tratado = limpeza.valores_vazios(df)
    # Remover Outliers
    df = limpeza.remove_outliers(df_tratado)


    #============================================================
    #  Distribuições
    #============================================================
    tempo = Tempo(df)

    # Calcula a Idade
    tempo.calculo_idade(df)

