import pandas as pd
import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt
from yellowbrick.target import FeatureCorrelation

dataset = pd.read_csv('house_prices.csv')

#removendo atributos que nao serao utilizados para analise
dataset.drop(labels=['id', 'date', 'sqft_living15', 'sqft_lot15'], axis=1, inplace=True)

print(dataset.columns)

grafico = FeatureCorrelation(labels=dataset.columns[1:])
grafico.fit(dataset.iloc[:, 1:16].values, dataset.iloc[:, 0].values)
plt.show()