# Tech-Challenge-Fase-2-FIAP-P-s-Tech-Data-Analytics-2026
## Classificação da Qualidade de Vinhos com Machine Learning
Este projeto tem como objetivo desenvolver modelos de Machine Learning capazes de classificar a qualidade de vinhos tintos com base em suas propriedades físico químicas. O dataset utilizado (WineQT.csv) contém variáveis como acidez, teor alcoólico, pH, densidade, dióxido de enxofre, entre outras.

# Grupo 47
- Adriane de Souza Lino – euadrianee@gmail.com 
- Barbara Rodrigues Gusmão Rebelo – barbaragusmao906@gmail.com 
- Bruna Alessandra Belotto – bruna.belotto@gmail.com 
- Sidnei Rocha – sidroch@gmail.com

1. Dataset
O arquivo contém 13 variáveis químicas e 1 variável alvo (quality), além de um identificador (Id). Exemplos de colunas:
- fixed acidity
- volatile acidity
- citric acid
- residual sugar
-	chlorides
-	free sulfur dioxide
-	total sulfur dioxide
-	density
-	pH
-	sulphates
-	alcohol
-	quality
-	Id
A variável quality varia de 3 a 8, representando a avaliação sensorial do vinho.

2. Objetivo do Projeto
Transformar o problema em uma classificação binária, onde:
•	1 → Alta qualidade (quality ≥ 7)
•	0 → Baixa/média qualidade (quality < 7)

O objetivo é identificar quais características químicas influenciam a qualidade e construir modelos capazes de prever se um vinho é “bom” ou “ruim”.

 3. Análise Exploratória de Dados (EDA)
A EDA inclui:
•	Histogramas das variáveis químicas
•	Distribuição da variável quality
•	Criação da variável binária quality_bin
•	Heatmap de correlação
•	Boxplots comparando vinhos bons vs. ruins
•	Identificação de outliers (ex.: acidez volátil muito alta)

Insights observados:
•	Vinhos de alta qualidade tendem a ter teor alcoólico maior.
•	Acidez volátil elevada está associada a qualidade mais baixa.
•	Sulfatos e citric acid apresentam correlação moderada com qualidade.

4. Pré processamento
Etapas realizadas:
•	Remoção da coluna Id
•	Padronização das variáveis com StandardScaler
•	Separação entre treino e teste (80/20)
•	Verificação de balanceamento da classe
•	Construção de pipelines para garantir reprodutibilidade

5. Modelos Utilizados
Modelos clássicos
•	Logistic Regression (baseline)
•	Random Forest Classifier
•	Support Vector Machine (SVC)
Modelos avançados
•	XGBoost
•	LightGBM

Esses modelos foram escolhidos para comparar desempenho entre abordagens lineares, não lineares e algoritmos de gradient boosting.

 6. Avaliação dos Modelos
As métricas utilizadas incluem:
•	Acurácia
•	Precision, Recall e F1-score
•	Matriz de confusão
•	ROC AUC (quando aplicável)

Os modelos de boosting (XGBoost e LightGBM) apresentaram desempenho superior aos modelos clássicos.
 7. Interpretabilidade com SHAP
Para entender o impacto de cada variável na previsão:
•	SHAP TreeExplainer aplicado ao modelo XGBoost
•	Summary Plot para importância global
•	Force Plot para explicações individuais

Principais conclusões:
•	Álcool é o maior preditor de qualidade.
•	Acidez volátil reduz a probabilidade de alta qualidade.
•	Sulfatos e citric acid contribuem positivamente em alguns casos.

10. Tecnologias Utilizadas
•	Python
•	Pandas, NumPy
•	Matplotlib, Seaborn
•	Scikit Learn
•	XGBoost
•	LightGBM
•	SHAP
•	Google Colab


└── requirements.txt

