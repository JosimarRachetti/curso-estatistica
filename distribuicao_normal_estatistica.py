import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

# distribuição normal também é chamada de gaussian distribution

dados_normal = stats.norm.rvs(size = 1000)

print(max(dados_normal), min(dados_normal))

sns.displot(dados_normal, kde=True)
plt.show()

media = dados_normal.mean()
mediana = np.median(dados_normal)
moda = stats.mode(dados_normal)
varianca = np.var(dados_normal)
desvio_padrao = np.std(dados_normal)

print(media, mediana, moda, varianca, desvio_padrao)
