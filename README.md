# Análise de Preços de Passagens Aéreas

Este repositório contém um projeto de análise de preços de passagens aéreas, utilizando **machine learning** para prever os preços das passagens com base em variáveis como dias restantes para a partida, cidade de origem, cidade de destino, companhia aérea, entre outras. O projeto também inclui visualizações para ajudar na análise dos dados.

## Estrutura do Projeto

1. **Importação de bibliotecas e carregamento de dados**
   - O código começa com a importação das bibliotecas necessárias, como `pandas`, `seaborn`, `matplotlib`, `sklearn`, e `xgboost`. 
   - Em seguida, carrega um conjunto de dados sobre passagens aéreas para análise.

2. **Análise exploratória e visualização de dados**
   - Gráficos de linha são gerados para visualizar a relação entre os dias restantes para a partida e o preço das passagens.
   - A visualização inclui gráficos de linha com diferentes paletas de cores para mostrar as variações de preço entre as companhias aéreas.

3. **Preparação e pré-processamento dos dados**
   - Conversão de variáveis categóricas para variáveis numéricas utilizando `LabelEncoder`.
   - Normalização dos dados com o `MinMaxScaler`, transformando os dados para uma escala de 0 a 1.

4. **Treinamento e avaliação dos modelos**
   - Diversos modelos de regressão são treinados para prever o preço das passagens:
     - **Linear Regression**
     - **Decision Tree Regressor**
     - **Random Forest Regressor**
     - **Extra Trees Regressor**
   - A avaliação do modelo é feita utilizando métricas como:
     - Erro Absoluto Médio (MAE)
     - Erro Quadrático Médio (MSE)
     - Raiz do Erro Quadrático Médio (RMSE)
     - R²
     - Raiz do Erro Quadrático Logarítmico (RMSLE)
     - Erro Percentual Absoluto Médio (MAPE)
   - A métrica `R² Ajustado` é calculada para ajustar a pontuação R², levando em consideração a complexidade do modelo.

5. **Previsão de preços**
   - Após o treinamento do modelo escolhido, o código faz previsões sobre os preços das passagens para o conjunto de dados de teste.

6. **Resultados**
   - Um resumo das métricas de desempenho de cada modelo é impresso e organizado em um DataFrame.
   - O modelo de melhor desempenho é escolhido com base na métrica de `R² Ajustado` e as previsões são comparadas com os preços reais das passagens.

## Como Usar

1. **Carregue os dados**:
   - Modifique o caminho do arquivo de dados no código para carregar seu próprio conjunto de dados de passagens aéreas.

2. **Execute a análise**:
   - O código já está configurado para realizar a análise de preços, treinar os modelos de regressão e gerar as visualizações automaticamente.

3. **Visualize os resultados**:
   - Os resultados de cada modelo serão exibidos no terminal ou no console Python.
   - O gráfico de linhas e as previsões também são exibidos para análise visual.

## Resultados Esperados

- **Modelos Avaliados**: O código treina quatro modelos de regressão para prever o preço das passagens aéreas.
- **Métricas**:
  - O `R² Ajustado` será usado para avaliar qual modelo possui o melhor ajuste para os dados.
  - O `MAPE` e o `MAE` serão usados para entender a precisão do modelo.
- **Previsões**:
  - Após o treinamento, as previsões serão comparadas com os preços reais, e um gráfico de comparação será gerado.

## Exemplos de Resultados

| Modelo                      | R² Ajustado | MAE    | RMSE   | MAPE (%) |
|-----------------------------|-------------|--------|--------|----------|
| RandomForestRegressor        | 0.988985    | 893.24 | 2381.00 | 6.00     |
| KNeighborsRegressor          | 0.987290    | 944.16 | 2557.66 | 6.41     |
| DecisionTreeRegressor        | 0.982736    | 909.15 | 2980.79 | 6.20     |
| LinearRegression             | 0.904669    | 4623.41 | 7004.43 | 43.66    |