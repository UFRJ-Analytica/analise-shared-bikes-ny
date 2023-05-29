import pandas as pd
from Tratamento import tratamento_dados

def main() -> None:
    # ID do Google Drive
    FILE_ID = "1a8gzQg37aaDHBO6OBVMieOZmNU7jTOL1"

    #  Link do arquivo
    link = f"https://drive.google.com/uc?export=download&id={FILE_ID}"

    # Obtendo os Dados Brutos e Salvando na pasta Dados
    df = pd.read_parquet(link)
    df.to_parquet("../Dados/BikeData-Raw.parquet", index=False)
    
    #  Tratando os dados e salvando na pasta Dados
    #df = tratamento_dados(df)
    #df.to_parquet("../Dados/BikeData-Processed.parquet", index=False, engine="pyarrow", strings_to_categorical=True)
    


if __name__ == "__main__":
    main()
