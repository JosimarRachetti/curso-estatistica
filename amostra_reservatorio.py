import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit
import random
import numpy as np


dataset = pd.read_csv('census.csv')

def amostra_reservatorio(dataset, amostras):
    stream = []
    for i in range(len(dataset)):
        stream.append(i)

    i = 0
    tamanho = len(dataset)

    reservatorio = [0] * amostras

    for i in range(amostras):
        reservatorio[i] = stream[i]

    while i < tamanho:
        j = random.randrange(i + 1)
        if j < amostras:
            reservatorio[j] = stream[i]
        i += 1

    return dataset.iloc[reservatorio]


df_amostragem_reservatorio = amostra_reservatorio(dataset, 100)

