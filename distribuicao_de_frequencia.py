import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


dados_ = np.array([160, 165, 167, 164, 160, 166, 160, 161, 150, 152, 173, 160, 155,
                  164, 168, 162, 161, 168, 163, 156, 155, 169, 151, 170, 164,
                  155, 152, 163, 160, 155, 157, 156, 158, 158, 161, 154, 161, 156, 172, 153])

# ordenando dados
dados = np.sort(dados_)
# dado min
minino = dados.min()
# dado maximo
maximo = dados.max()
# quantidade de cada elemento
qtd_elementos = np.unique(dados, return_counts=True)

n = len(dados)

# quantidade de classes na distribuição

i = 1 + 3.3 * np.log10(n)
i = round(i)

# amplitude do intervalo

AA = maximo - minino
h = AA / i

import math

h = math.ceil(h)

#  costrução distribuição de frequencia

intervalos = np.arange(minino, maximo + 2, step = h)

intervalo1, intervalo2, intervalo3, intervalo4, intervalo5, intervalo6 = 0, 0, 0, 0, 0, 0

for i in range(n):
    if intervalos[0] <= dados[i] < intervalos[1]:
        intervalo1 += 1
    elif intervalos[1] <= dados[i] < intervalos[2]:
        intervalo2 += 1
    elif intervalos[2] <= dados[i] < intervalos[3]:
        intervalo3 += 1
    elif intervalos[3] <= dados[i] < intervalos[4]:
        intervalo4 += 1
    elif intervalos[4] <= dados[i] < intervalos[5]:
        intervalo5 += 1
    elif intervalos[5] <= dados[i] < intervalos[6]:
        intervalo6 += 1

lista_intervalos = [intervalo1, intervalo2, intervalo3, intervalo4, intervalo5, intervalo6]


lista_classes = []
for i in range(len(lista_intervalos)):
    lista_classes.append(str(intervalos[i]) + '-' + str(intervalos[i+1]))

# criando gráfico
# plt.bar(lista_classes, lista_intervalos)
# plt.title("Distribuição frequencia")
# plt.xlabel('intervalos')
# plt.ylabel('valores')
# plt.show()

# criando distribuicao usando bibliotecas python numpy e matplotlib

# frequencia, classes = np.histogram(dados, bins=5)
# plt.hist(dados, bins=classes)
# plt.show()

# criando distribuicao usando bibliotecas python pandas

dataset = pd.DataFrame({'dados': dados_})

print(dataset.head())

dataset.plot.hist()
sns.displot(dados_, kind='kde')
plt.show()