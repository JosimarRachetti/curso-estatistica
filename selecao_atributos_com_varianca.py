import numpy as np
import pandas as pd
base_selecao = {'a': np.random.rand(20),
                'b': np.array([0.5] * 20),
                'classe': np.random.randint(0, 2, size=20)}

print(base_selecao)

dataset = pd.DataFrame(base_selecao)

print(dataset)

varianca_coluna_a = np.var(dataset['a'])
varianca_coluna_b = np.var(dataset['b'])

print("varianca coluna a: " + str(varianca_coluna_a))
print("varianca coluna b: " + str(varianca_coluna_b))

from sklearn.feature_selection import VarianceThreshold

X = dataset.iloc[:, 0:2].values #Pegando valores colunas A e B
selecao = VarianceThreshold(threshold=0.07)
atributos_valor_maior_007 = selecao.fit_transform(X)

print(atributos_valor_maior_007)
