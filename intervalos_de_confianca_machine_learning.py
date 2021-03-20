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

resultados_naive_bayes_cv = []
resultados_naive_bayes_cv_300 = []

resultado_logistica_cv = []
resultado_logistica_cv_300 = []

resultados_forest_cv = []
resultados_forest_cv_300 = []

for i in range(30):
    kfold = KFold(n_splits=10, shuffle=True, random_state=i)

    naive_bayes = GaussianNB()
    scores = cross_val_score(naive_bayes, X, y, cv=kfold)
    resultados_naive_bayes_cv_300.append(scores)
    resultados_naive_bayes_cv.append(scores.mean())

    logistica = LogisticRegression()
    scores = cross_val_score(logistica, X, y, cv=kfold)
    resultados_forest_cv_300.append(scores)
    resultado_logistica_cv.append(scores.mean())

    random_forest = RandomForestClassifier()
    scores = cross_val_score(random_forest, X, y, cv=kfold)
    resultados_forest_cv_300.append(scores)
    resultados_forest_cv.append(scores.mean())


resultados_naive_bayes = np.array(resultados_naive_bayes_cv)
resultados_naive_bayes_cv_300 = np.array(np.asarray(resultados_naive_bayes_cv_300).reshape(-1))
resultado_logistica = np.array(resultado_logistica_cv)
resultado_logistica_cv_300 = np.array(np.asarray(resultados_naive_bayes_cv_300).reshape(-1))
resultados_forest = np.array(resultados_forest_cv)
resultados_forest_cv_300 = np.array(np.asarray(resultados_forest_cv_300).reshape(-1))


from scipy import stats

intervalos_naive_bayes_t = stats.t.interval(0.95, len(resultados_naive_bayes) - 1, resultados_naive_bayes.mean(), stats.sem(resultados_naive_bayes, ddof = 0))

print(abs(resultados_naive_bayes.mean()-intervalos_naive_bayes_t[1]))

intervalos_naive_bayes_n = stats.norm.interval(0.95, resultados_naive_bayes_cv_300.mean(),
                                               stats.sem(resultados_naive_bayes_cv_300))

print(abs(resultados_naive_bayes_cv_300.mean() - intervalos_naive_bayes_n[1]))

intervalos_logistica_t = stats.t.interval(0.95, len(resultado_logistica) - 1, resultado_logistica.mean(), stats.sem(resultado_logistica, ddof = 0))

print(abs(resultado_logistica.mean() - intervalos_logistica_t[1]))

intervalos_logistica_n = stats.norm.interval(0.95, resultado_logistica_cv_300.mean(),
                                             stats.sem(resultado_logistica_cv_300))

print(abs(resultado_logistica_cv_300.mean() - intervalos_logistica_n[1]))

intervalos_florest_t = stats.t.interval(0.95, len(resultados_forest) - 1, resultados_forest.mean(), stats.sem(resultados_forest, ddof = 0))

print(abs(resultados_forest.mean() - intervalos_florest_t[1]))

intervalos_florest_n = stats.norm.interval(0.95, resultados_forest_cv_300.mean(),
                                           stats.sem(resultados_forest_cv_300))

print(abs(resultados_forest_cv_300.mean() - intervalos_florest_n[1]))

