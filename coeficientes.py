import pandas as pd
import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt

tamanho = np.array([30, 39, 49, 60])
preco = np.array([57000, 69000, 77000, 90000])

dataset = pd.DataFrame({'tamanho': tamanho, 'preço': preco})
print(dataset)

media_preco = dataset["preço"].mean()
media_tamanho = dataset["tamanho"].mean()

print("media tamanho : " + str(media_tamanho) + " media preco: " + str(media_preco))

dp_preco = dataset["preço"].std()
dp_tamanho = dataset["tamanho"].std()

print("desvio padrao tamanho : " + str(dp_tamanho) + " desvio padrao preco: " + str(dp_preco))


#calculo manual de correlação

dataset['dif'] = (dataset['tamanho'] - media_tamanho) * (dataset['preço'] - media_preco)

print(dataset['dif'])

soma_dif = dataset['dif'].sum()

print("soma dif: " + str(soma_dif))


#Calculo da covarianca

covarianca = soma_dif /(len(dataset) - 1)

print("Covarianca: " + str(covarianca))

#Coeficiente de correlaçao

coeficiente_de_correlacao = covarianca / (dp_tamanho * dp_preco)

print("Coeficiente de correlacao: " +  str(coeficiente_de_correlacao))

sns.scatterplot(tamanho, preco)
plt.show()

#coeficiente de determinacao

coeficiente_de_determinacao = pow(coeficiente_de_correlacao, 2)
print("Coeficiente de determinacao: " + str(coeficiente_de_determinacao))

#utilizando np para realizar os calculos

covarianca_np = np.cov(tamanho, preco)

coeficiente_de_correlacao_cp = np.corrcoef(tamanho, preco)
