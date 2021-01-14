from scipy.stats.mstats import gmean
from scipy.stats.mstats import hmean
import numpy as np
import statistics
import math

dados = np.array([150, 151, 152, 152, 153, 154, 155, 155, 155, 155, 156, 156, 156,
                  157, 158, 158, 160, 160, 160, 160, 160, 161, 161, 161, 161, 162,
                  163, 163, 164, 164, 164, 165, 166, 167, 168, 168, 169, 170, 172,
                  173])


# media geometrica

print(gmean(dados))

# media harmonica

print(hmean(dados))

# media quadratica


def quadratic_mean(dados):
    return math.sqrt(sum(n * n for n in dados) / len(dados))


print(quadratic_mean(dados))