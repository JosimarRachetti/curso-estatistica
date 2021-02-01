import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from scipy.stats import skewnorm

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
# o multinomial trabalha com atributos que possuem varias categorias ex: estado civel (solteiro, casado, divorciado e etc)

dataset = pd.read_csv("census.csv")

#mas para fazer o calculo preciso transformar de categoria para discreto, ou seja numeros

label_encoder_1 = LabelEncoder()
label_encoder_2 = LabelEncoder()
label_encoder_3 = LabelEncoder()
label_encoder_4 = LabelEncoder()
label_encoder_5 = LabelEncoder()
label_encoder_6 = LabelEncoder()
label_encoder_7 = LabelEncoder()

dataset["workclass"] = label_encoder_1.fit_transform(dataset["workclass"])
dataset["education"] = label_encoder_2.fit_transform(dataset["education"])
dataset["marital-status"] = label_encoder_3.fit_transform(dataset["marital-status"])
dataset["occupation"] = label_encoder_4.fit_transform(dataset["occupation"])
dataset["relationship"] = label_encoder_5.fit_transform(dataset["relationship"])
dataset["race"] = label_encoder_6.fit_transform(dataset["race"])
dataset["native-country"] = label_encoder_7.fit_transform(dataset["native-country"])

X = dataset.iloc[:, [1, 3, 5, 6, 7, 8, 13]]
y = dataset["income"].values

multinomial_naive_bayes = MultinomialNB()
multinomial_naive_bayes.fit(X, y)
MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)

previsoes = multinomial_naive_bayes.predict(X)

print(previsoes, y)
print(accuracy_score(previsoes, y))