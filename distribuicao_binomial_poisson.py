import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from scipy.stats import skewnorm

from scipy.stats import binom, poisson

dados_binomial = binom.rvs(size=1000, n=2, p=0.5)

print(dados_binomial)
print(np.unique(dados_binomial, return_counts=True))

sns.displot(dados_binomial)
plt.show()

dados_poisson = poisson.rvs(size=1000, mu=5)

sns.displot(dados_poisson)
plt.show()