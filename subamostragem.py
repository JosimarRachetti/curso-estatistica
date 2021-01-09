import imblearn.under_sampling
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import seaborn as sns


dataset = pd.read_csv('credit_data.csv')
print(dataset.shape)

dataset.dropna(inplace=True)

x = dataset.iloc[:, 1:4].values
y = dataset.iloc[:, 4].values

tl = imblearn.under_sampling.TomekLinks(sampling_strategy='majority')
# gerando a amostra com técnica de subamostragem(retirando valores da amostra para balancear)
x_under, y_under = tl.fit_sample(x, y)

print(x_under.shape, y_under.shape, tl.sample_indices_)

x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(x_under, y_under, test_size = 0.2, stratify = y_under)

modelo = GaussianNB()
# treinamento do algoritimo com dados
modelo.fit(x_treinamento, y_treinamento)

# previsoes geradas pelo algoritmo
previsoes = modelo.predict(x_teste)

# verificando a acuracidade do algoritmo
from sklearn.metrics import accuracy_score, confusion_matrix

print(accuracy_score(previsoes, y_teste))
cm = confusion_matrix(previsoes, y_teste)
print(cm)
sns.heatmap(cm, annot=True)
plt.show()


