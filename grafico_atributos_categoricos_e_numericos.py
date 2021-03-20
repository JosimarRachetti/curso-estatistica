import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


dataset = pd.read_csv('census.csv')

sns.catplot(x='income', y='hour-per-week', data=dataset, hue='sex')
plt.show()

sns.catplot(x='income', y='hour-per-week', data=dataset.query('age < 30'), hue='sex')
plt.show()