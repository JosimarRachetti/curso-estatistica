import pandas as pd
import random
import numpy as np

dataset = pd.read_csv('census.csv')

def amostra_sistematica(dataset, quantidade):
    amostra = quantidade

    tam_dataset = len(dataset)

    intervalo = tam_dataset//amostra

    print(intervalo)

    random.seed(1)

    primeiro_registro = random.randint(0, intervalo)

    valores_aleatorios = np.arange(primeiro_registro, tam_dataset, step=intervalo)

    amostrar_sistematica = dataset.iloc[valores_aleatorios]

    return amostrar_sistematica
