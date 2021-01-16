from scipy.stats.mstats import gmean
from scipy.stats.mstats import hmean
import numpy as np
import statistics
import math
from scipy import stats

dados_impar = np.array([150, 151, 152, 152, 153, 154, 155, 155, 155])

media = dados_impar.sum() / len(dados_impar)

desvio = abs(dados_impar - media)

desvio = desvio ** 2

print(desvio)

soma_desvio = desvio.sum()

varianca = soma_desvio / len(dados_impar)

print(varianca)

varianca = statistics.variance(dados_impar)

print(varianca)

varianca = np.var(dados_impar)

print(varianca)



desvio_padrao = math.sqrt(varianca)

print(desvio_padrao)

desvio_padrao = np.std(dados_impar)

print(desvio_padrao)


coeficiente_variacao = (desvio_padrao/media) * 100

print(coeficiente_variacao)

coeficiente_variacao = stats.variation(dados_impar) * 100

print(coeficiente_variacao)
