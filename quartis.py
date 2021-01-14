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
dados_impar = [150, 151, 152, 152, 153, 154, 155, 155, 155]

pos_mediana = math.ceil(len(dados_impar)/2)
mediana = dados_impar[pos_mediana-1]


# calculo sem bibliotecas
posicao_mediana = math.floor(len(dados_impar) / 2)
esquerda = dados_impar[0: posicao_mediana]
print("resultado sem biblioteca: ")

quartil_um = np.median(esquerda)
print(quartil_um)

quartil_dois = np.median(dados_impar)
print(quartil_dois)

direta = dados_impar[posicao_mediana + 1:]
quartil_tres = np.median(direta)
print(quartil_tres)

# calculo utilizando biblioteca
#numpy
print("resultado com bibliotecas numpy: ")
quartil_um = np.quantile(dados_impar, 0.25)
quartil_dois = np.quantile(dados_impar, 0.50)
quartil_tres = np.quantile(dados_impar, 0.75)

print(quartil_um)
print(quartil_dois)
print(quartil_tres)

quartil_um = np.quantile(dados, 0.25)
quartil_dois = np.quantile(dados, 0.50)
quartil_tres = np.quantile(dados, 0.75)

print(quartil_um)
print(quartil_dois)
print(quartil_tres)

#scipy
print("resultado com biblioteca scipy: ")
quartil_um = stats.scoreatpercentile(dados, 25)
quartil_dois = stats.scoreatpercentile(dados, 50)
quartil_tres = stats.scoreatpercentile(dados, 75)

print(quartil_um)
print(quartil_dois)
print(quartil_tres)

#pandas
print("resultado com panda: ")
dataset = pd.DataFrame(dados)

print(dataset.quantile([0.25, 0.50, 0.75]))