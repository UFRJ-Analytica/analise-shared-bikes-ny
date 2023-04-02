# Análise de dados do Citi Bike de Nova Iorque

## Introdução

O objetivo deste projeto é realizar uma análise dos dados do sistema de compartilhamento de bicicletas da cidade de Nova Iorque, conhecido como Citi Bike. Desde seu lançamento em 2013, o Citi Bike tem se tornado cada vez mais popular na cidade.

Para esta análise, serão utilizados dados abertos fornecidos pelo Citi Bike para explorar informações sobre o uso das bicicletas, padrões de viagem, duração média de uso, rotas mais comuns e outras informações relevantes.

Com o intuito de tornar a análise mais clara e organizada, serão utilizados notebooks jupyter e markdown para explicar cada seção e garantir que a compreensão do leitor seja aprimorada.

## Análise de Dados

Você tem a liberdade de conduzir sua própria análise de dados, com base nas perguntas que achar mais relevantes. Entretanto, sugerimos um roteiro básico que inclui as seguintes etapas:

- Comece analisando os dados para compreender o uso e identificar erros. Realize todas as análises relevantes.
- Levante questões que precisam ser respondidas antes de iniciar a análise. Interrompa a leitura aqui e elabore suas próprias questões.
- Como é a distribuição do tempo de uso? Essa distribuição varia de acordo com os dias da semana ou horários do dia?
- Visualize as estações no mapa para entender sua distribuição geográfica. Utilize a biblioteca Plotly, com a ferramenta Scatter Mapbox.
- Quais são as estações mais populares e o que as torna especiais? Existe alguma relação entre elas? Visualize a popularidade no mapa usando o tamanho dos círculos ou cores.
- Quais são as rotas mais populares (origem-destino) e o que as torna especiais? Existe alguma relação entre elas?
- Qual é a distribuição do uso de bicicletas (pickups) durante os dias da semana? Existem dias de pico?
- Qual é a distribuição do uso de bicicletas (pickups) durante os horários do dia? Existem horas de pico? Essa distribuição se mantém em todos os dias da semana? Há diferenças entre dias úteis e finais de semana?
- É possível analisar corridas em pares, ou seja, pessoas que pegam e deixam as bicicletas juntas? Quais são as estações mais usadas para isso? E as rotas mais utilizadas?
- Existe alguma relação entre o tempo de viagem e a idade ou gênero dos indivíduos?
- Como é a distribuição de idade e gênero por estação? Há diferenças entre as estações?

## Predição

O objetivo nesta etapa é criar um modelo capaz de prever a quantidade diária de bicicletas alugadas para cada hora do dia, considerando tanto o dia da semana quanto a hora. Para isso, é necessário transformar os dados em uma série temporal, onde a variável alvo é a quantidade de viagens iniciadas por dia e hora.

Para avaliar o desempenho do modelo, é sugerido utilizar uma divisão dos dados em conjuntos de treinamento e teste. Além disso, algumas métricas que podem ser úteis para avaliar o modelo incluem:

- **Erro absoluto médio (MAE):** é uma métrica simples que mede a diferença absoluta média entre as previsões do modelo e os valores reais.
- **Erro quadrático médio (MSE):** mede a média das diferenças quadráticas entre as previsões e os valores reais.
- **Raiz do erro quadrático médio (RMSE):** é a raiz quadrada do MSE, o que faz com que esta métrica tenha a mesma unidade da variável alvo.
- **Coeficiente de determinação (R²):** é uma métrica que varia de 0 a 1 e mede a proporção da variação total da variável alvo que é explicada pelo modelo. Um valor de R² próximo a 1 indica que o modelo explica uma grande parte da variação da variável alvo, enquanto um valor próximo a 0 indica que o modelo não é capaz de explicar a variação observada.
- **Erro Percentual Absoluto Médio (MAPE):** calcula a média do valor absoluto da diferença percentual entre os valores previstos e os valores reais.

O objetivo não é utilizar todas as métricas, mas sim selecionar aquela(s) que melhor se adequam ao modelo e explicar o motivo pelo qual foi escolhida.
