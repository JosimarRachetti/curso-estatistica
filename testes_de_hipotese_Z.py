#teste de hipotese Z é utilizada para contrapor uma hipotese
# H0 ou hipotese nula é a hipotese atual q ja existe ex: media de preço de um produto
# H1 é a hipotese que contrapoe a hipotese nula, um novo valor que se quer provar ser o correto

#existe dois tipos de erro no hipotese
# tipo um quando a H1 é errada mas foi considerada vdd
# tipo dois quando a H1 é correta mas foi considerada errada

import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats


#caso com distribuição normal
dados_originais = np.array([126. , 129.5, 133. , 133. , 136.5, 136.5, 140. , 140. , 140. ,
                  140. , 143.5, 143.5, 143.5, 143.5, 143.5, 143.5, 147. , 147. ,
                  147. , 147. , 147. , 147. , 147. , 150.5, 150.5, 150.5, 150.5,
                  150.5, 150.5, 150.5, 150.5, 154. , 154. , 154. , 154. , 154. ,
                  154. , 154. , 154. , 154. , 157.5, 157.5, 157.5, 157.5, 157.5,
                  157.5, 157.5, 157.5, 157.5, 157.5, 161. , 161. , 161. , 161. ,
                  161. , 161. , 161. , 161. , 161. , 161. , 164.5, 164.5, 164.5,
                  164.5, 164.5, 164.5, 164.5, 164.5, 164.5, 168. , 168. , 168. ,
                  168. , 168. , 168. , 168. , 168. , 171.5, 171.5, 171.5, 171.5,
                  171.5, 171.5, 171.5, 175. , 175. , 175. , 175. , 175. , 175. ,
                  178.5, 178.5, 178.5, 178.5, 182. , 182. , 185.5, 185.5, 189., 192.5])

H0_media = dados_originais.mean()
H0_desvio_padrao = dados_originais.std()


dados_novos = dados_originais * 1.03

H1_media = dados_novos.mean()
H1_desvio_padrao = dados_novos.std()

print(H1_media, H1_desvio_padrao)

H1_n = len(dados_novos)

alpha = 0.05

Z = (H1_media - H0_media) / (H1_desvio_padrao / math.sqrt(H1_n))
print(Z)

Z = stats.norm.cdf(Z)

p = 1 - Z

print(p)

if p < alpha:
    print('Hipotese nula (0) rejeitada')
else:
    print('Hipotese nova (1) rejeitada')