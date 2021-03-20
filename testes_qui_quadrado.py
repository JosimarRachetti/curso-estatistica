import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from scipy.stats import chi2_contingency

#O teste do qui quadrado é utilizado para verificar se os resultados de um amostra foi ao acaso ou se realmente representou uma mudança estatistica dada a ultima pesquisa

tabela = np.array([30, 20], [22, 28])

print(tabela.shape)

_, p, _, _ = chi2_contingency(tabela)

alpha = 0.05

if p <= alpha:
    print("hipotese nula rejeitada")
else:
    print("hipotese alternativa rejeitada")