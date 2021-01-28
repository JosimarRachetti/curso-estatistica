import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from scipy.stats import skewnorm

# quanto maior o tamanho da amostra a distribuiçao amostral será cada vez mais normal.

medias = [np.mean(np.random.randint(126, 129, 500)) for _ in range(1000)]

sns.displot(medias)
plt.show()