# An�lise de Pre�os de Passagens A�reas

Este reposit�rio cont�m um projeto de an�lise de pre�os de passagens a�reas, utilizando **machine learning** para prever os pre�os das passagens com base em vari�veis como dias restantes para a partida, cidade de origem, cidade de destino, companhia a�rea, entre outras. O projeto tamb�m inclui visualiza��es para ajudar na an�lise dos dados.

## Estrutura do Projeto

1. **Importa��o de bibliotecas e carregamento de dados**
   - O c�digo come�a com a importa��o das bibliotecas necess�rias, como `pandas`, `seaborn`, `matplotlib`, `sklearn`, e `xgboost`. 
   - Em seguida, carrega um conjunto de dados sobre passagens a�reas para an�lise.

2. **An�lise explorat�ria e visualiza��o de dados**
   - Gr�ficos de linha s�o gerados para visualizar a rela��o entre os dias restantes para a partida e o pre�o das passagens.
   - A visualiza��o inclui gr�ficos de linha com diferentes paletas de cores para mostrar as varia��es de pre�o entre as companhias a�reas.

3. **Prepara��o e pr�-processamento dos dados**
   - Convers�o de vari�veis categ�ricas para vari�veis num�ricas utilizando `LabelEncoder`.
   - Normaliza��o dos dados com o `MinMaxScaler`, transformando os dados para uma escala de 0 a 1.

4. **Treinamento e avalia��o dos modelos**
   - Diversos modelos de regress�o s�o treinados para prever o pre�o das passagens:
     - **Linear Regression**
     - **Decision Tree Regressor**
     - **Random Forest Regressor**
     - **Extra Trees Regressor**
   - A avalia��o do modelo � feita utilizando m�tricas como:
     - Erro Absoluto M�dio (MAE)
     - Erro Quadr�tico M�dio (MSE)
     - Raiz do Erro Quadr�tico M�dio (RMSE)
     - R�
     - Raiz do Erro Quadr�tico Logar�tmico (RMSLE)
     - Erro Percentual Absoluto M�dio (MAPE)
   - A m�trica `R� Ajustado` � calculada para ajustar a pontua��o R�, levando em considera��o a complexidade do modelo.

5. **Previs�o de pre�os**
   - Ap�s o treinamento do modelo escolhido, o c�digo faz previs�es sobre os pre�os das passagens para o conjunto de dados de teste.

6. **Resultados**
   - Um resumo das m�tricas de desempenho de cada modelo � impresso e organizado em um DataFrame.
   - O modelo de melhor desempenho � escolhido com base na m�trica de `R� Ajustado` e as previs�es s�o comparadas com os pre�os reais das passagens.

## Como Usar

1. **Carregue os dados**:
   - Modifique o caminho do arquivo de dados no c�digo para carregar seu pr�prio conjunto de dados de passagens a�reas.

2. **Execute a an�lise**:
   - O c�digo j� est� configurado para realizar a an�lise de pre�os, treinar os modelos de regress�o e gerar as visualiza��es automaticamente.

3. **Visualize os resultados**:
   - Os resultados de cada modelo ser�o exibidos no terminal ou no console Python.
   - O gr�fico de linhas e as previs�es tamb�m s�o exibidos para an�lise visual.

## Resultados Esperados

- **Modelos Avaliados**: O c�digo treina quatro modelos de regress�o para prever o pre�o das passagens a�reas.
- **M�tricas**:
  - O `R� Ajustado` ser� usado para avaliar qual modelo possui o melhor ajuste para os dados.
  - O `MAPE` e o `MAE` ser�o usados para entender a precis�o do modelo.
- **Previs�es**:
  - Ap�s o treinamento, as previs�es ser�o comparadas com os pre�os reais, e um gr�fico de compara��o ser� gerado.

## Exemplos de Resultados

| Modelo                      | R� Ajustado | MAE    | RMSE   | MAPE (%) |
|-----------------------------|-------------|--------|--------|----------|
| RandomForestRegressor        | 0.988985    | 893.24 | 2381.00 | 6.00     |
| KNeighborsRegressor          | 0.987290    | 944.16 | 2557.66 | 6.41     |
| DecisionTreeRegressor        | 0.982736    | 909.15 | 2980.79 | 6.20     |
| LinearRegression             | 0.904669    | 4623.41 | 7004.43 | 43.66    |