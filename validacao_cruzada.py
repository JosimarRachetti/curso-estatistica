from sklearn.model_selection import cross_val_score, KFold
from scipy import stats
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

dataset = pd.read_csv('credit_data.csv')
dataset.dropna(inplace=True)


X = dataset.iloc[:, 1:4].values
print(X)

y = dataset.iloc[:, 4].values
print(y)

resultados_naive_bayes_cv = []
resultado_logistica_cv = []
resultados_forest_cv = []

for i in range(30):
    kfold = KFold(n_splits=10, shuffle=True, random_state=i)

    naive_bayes = GaussianNB()
    scores = cross_val_score(naive_bayes, X, y, cv=kfold)
    resultados_naive_bayes_cv.append(scores.mean())

    logistica = LogisticRegression()
    scores = cross_val_score(logistica, X, y, cv=kfold)
    resultado_logistica_cv.append(scores.mean())

    random_forest = RandomForestClassifier()
    scores = cross_val_score(random_forest, X, y, cv=kfold)
    resultados_forest_cv.append(scores.mean())

print(resultados_naive_bayes_cv)
print(resultado_logistica_cv)
print(resultados_forest_cv)

resultados_naive_bayes = np.array(resultados_naive_bayes_cv)
resultado_logistica = np.array(resultado_logistica_cv)
resultados_forest = np.array(resultados_forest_cv)

media_naive_bayes = resultados_naive_bayes.mean()
media_logistica = resultado_logistica.mean()
media_forest = resultados_forest.mean()

print("media valores")
print(media_naive_bayes)
print(media_logistica)
print(media_forest)

moda_naive_bayes = stats.mode(resultados_naive_bayes)
moda_logistica = stats.mode(resultado_logistica)
moda_forest = stats.mode(resultados_forest)

print("moda valores")
print(moda_naive_bayes)
print(moda_logistica)
print(moda_forest)

mediana_naive_bayes = np.median(resultados_naive_bayes)
mediana_logistica = np.median(resultado_logistica)
mediana_forest = np.median(resultados_forest)

print("mediana valores")
print(mediana_naive_bayes)
print(mediana_logistica)
print(mediana_forest)

varianca_naive_bayes = np.var(resultados_naive_bayes)
varianca_logistica = np.var(resultado_logistica)
varianca_forest = np.var(resultados_forest)

print("varianca valores")
print(varianca_naive_bayes)
print(varianca_logistica)
print(varianca_forest)

desvio_padrao_naive_bayes = np.std(resultados_naive_bayes)
desvio_padrao_logistica = np.std(resultado_logistica)
desvio_padrao_forest = np.std(resultados_forest)

print("desvio padrão valores")
print(desvio_padrao_naive_bayes)
print(desvio_padrao_logistica)
print(desvio_padrao_forest)

coeficiente_variacao_naive_bayes = stats.variation(resultados_naive_bayes) * 100
coeficiente_variacao_logistica = stats.variation(resultado_logistica) * 100
coeficiente_variacao_forest = stats.variation(resultados_forest) * 100

print("coeficiente variacao valores")
print(coeficiente_variacao_naive_bayes)
print(coeficiente_variacao_logistica)
print(coeficiente_variacao_forest)
