import haversine as hv
import limpeza_dos_dados as ld
from Tratamento import tratamento_dados
import pandas as pd



def extrair_dados() -> pd.DataFrame:
      
    def series_to_time_series(df: pd.DataFrame, coluna_referencia: str) -> pd.Series:
        return (
            df[coluna_referencia]
            .dt
            .floor('H')  
            .value_counts()
            .sort_index()
            .rename('qnt_viagens')
            .reindex(
                index = pd.date_range(
                    start=df[coluna_referencia].dt.floor('H').min(), 
                    end=df[coluna_referencia].dt.floor('H').max(),
                    freq='H'
                ),
                method="pad"
            )
        )
    
    #  Objeto para limpeza dos dados
    limpeza = ld.Limpeza()

    df_clean = (
        pd.read_parquet("../Dados/BikeData-Raw.parquet")
        .pipe(tratamento_dados)
        .pipe(limpeza.valores_vazios)
        .pipe(limpeza.remove_outliers)
        .pipe(series_to_time_series, coluna_referencia = 'inicio_viagem')
    )
    return df_clean
