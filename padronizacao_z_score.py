import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler


#padronizar é equilabrar o desvio padrao da amostra, evitando dar erros nas previsões do algoritmo

dataset = pd.read_csv('credit_data.csv')
dataset.dropna(inplace=True)
dataset.head()


# sem padronizacao

X = dataset.iloc[:, 1:4].values
y = dataset['c#default'].values
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y, test_size=0.2, stratify=y)

media = np.mean(X_treinamento[0])
mediana = np.median(X_treinamento[0])
desvio_padrao = np.std(X_treinamento[0])

print(media, mediana, desvio_padrao)

knn = KNeighborsClassifier()
knn.fit(X_treinamento, y_treinamento)
previsoes = knn.predict(X_teste)
print(accuracy_score(y_teste, previsoes))

#com padronizacao
z_score_treinamento = StandardScaler()
z_score_teste = StandardScaler()

X_treinamento_p = z_score_treinamento.fit_transform(X_treinamento)
X_teste_p = z_score_teste.fit_transform(X_teste)

media = np.mean(X_treinamento_p[0])
mediana = np.median(X_treinamento_p[0])
desvio_padrao = np.std(X_treinamento_p[0])

print(media, mediana, desvio_padrao)

media_teste = np.mean(X_teste_p)
mediana_teste = np.median(X_teste_p)
desvio_padrao_teste = np.std(X_teste_p)

print(media_teste, mediana_teste, desvio_padrao_teste)

knn = KNeighborsClassifier()
knn.fit(X_treinamento_p, y_treinamento)
previsoes = knn.predict(X_teste_p)
print(accuracy_score(y_teste, previsoes))
