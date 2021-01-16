import pandas as pd
import math
dados = {'inferior': [150, 154, 158, 162, 166, 170],
         'superior': [154, 158, 162, 166, 170, 174],
         'fi': [ 5, 9, 11, 7, 5, 3]}


dataset = pd.DataFrame(dados)
dataset['xi'] = (dataset['superior'] + dataset['inferior']) / 2

dataset['fi.xi'] = dataset['fi'] * dataset['xi']
frequencia_acumulada = []
somatorio = 0
for linha in dataset.iterrows():
    somatorio += linha[1][2]
    frequencia_acumulada.append(somatorio)

dataset['Fi'] = frequencia_acumulada

print(dataset)

dataset['xi_2'] = dataset['xi'] * dataset['xi']

print(dataset)

dataset['fi_xi_2'] = dataset['fi'] * dataset['xi_2']

colunas_ordenadas = ['inferior', 'superior', 'fi', 'xi', 'fi.xi', 'xi_2', 'fi_xi_2', 'Fi']

dataset = dataset[colunas_ordenadas]

desvio_padrao_dados_agrupados = math.sqrt(dataset['fi_xi_2'].sum()/ dataset['fi'].sum() - math.pow(dataset['fi.xi'].sum() / dataset['fi'].sum(), 2))

print(desvio_padrao_dados_agrupados)