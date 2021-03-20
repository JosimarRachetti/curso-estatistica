import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats


#segue as mesmas regras dos testes de hipotese Z porem é indicado para dados com quantidade menor que 30

dados_originais = np.array([149., 160., 147., 189., 175., 168., 156., 160., 152.])

media_dados_originais = dados_originais.mean()
desvio_padrao_dados_originais = dados_originais.std()

dados_novos = dados_originais * 1.02

media_dados_novos = dados_novos.mean()
desvio_padrao_dados_novos = dados_novos.std()

from scipy.stats import ttest_rel

_, p = ttest_rel(dados_originais, dados_novos)

print(p)

alpha = 0.01

if p < alpha:
    print('Hipotese nula (0) rejeitada')
else:
    print('Hipotese nova (1) rejeitada')