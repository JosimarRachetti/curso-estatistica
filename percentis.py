from scipy.stats.mstats import gmean
from scipy.stats.mstats import hmean
from scipy import stats
import numpy as np
import statistics
import math
import pandas as pd

dados = np.array([150, 151, 152, 152, 153, 154, 155, 155, 155, 155, 156, 156, 156,
                  157, 158, 158, 160, 160, 160, 160, 160, 161, 161, 161, 161, 162,
                  163, 163, 164, 164, 164, 165, 166, 167, 168, 168, 169, 170, 172,
                  173])

#numpy
print("resultados com np: ")
percentil_com_cinco = np.percentile(dados, 5)
percentil_com_dez = np.percentile(dados, 10)
percentil_com_noventa = np.percentile(dados, 90)

print(percentil_com_cinco)
print(percentil_com_dez)
print(percentil_com_noventa)

#scipy
print("resultados com stats: ")
percentil_com_cinco = stats.scoreatpercentile(dados, 5)
percentil_com_dez = stats.scoreatpercentile(dados, 10)
percentil_com_noventa = stats.scoreatpercentile(dados, 90)

print(percentil_com_cinco)
print(percentil_com_dez)
print(percentil_com_noventa)

#pandas

print("resultado com panda: ")
dataset = pd.DataFrame(dados)

print(dataset.quantile([0.05, 0.10, 0.90]))