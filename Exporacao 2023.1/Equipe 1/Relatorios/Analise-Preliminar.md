# Visão Preliminar dos Dados

## Juan

- Limpeza dos Dados
  - Outliers
  - Valores Vazios
    - Poucos Casos
  - Problemas na Tipagem dos dados
    - Coluna de Data
    - Passível de algumas otimizações
  - Renomeação de dados pra melhorar a compreensão
    - Coluna "Gender"
- Possibilidades de Criação de Novas Variáveis
  - Distancia da Viagem
    - API google Maps
    - Calculo Haversine
      - Dado que a terra não é plana, calcular a distancia euclidiana está errado
  - Idades dos Clientes
  - Variáveis relacionadas a datas
    - Mes
    - Dia
    - Hora
    - Minuto
  - Velocidade Média
    - Pode ter pessoas que pegaram a bike e deixaram de pedalar por um período curto, mas acredito que seja um grupo pequeno
- Análise Exploratória de Dados
  - Estatística
    - Análise multivariada
  - Demanda
    - Demanda em relação aos consumidores
      - Idade
      - Sexo
      - Tipo de Plano
    - Demanda em relação a região
      - Quais regiões são mais utilizadas?
      - Quais regiões são menos utilizadas?
      - Relação entre clientes e regiões
    - Demanda em relação ao horário
      - Quais os horários de maior demanda?
      - Quais os horários de menor demanda?
      - Relação entre o Tipo dos Consumidores por Horário
        - Necessário realizar algum tipo de trabalho de segmentação dos consumidores (Clustering)
  - Oferta
    - Localização geo-espacial das estações
    - Bicicletas
      - Distribuição geo-espacial
      - Quantidade Total
- Modelagem
  - Segmentação de Consumidores
  - Previsão de Demanda por Região
  - Previsão do Uso de Bikes


## Tarefas Geral

- Possibilidades de Criação de Novas Variáveis
  - Distancia da Viagem
    - API google Maps
    - Calculo Haversine
      - Dado que a terra não é plana, calcular a distancia euclidiana está errado
  - Velocidade Média
    - Pode ter pessoas que pegaram a bike e deixaram de pedalar por um período curto, mas acredito que seja um grupo pequeno

### Juan

- Problemas na Tipagem dos dados -- OK
  - Coluna de Data -- OK
  - Passível de algumas otimizações -- OK
- Renomeação de dados pra melhorar a compreensão -- OK
  - Coluna "Gender" -- OK

### Gabriel

- Idades dos Clientes
- Variáveis relacionadas a datas
  - Mes
  - Dia
  - Hora
  - Minuto

### Gustavo
- Valores Vazios  -- OK
    - Poucos Casos
- Outliers    -- OK para dados numéricos 
