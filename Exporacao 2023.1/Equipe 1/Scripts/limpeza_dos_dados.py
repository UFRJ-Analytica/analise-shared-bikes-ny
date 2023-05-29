import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import statsmodels.api as sm

import logging

# Configurando o logger
from sklearn.preprocessing import StandardScaler

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
log = logger.info


# =================================================================
# Limpeza dos Dados
# =================================================================

def is_numeric(column):
    try:
        pd.to_numeric(column)
        return True
    except ValueError:
        return False

class Limpeza:
    """
    Exemplo de Uso
    ================================

    Ler Dataset
    df = pd.read_parquet("../Dados/BikeData-Processed.parquet")
    Tratar dados vazios
    df_tratado = limpeza.valores_vazios(df)
    Remover Outliers
    df = limpeza.remove_outliers(df_tratado)
    """

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
    
    
    @staticmethod
    def valores_vazios(dataframe):
        """
        Identifica e trata valores vazios em um dataframe.

        Argumentos:
        dataframe -- um dataframe

        Retorno:
        Um dataframe sem valores vazios.
        """
        #  Criando uma cópia do dataframe
        _df = dataframe.copy()


        # Identificando valores vazios
        log('Identificando valores vazios...')
        log(_df.isnull().sum())

        #  Identificando colunas com valores vazios
        null_columns_names = _df.columns[_df.isnull().any()]
        
        # Tratando valores vazios
        log('Tratando valores vazios...')
        for col in null_columns_names:
            if _df[col].dtype.name == 'category':
                log(f'Coluna {col} é categórica.')
                imp_mode = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
                _df[col] = imp_mode.fit_transform(_df[[col]]).ravel()
            elif is_numeric(_df[col]):
                log(f'Coluna {col} é numérica.')
                imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
                _df[col] = imp_mean.fit_transform(_df[[col]]).ravel()

        log('Valores vazios tratados.')
        return _df

    @staticmethod
    def remove_outliers(dataframe, columns=None):
        """
        Identifica e remove outliers de um dataframe.

        Argumentos:
        dataframe -- um dataframe
        columns -- uma lista com as colunas a serem analisadas. Se não for informado, todas as colunas serão analisadas.

        Retorno:
        Um dataframe sem outliers.
        """
        _df = dataframe.copy()
        
        log('Identificando outliers...')
        if columns is None:
            columns = _df.select_dtypes(include='number').columns

        # Usando o método de Tukey para identificar outliers
        for column in columns:
            q1 = _df[column].quantile(0.25)
            q3 = _df[column].quantile(0.75)
            iqr = q3 - q1
            low = q1 - 1.5 * iqr
            high = q3 + 1.5 * iqr
            outliers = _df[(_df[column] < low) | (_df[column] > high)]
            if len(outliers) > 0:
                log(f'{column}: {len(outliers)} outliers encontrados.')
                # print(outliers)

        # Removendo outliers
        log('Removendo outliers...')
        num_rows_before = len(_df)
        for column in columns:
            q1 = _df[column].quantile(0.25)
            q3 = _df[column].quantile(0.75)
            iqr = q3 - q1
            low = q1 - 1.5 * iqr
            high = q3 + 1.5 * iqr
            _df = _df[(_df[column] >= low) & (_df[column] <= high)]
        num_rows_after = len(_df)
        log(f'Outliers removidos. Tamanho antes: {num_rows_before}, tamanho depois: {num_rows_after}.')
        return _df

    def normalizacao_zscore(self, col):
        # Normaliza os dados de uma coluna utilizando a técnica Z-Score
        scaler = StandardScaler()
        self.df[col] = scaler.fit_transform(self.df[col].values.reshape(-1, 1))
        log('Coluna {} normalizada utilizando Z-Score'.format(col))


if __name__ == '__main__':
    pass
    # Lendo Dataset
    #df = pd.read_parquet("../Dados/BikeData-Processed.parquet")
    ## log(df.info)
#
    ## Identificando valores vazios
    #nulos = df.isna().sum()
    #log('Quantidade de nulos: {}'.format(len(nulos)))
    #log('Valores nulos:\n {}'.format(nulos))
#
    #'''     
    #        Explorar ausência dos dados:
    #        ==============================
    #        id_estacao_inicio:   73 tipo: numérico
    #        id_estacao_fim       73 tipo: numérico
    #        nome_estacao_inicio  73 tipo: categórico            
    #        nome_estacao_fim     73 tipo: categórico
    #               
    #'''
#
    ## Preencher com valores fixos:
    ## Media
#
    ## classe para limpeza dos dados
    #limpeza = Limpeza()
    ## df = df.drop(columns=['inicio_viagem', 'fim_viagem', 'nome_estacao_inicio', 'nome_estacao_fim'])
    #df_tratado = limpeza.valores_vazios(df)
    #log(f'Dataframe tratado: \n {df_tratado.isnull().sum()}')
#
    ## removendo outliers
    #df = limpeza.remove_outliers(df_tratado)
    #log('Outliers removido')

