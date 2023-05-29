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
# Distribuição dos Dados
# =================================================================


class Distribution:

    def __init__(self):

        '''
        duracao_viagem:           0 tipo: numérico
        inicio_viagem:            0 tipo: data/hora
        fim_viagem:               0 tipo: data/hora
        id_estacao_inicio:       73 tipo: numérico
        nome_estacao_inicio:     73 tipo: categórico
        estacao_inicio_latitude: 0 tipo: numérico
        estacao_inicio_longitude: 0 tipo: numérico
        id_estacao_fim:          73 tipo: numérico
        nome_estacao_fim:        73 tipo: categórico
        estacao_fim_latitude:    0 tipo: numérico
        estacao_fim_longitude:   0 tipo: numérico
        id_bike:                  0 tipo: numérico
        tipo_usuario:             0 tipo: categórico
        ano_nascimento:           0 tipo: numérico
        genero:                   0 tipo: categórico
        dtype: int64
        '''
        pass


    def dias_da_semana(self):
        ...


    def dias_horarios(self):
        ...



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
    distribuicao = Distribution()

    #  distribuição do uso de bicicletas (pickups) durante os dias da semana
    distribuicao.dias_da_semana()

    #  distribuição do uso de bicicletas (pickups) durante os horários do dia
    distribuicao.dias_horarios()

    df.head()
