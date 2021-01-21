import pandas as pd
import numpy as np
import stats
import statistics
dataset = pd.read_csv('credit_data.csv')

print(dataset.isnull().sum())

media = dataset['age'].mean()
mediana = dataset['age'].median()

# substituindo valores nulls pela media
dataset['age'] = dataset['age'].replace(to_replace=np.nan, value=media)

dataset = pd.read_csv('autos.csv', encoding='ISO-8859-1')

print(dataset.isnull().sum())

print(dataset['fuelType'].unique())

print(statistics.mode(dataset['fuelType']))
moda = statistics.mode(dataset['fuelType'])

dataset['fuelType'] = dataset['fuelType'].replace(to_replace= np.nan, value = statistics.mode(dataset['fuelType']))

print(dataset['fuelType'].unique())