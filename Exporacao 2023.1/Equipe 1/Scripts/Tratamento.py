import pandas as pd

def tratamento_dados(df: pd.DataFrame) -> pd.DataFrame:
    return df.rename(
        columns={
            "tripduration": "duracao_viagem",
            "starttime": "inicio_viagem",
            "stoptime": "fim_viagem",
            "start station id": "id_estacao_inicio",
            "start station name": "nome_estacao_inicio",
            "start station latitude": "estacao_inicio_latitude",
            "start station longitude": "estacao_inicio_longitude",
            "end station id": "id_estacao_fim",
            "end station name": "nome_estacao_fim",
            "end station latitude": "estacao_fim_latitude",
            "end station longitude": "estacao_fim_longitude",
            "bikeid": "id_bike",
            "usertype": "tipo_usuario",
            "birth year": "ano_nascimento",
            "gender": "genero",
        }
    ).assign(
        inicio_viagem=lambda x: pd.to_datetime(x.inicio_viagem),
        fim_viagem=lambda x: pd.to_datetime(x.fim_viagem),
        id_estacao_inicio=lambda x: x.id_estacao_inicio.astype("category"),
        nome_estacao_inicio=lambda x: x.nome_estacao_inicio.astype("category"),
        id_estacao_fim=lambda x: x.id_estacao_fim.astype("category"),
        id_bike=lambda x: x.id_bike.astype("category"),
        nome_estacao_fim=lambda x: x.nome_estacao_fim.astype("category"),
        tipo_usuario=lambda x: x.tipo_usuario.astype("category"),
        genero=lambda x: x.genero.apply(
            lambda y: "Masculino"
            if y == 1
            else "Feminino"
            if y == 2
            else "Desconhecido"
        ).astype("category"),
    )