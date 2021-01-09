import pandas as pd
import random
import numpy as np

dataset = pd.read_csv('census.csv')


def amostra_grupo(dataset, n_grupos):
    numero_grupos = n_grupos
    qtd_por_grupo = len(dataset) / numero_grupos

    grupos_list = []
    id_grupo = 0
    contagem = 0

    for _ in dataset.iterrows():
        grupos_list.append(id_grupo)
        contagem += 1
        if contagem > qtd_por_grupo:
            contagem = 0
            id_grupo += 1

    np.unique(grupos_list, return_counts=True)

    # adicionando grupo
    dataset['grupo'] = grupos_list

    random.seed(1)
    grupo_menos_um = n_grupos - 1
    grupo_selecionado = random.randint(0, grupo_menos_um)
    grupo_amostra = dataset[dataset['grupo'] == grupo_selecionado]
    return grupo_amostra


grupo_amostra = amostra_grupo(dataset, 10)
print(grupo_amostra.shape)
print(grupo_amostra.head())