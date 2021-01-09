import pandas as pd

dataset = pd.read_csv('census.csv')
dataset2 = dataset[['income', 'education']]
# print(dataset2)
dataset3 = dataset2.groupby(['education', 'income'])['education'].count()
print(dataset3)
print(dataset3[' Bachelors', ' <=50K'], dataset3[' Bachelors', ' >50K'])

total_bachelors = 3134+2221

porcentagem_menos_50k = 3134/total_bachelors * 100
print(porcentagem_menos_50k)
porcentagem_mais_50k = 2221/total_bachelors * 100
print(porcentagem_mais_50k)