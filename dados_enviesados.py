import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from scipy.stats import skewnorm

dado_enviesados_positivo = skewnorm.rvs(a=10, size=1000)
sns.displot(dado_enviesados_positivo, kde=True)
plt.show()

media = dado_enviesados_positivo.mean()
mediana = np.median(dado_enviesados_positivo)
moda = stats.mode(dado_enviesados_positivo)

print(media, mediana, moda)

dado_enviesados_negativo = skewnorm.rvs(a=-10, size=1000)
sns.displot(dado_enviesados_negativo, kde=True)
plt.show()

media = dado_enviesados_negativo.mean()
mediana = np.median(dado_enviesados_negativo)
moda = stats.mode(dado_enviesados_negativo)

print(media, mediana, moda)