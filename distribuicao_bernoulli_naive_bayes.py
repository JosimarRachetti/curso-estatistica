import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from scipy.stats import skewnorm

from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score

dataset = pd.read_csv("census.csv")

# relembrando distribuicao bernoulli é composta por duas opções apenas, 0 e 1, masculino e feminino, etc...

print(dataset['sex'].unique())

X = dataset['sex'].values

from sklearn.preprocessing import LabelEncoder

# para trabalhar com bernoulli transformamos valores categoricos em numero Ex: mulher = 0 e homem = 1
label_encoder = LabelEncoder()
X = label_encoder.fit_transform(X)
sns.displot(X, kde=False)
plt.show()

X = X.reshape(-1, 1)

y = dataset['income'].values

bernoulli_naive_bayes = BernoulliNB()
bernoulli_naive_bayes.fit(X, y)
previsoes = bernoulli_naive_bayes.predict(X)
print(previsoes, y)
print(accuracy_score(y, previsoes))