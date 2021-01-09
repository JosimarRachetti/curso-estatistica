import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import random
import numpy as np


dataset = pd.read_csv('credit_data.csv')
print(dataset.shape)

# apaga linhas com dados invalidos
dataset.dropna(inplace=True)

print(dataset.shape)
# cria uma gráfico dos dados de c#default
# sns.countplot(dataset['c#default'])
# mostra o gráfico em uma imagem
# print(plt.show())

x = dataset.iloc[:, 1:4].values

print(x.shape)

y = dataset.iloc[:, 4].values

print(y)
# dividindo as porções em bases de treinamento e de testes
x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(x, y, test_size = 0.2, stratify = y)

# conferindo se a estratificação foi feita corretamente

print(np.unique(y, return_counts=True))
print(283/len(dataset))
print(np.unique(y_treinamento, return_counts=True))
print(226/len(y_treinamento))
print(np.unique(y_teste, return_counts=True))
print(57/len(y_teste))

modelo = GaussianNB()
# treinamento do algoritimo com dados
modelo.fit(x_treinamento, y_treinamento)

# previsoes geradas pelo algoritmo
previsoes = modelo.predict(x_teste)

# verificando a acuracidade do algoritmo
from sklearn.metrics import accuracy_score, confusion_matrix

print(accuracy_score(previsoes, y_teste))
cm = confusion_matrix(previsoes, y_teste)
print(cm)
sns.heatmap(cm, annot=True)
plt.show()

