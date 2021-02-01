
from tensorflow.keras import initializers
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#inicializar os pesos de redes neurais

#distribuição normal
normal = initializers.RandomNormal()
dados_normal = normal(shape=[1000])
media = np.mean(dados_normal)
desvio_padrao = np.std(dados_normal)
print(media, desvio_padrao)
sns.displot(dados_normal)
plt.show()

#distribuição uniforma
uniforme = initializers.RandomUniform()
dados_uniforme = uniforme(shape=[1000])
sns.displot(dados_uniforme)
plt.show()