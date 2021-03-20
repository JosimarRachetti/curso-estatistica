import pandas as pd
import numpy as np
import statistics
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score, KFold

dataset = pd.read_csv('credit_data.csv')
dataset.dropna(inplace=True)

X = dataset.iloc[:, 1:4].values
y = dataset.iloc[:, 4].values

min(X[0]), max(X[0])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)


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

resultados_naive_bayes = np.array(resultados_naive_bayes_cv)
resultado_logistica = np.array(resultado_logistica_cv)
resultados_forest = np.array(resultados_forest_cv)

resultados_naive_bayes_mean, resultado_logistica_mean, resultados_forest_mean = resultados_naive_bayes.mean(), resultado_logistica.mean(), resultados_forest.mean()

resultados = [resultados_naive_bayes, resultado_logistica, resultados_forest]

#testes nao parametricos
#testes de Wilcoxon
alpha = 0.05
_, p = stats.wilcoxon(resultados_naive_bayes, resultado_logistica)
print("diferença estatistica naive bayes com logistica: " + str(p))
_, p = stats.wilcoxon(resultados_naive_bayes, resultados_forest)
print("diferença estatistica naive bayes com forest: " + str(p))
_, p = stats.wilcoxon(resultados_forest, resultado_logistica)
print("diferença estatistica forest com logistica: " + str(p))

#Testes de Friedman
alpha = 0.05
_, p = stats.friedmanchisquare(resultados_naive_bayes, resultado_logistica, resultados_forest)
print("diferença estatistica naive bayes, logistica, forest: " + str(p))