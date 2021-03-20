import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


dataset = pd.read_csv('census.csv')

sns.boxplot(dataset['age'])
plt.show()

sns.boxplot(dataset['education-num'])
plt.show()

dataset2 = dataset.iloc[:, [0, 4, 12]]
sns.boxplot(data=dataset2)
plt.show()