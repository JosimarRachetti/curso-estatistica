import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from apyori import apriori

dataset = pd.read_csv('census.csv')

dados = dataset['age']
dataset['age'] = pd.cut(dataset['age'], bins=[0, 17, 25, 40, 60, 90], labels=['faixa1','faixa2','faixa3','faixa4', 'faixa5'])

dataset_apriori = dataset[['age','workclass','education', 'marital-status','relationship','occupation','sex','native-country','income']]

dataset_apriori = dataset_apriori.sample(n = 1000)

transacoes = []

for i in range(dataset_apriori.shape[0]):
    transacoes.append([str(dataset_apriori.values[i, j]) for j in range(dataset_apriori.shape[1])])

regras = apriori(transacoes, min_support=0.3, min_confidence=0.2)
resultados = list(regras)

print(resultados)