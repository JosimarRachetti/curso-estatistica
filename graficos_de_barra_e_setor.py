import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv('census.csv')
dataset.head()

sns.barplot(x='sex', y="final-weight", data=dataset, hue='income')
plt.show()

#agrupando pessoas pela renda, e fazendo somatorio de anos estudados
dados_agrupados = dataset.groupby(['income'])['education-num'].sum()
#gerando grafico de pizza
dados_agrupados.plot.pie()
plt.show()