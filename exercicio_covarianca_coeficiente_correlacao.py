import pandas as pd
import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt


dataset = pd.read_csv('house_prices.csv')

#removendo atributos que nao serao utilizados para analise
dataset.drop(labels = ['id', 'date', 'sqft_living15', 'sqft_lot15'], axis=1, inplace=True)

#print(dataset.head())

#correlaçao de um atributo com os demais
print(dataset.corr())

#grafico de correlacao
sns.scatterplot(dataset['sqft_living'], dataset['price'])
#plt.show()

#grafico de correlacao
sns.scatterplot(dataset['bathrooms'], dataset['price'])
#plt.show()

sns.heatmap(dataset.corr(), annot=True)
plt.show()