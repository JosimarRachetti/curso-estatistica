import imblearn.under_sampling
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import numpy as np

dataset = pd.read_csv('csv_result-ebay_confianca_completo.csv')

dataset['blacklist'] = dataset['blacklist'] == 'S'

# cria uma gráfico dos dados de c#default
sns.countplot(dataset['reputation'])
# mostra o gráfico em uma imagem

X = dataset.iloc[:, 0:74].values
y = dataset.iloc[:, 74].values

x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(X, y, test_size = 0.2, stratify = y)

modelo = RandomForestClassifier()
modelo.fit(x_treinamento, y_treinamento)

previsoes = modelo.predict(x_teste)

from sklearn.metrics import accuracy_score
print(accuracy_score(previsoes, y_teste))


tl = imblearn.under_sampling.TomekLinks(sampling_strategy='majority')
# gerando a amostra com técnica de subamostragem(retirando valores da amostra para balancear)
x_under, y_under = tl.fit_sample(X, y)

x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(x_under, y_under, test_size = 0.2, stratify = y_under)

modelo = RandomForestClassifier()
modelo.fit(x_treinamento, y_treinamento)

previsoes = modelo.predict(x_teste)

from sklearn.metrics import accuracy_score
print(accuracy_score(previsoes, y_teste))

smote = imblearn.over_sampling.SMOTE(sampling_strategy='minority')
# gerando amostra com tecnica de sobreamostragem (criando valores sisteticos)
x_over, y_over = smote.fit_sample(X, y)

x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(x_over, y_over, test_size = 0.2, stratify = y_over)

modelo = RandomForestClassifier()
modelo.fit(x_treinamento, y_treinamento)

previsoes = modelo.predict(x_teste)

from sklearn.metrics import accuracy_score
print(accuracy_score(previsoes, y_teste))