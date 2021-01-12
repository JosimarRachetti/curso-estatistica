import pandas as pd
dados = {'inferior': [150, 154, 158, 162, 166, 170],
         'superior': [154, 158, 162, 166, 170, 174],
         'fi': [ 5, 9, 11, 7, 5, 3]}


dataset = pd.DataFrame(dados)
print(dataset)

dataset['xi'] = (dataset['superior'] + dataset['inferior']) / 2

print(dataset)

dataset['fi.xi'] = dataset['fi'] * dataset['xi']

print(dataset)

frequencia_acumulada = []
somatorio = 0
for linha in dataset.iterrows():
    somatorio += linha[1][2]
    frequencia_acumulada.append(somatorio)


dataset['Fi'] = frequencia_acumulada

print(dataset)

# calculo media
media = dataset['fi.xi'].sum() / dataset['fi'].sum()
print(media)

# calculo moda
moda = dataset[dataset['fi'] == dataset['fi'].max()]['xi']
print(moda)

# calculo mediana
fi_2 = dataset['fi'].sum() / 2

limite_inferior, frequencia_classe, id_frequencia_anterior = 0, 0, 0
for linha in dataset.iterrows():
    limite_inferior = linha[1][0]
    frequencia_classe = linha[1][2]
    id_frequencia_anterior = linha[0]
    if linha[1][5] >= fi_2:
        id_frequencia_anterior -= 1
        break

Fi_anterior = dataset.iloc[[id_frequencia_anterior]]['Fi'].values[0]

mediana = limite_inferior + ((fi_2 - Fi_anterior) * 4) / frequencia_classe

print(mediana)