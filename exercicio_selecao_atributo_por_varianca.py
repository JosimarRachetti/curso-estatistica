import numpy as np
import pandas as pd
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import MinMaxScaler

dataset = pd.read_csv('credit_data.csv')

dataset.dropna(inplace=True)

print(dataset.describe())

X = dataset.iloc[:, 1:4].values

y = dataset.iloc[:, 4].values

scaler = MinMaxScaler()
X = scaler.fit_transform(X)

selecao = VarianceThreshold(threshold=0.07)
atributos_valor_maior_007 = selecao.fit_transform(X)

print(atributos_valor_maior_007)