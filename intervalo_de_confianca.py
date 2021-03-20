import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import math

#caso com distribuição normal
dados = np.array([126. , 129.5, 133. , 133. , 136.5, 136.5, 140. , 140. , 140. ,
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



#abaixo estao calculados o limite inferior e superior dos intervalos de confiança de uma amostra de dados
n = len(dados)
media = dados.mean()
desvio_padrao = dados.std()


alpha = 0.05 / 2

print(alpha)

z = stats.norm.ppf(1 - alpha)

limite_x_inferior = media - z * (desvio_padrao / math.sqrt(n))

print(limite_x_inferior)

limite_x_superior = media + z * (desvio_padrao / math.sqrt(n))

print(limite_x_superior)

margem_erro = abs(media - limite_x_superior)

print(margem_erro)
