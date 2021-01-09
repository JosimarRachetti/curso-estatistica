import pandas as pd
from amostra_simples import amostra_simples
from amostra_sistematica import amostra_sistematica
from amostra_estratificada import amostragem_estratificada
from amostra_grupo import amostra_grupo
from amostra_reservatorio import amostra_reservatorio
from sklearn.model_selection import StratifiedShuffleSplit
import random
import numpy as np


dataset = pd.read_csv('credit_data.csv')

amostra_simples = amostra_simples(dataset, 1000)
print("Amostra simples:")
print(amostra_simples.shape)
print(amostra_simples['age'].mean())
print(amostra_simples['income'].mean())
print(amostra_simples['loan'].mean())

amostra_sistematica = amostra_sistematica(dataset, 1000)
print("Amostra sistematica:")
print(amostra_sistematica.shape)
print(amostra_sistematica['age'].mean())
print(amostra_sistematica['income'].mean())
print(amostra_sistematica['loan'].mean())

grupo_amostra = amostra_grupo(dataset, 32)
print("Amostra grupo:")
print(grupo_amostra.shape)
print(grupo_amostra['age'].mean())
print(grupo_amostra['income'].mean())
print(grupo_amostra['loan'].mean())

amostragem_estratificada = amostragem_estratificada(dataset, 0.5, 'c#default')
print("Amostra estratificada:")
print(amostragem_estratificada.shape)
print(amostragem_estratificada['age'].mean())
print(amostragem_estratificada['income'].mean())
print(amostragem_estratificada['loan'].mean())

amostra_reservatorio = amostra_reservatorio(dataset, 1000)
print("Amostra reservatorio:")
print(amostra_reservatorio.shape)
print(amostra_reservatorio['age'].mean())
print(amostra_reservatorio['income'].mean())
print(amostra_reservatorio['loan'].mean())
