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

#regressao linear multipla utiliza mais de um atributo para realizar a analise

X = dataset.iloc[:, [2, 3, 9, 10]].values
y = dataset.iloc[:, 0].values

#gerando graficos
f, ax = plt.subplots(2, 2)
ax[0, 0].hist(X[0])
ax[1, 0].hist(X[1])
ax[0, 1].hist(X[2])
ax[1, 1].hist(X[3])
plt.show()

#transformando os dados em uma distribuição normal com logaritmo
y = np.log(y)

#separando a base para treinamento e teste
from sklearn.model_selection import train_test_split
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y, test_size=0.2, random_state=1)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_treinamento, y_treinamento)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)

regressor.score(X_treinamento, y_treinamento)
regressor.score(X_teste, y_teste)

from sklearn.metrics import mean_absolute_error, mean_squared_error

previsoes = regressor.predict(X_teste)
print(previsoes)
print(mean_absolute_error(y_teste, previsoes))
