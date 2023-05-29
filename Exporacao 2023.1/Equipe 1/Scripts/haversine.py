
import pandas as pd
import math
from limpeza_dos_dados import Limpeza

import logging

# Configurando o logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
log = logger.info


#limpeza = Limpeza()
#
## Ler Dataset
#df = pd.read_parquet("../Dados/BikeData-Processed.parquet")
## Tratar dados vazios
#df_tratado = limpeza.valores_vazios(df)
## Remover Outliers
#df = limpeza.remove_outliers(df_tratado)

def haversine(estacao_inicio_latitude, estacao_inicio_longitude, estacao_fim_latitude, estacao_fim_longitude):
    """
    Calculate the distance between two points on the Earth's surface using the haversine formula.
    :param lat1: Latitude of the first point in degrees.
    :param lon1: Longitude of the first point in degrees.
    :param lat2: Latitude of the second point in degrees.
    :param lon2: Longitude of the second point in degrees.
    :return: Distance between the two points in kilometers.
    """
    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(estacao_inicio_latitude)
    lon1_rad = math.radians(estacao_inicio_longitude)
    lat2_rad = math.radians(estacao_fim_latitude)
    lon2_rad = math.radians(estacao_fim_longitude)

    # Haversine formula
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = 6371 * c  # Radius of the Earth in kilometers
    return distance


def calculate_haversine(row):
    return haversine(row['estacao_inicio_latitude'], row['estacao_inicio_longitude'], row['estacao_fim_latitude'], row['estacao_fim_longitude'])


#df['distancia'] = df.apply(calculate_haversine, axis=1)


#log(df)

