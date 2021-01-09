import numpy as np
import statistics
from scipy import stats
import math

dados = np.array([150, 151, 152, 152, 153, 154, 155, 155, 155, 155, 156, 156, 156,
                  157, 158, 158, 160, 160, 160, 160, 160, 161, 161, 161, 161, 162,
                  163, 163, 164, 164, 164, 165, 166, 167, 168, 168, 169, 170, 172,
                  173])


# retirando a média

media = dados.sum()/len(dados)

# usando np

media_np = dados.mean()

# usando statistics

media_statistics = statistics.mean(dados)

print(media)

# retirando a moda

# usando statistics

moda = statistics.mode(dados)

print(moda)

# usando stats

print(stats.mode(dados))

# retirando a mediana

dados_impar = [150, 151, 152, 152, 153, 154, 155, 155, 155]

#
posicao = len(dados_impar)/2
posicao = math.ceil(posicao)
mediana = dados_impar[posicao - 1]

posicao_par = len(dados)//2
mediana_par = (dados[posicao - 1] + dados[posicao]) / 2


# utilizando np

mediana_impar_np = np.median(dados_impar)
mediana_par_np = np.median(dados)

# utilizando statistics

mediana_impar_statis = statistics.median(dados_impar)
mediana_par_statis = statistics.median(dados)
