import pandas as pd

dados = {'empregos': ['Administrador_banco_dados','Programador','Arquiteto_redes'],
         'nova_jersey': [97350, 82080, 112840],
         'florida': [77140, 71540, 62310]}

dataset = pd.DataFrame(dados)

print(dataset)

# criando nova coluna

dataset['%_nova_jersey'] = (dataset['nova_jersey'] / dataset['nova_jersey'].sum() * 100)
dataset['%_florida'] = (dataset['florida'] / dataset['florida'].sum() * 100)
print(dataset)
