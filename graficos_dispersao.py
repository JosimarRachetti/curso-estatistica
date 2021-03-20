import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv('census.csv')
dataset.head()


sns.relplot(x = 'age', y = 'final-weight', data=dataset, hue='income', style='sex', size='education-num')
plt.show()