from imblearn.over_sampling import SMOTE
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import seaborn as sns
import numpy as np


dataset = pd.read_csv('credit_data.csv')
print(dataset.shape)

dataset.dropna(inplace=True)

x = dataset.iloc[:, 1:4].values
y = dataset.iloc[:, 4].values

smote = SMOTE(sampling_strategy='minority')
# gerando amostra com tecnica de sobreamostragem (criando valores sisteticos)
x_over, y_over = smote.fit_sample(x, y)

x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(x_over, y_over, test_size = 0.2, stratify = y_over)

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