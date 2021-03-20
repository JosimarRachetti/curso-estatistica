import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

#os calculos para distribuiçao t são recomendados para amostrar com quantidades abaixo de 30
dados = np.array([149, 160, 147, 189, 175, 168, 156, 160, 152])

n = len(dados)
media = dados.mean()
desvio_padrao = dados.std()


intervalos = stats.t.interval(0.95, n - 1, media, stats.sem(dados, ddof=0))

margem_erro = media - intervalos[0]

print(intervalos)
print(margem_erro)