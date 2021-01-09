import pandas as pd

dados = {'ano': ['1','2','3','4','total'],
         'matriculas_marco': [70, 50, 47, 23, 190],
         'matriculas_novembro': [65, 48, 40, 22, 175]}

dataset = pd.DataFrame(dados)

dataset['taxa_evasao'] = ((dataset['matriculas_marco']-dataset['matriculas_novembro'])/ dataset['matriculas_marco']) * 100

print(dataset)