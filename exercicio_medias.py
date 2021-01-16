import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from media_geometrica_harmonica_quadratica import quadratic_mean
from scipy.stats.mstats import gmean
from scipy.stats.mstats import hmean
import numpy as np
import statistics
import math

dataset = pd.read_csv('census.csv')

dados = dataset['age']

media = sum(dados) / len(dados)
mediana = dados.median()
moda = statistics.mode(dados)

media_harmonica = hmean(dados)
media_geometrica = gmean(dados)
media_quadratica = quadratic_mean(dados)


print(media)
print(mediana)
print(moda)
print(media_harmonica)
print(media_geometrica)
print(media_quadratica)