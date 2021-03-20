import pandas as pd
import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt
from yellowbrick.target import FeatureCorrelation

dataset = pd.read_csv('house_prices.csv')

#removendo atributos que nao serao utilizados para analise
dataset.drop(labels=['id', 'date'], axis=1, inplace=True)

print(dataset.head())

# sns.heatmap(dataset.corr(), annot=True)
# plt.show()

#coeficiente determinaçao
coeficiente_determinacao_preco_metragem = math.pow(0.7, 2)
print(coeficiente_determinacao_preco_metragem)

#regressao simples
X = dataset["sqft_living"].values

X = X.reshape(-1, 1)
print(X.shape)

y = dataset["price"].values
#separando a base para treinamento e teste
from sklearn.model_selection import train_test_split
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y, test_size=0.2, random_state=1)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_treinamento, y_treinamento)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)

#b0
b0 = regressor.intercept_

#b1
b1 = regressor.coef_

print(f"b0: {b0} b1: {b1}")

#prevendo o preço da casa usando b0 e b1
metragem_casa = 770

resultado = b0 + b1 * metragem_casa

print(f"Resultado previsto: {resultado}")

#é possivel obter o mesmo resultado usando o predict
# regressor.predict(np.array([[900]]))

plt.scatter(X, y)
plt.plot(X, regressor.predict(X), 'o', color = 'red')
plt.show()

r2_treinamento = regressor.score(X_treinamento, y_treinamento)
r2_teste = regressor.score(X_teste, y_teste)

previsoes = regressor.predict(X_teste)

print(f"previsoes: {previsoes} y_teste: {y_teste}")

from sklearn.metrics import mean_absolute_error, mean_squared_error

print(mean_absolute_error(y_teste, previsoes))

print(mean_squared_error(y_teste, previsoes))

print(math.sqrt(mean_squared_error(y_teste, previsoes)))
