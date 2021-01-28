import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from scipy.stats import skewnorm

from scipy.stats import bernoulli

dados_bernoulli = bernoulli.rvs(size=1000, p=0.5)
print(dados_bernoulli)
print(np.unique(dados_bernoulli, return_counts=True))

sns.displot(dados_bernoulli)
plt.show()