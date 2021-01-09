import pandas as pd
import random
import numpy as np

dataset = pd.read_csv('census.csv')

# print(dataset.shape)
# primeiros registros
# print(dataset.head())
# ultimos registros
# print(dataset.tail())
# amostra aleatoria simples  // replace sempre traz valores diferentes // random_state sempre retorna os mesmo valores


def amostra_simples(dataset, quantidade):
    df_amostra_aleatoria_simples = dataset.sample(n=quantidade, replace=False, random_state=1)
    return df_amostra_aleatoria_simples
