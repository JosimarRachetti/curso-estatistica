import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from scipy.stats import uniform

dados_uniformes = uniform.rvs(size=1000)

sns.displot(dados_uniformes)
plt.show()

dataset = pd.read_csv('credit_data.csv')
dataset.dropna(inplace=True)
print(dataset.shape)

X = dataset.iloc[:, 1:4].values

y = dataset.iloc[:, 4].values


from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

resultados_naive_bayes = []
for i in range(30):
    X_treinamento,X_teste, y_treinamento, y_teste = train_test_split(X, y, test_size=0.2, stratify=y, random_state=1)
    naive_bayes = GaussianNB()
    naive_bayes.fit(X_treinamento, y_treinamento)
    resultados_naive_bayes.append(accuracy_score(y_teste, naive_bayes.predict(X_teste)))

print(resultados_naive_bayes)
sns.displot(resultados_naive_bayes, bins=2)
plt.show()