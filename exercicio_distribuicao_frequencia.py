import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dataset = pd.read_csv('census.csv')

dados = dataset['age']

print(dados.min(), dados.max())

dados.plot.hist()
plt.show()

frequencia, classes = np.histogram(dados, bins=5)
print(frequencia, classes)
plt.hist(dados, bins=classes)

# print(dados.head())
# dataset.plot.hist()
# sns.displot(dados)
# plt.show()