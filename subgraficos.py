import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


dataset = pd.read_csv('census.csv')

g = sns.FacetGrid(dataset, col = 'sex', hue='income')
g.map(sns.scatterplot, 'age', 'final-weight')

g = sns.FacetGrid(dataset, col = 'workclass', hue='income')
g.map(sns.scatterplot, 'age', 'final-weight')
plt.show()
