import numpy as np
from scipy.stats import f

grupo_a = np.array([165, 152, 143, 140, 155])
grupo_b = np.array([130, 169, 164, 143, 154])
grupo_c = np.array([163, 158, 154, 149, 156])

f.ppf(1 - 0.5, dfn=2, dfd=12)

from scipy.stats import f_oneway

_, p = f_oneway(grupo_a, grupo_b, grupo_c)

print(p)

alpha = 0.05

if p <= alpha:
    print("hipotese nula rejeitada")
else:
    print("hipotese alternativa rejeitada")


#Teste de Tukey

dados = {"valores": [165, 152, 143, 140, 155, 130, 169, 164, 143, 154, 163, 158, 154, 149, 156],
         "grupo": ['A','A','A','A','A','B','B','B','B','B','C','C','C','C','C']}

import pandas as pd

dados_pd = pd.DataFrame(dados)

print(dados_pd)

from statsmodels.stats.multicomp import MultiComparison

compara_grupos = MultiComparison(dados_pd['valores'], dados_pd['grupo'])

teste = compara_grupos.tukeyhsd()

print(teste)
