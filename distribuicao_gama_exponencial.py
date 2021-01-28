import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from scipy.stats import skewnorm

from scipy.stats import gamma, expon

dados_gama = gamma.rvs(a=4, size=1000)
sns.displot(dados_gama)
plt.show()

dados_expon = expon.rvs(size=1000)
sns.displot(dados_expon)
plt.show()
