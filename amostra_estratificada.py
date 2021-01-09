import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit
import random
import numpy as np

# biblioteca sklearn é usada para amostra estratificada
dataset = pd.read_csv('census.csv')

tam_dataset = len(dataset)
print(dataset["income"].value_counts())

print(7841/tam_dataset)

print(24720/tam_dataset)


def amostragem_estratificada(dataset, percentual, campo):
    # indicando o tamanho da amostra no caso 10%
    split = StratifiedShuffleSplit(test_size=percentual, random_state=1)

    #retorna a quantidade relacionada a porcentagem de cada tipo do income
    for _, y in split.split(dataset, dataset[campo]):
        df_y = dataset.iloc[y]

    return df_y