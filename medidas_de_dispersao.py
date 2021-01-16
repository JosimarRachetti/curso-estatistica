from scipy.stats.mstats import gmean
from scipy.stats.mstats import hmean
import numpy as np
import statistics
import math

dados = np.array([150, 151, 152, 152, 153, 154, 155, 155, 155, 155, 156, 156, 156,
                  157, 158, 158, 160, 160, 160, 160, 160, 161, 161, 161, 161, 162,
                  163, 163, 164, 164, 164, 165, 166, 167, 168, 168, 169, 170, 172,
                  173])


amplitude_total = dados.max() - dados.min()

q1 = np.quantile(dados, 0.25)
q3 = np.quantile(dados, 0.75)

diferenca_interquartil = q3-q1

outliners_inferior = q1 - ( 1.5 * diferenca_interquartil )
outliners_superior = q3 + ( 1.5 * diferenca_interquartil )

print(outliners_inferior)
print(outliners_superior)
print(diferenca_interquartil)
print(amplitude_total)