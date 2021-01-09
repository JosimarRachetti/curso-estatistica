import numpy as np
import statistics
from scipy import stats
import math

notas = np.array([9, 8, 7, 3])
pesos = np.array([1, 2, 3, 4])

# calculo

media_ponderada = (9 * 1 + 8 * 2 + 7 * 3 + 3 * 4) / (1 + 2 + 3 + 4)

print(media_ponderada)

# calculo direto nos arrays

media_ponderada = (notas * pesos).sum() / pesos.sum()

print(media_ponderada)

# usando numpy

np.average(notas, weights=pesos)