from scipy.stats import skewnorm, shapiro
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot

#servem para descobrir se uma distribuição é normal ou não está

#criando distribuição normal
dados_normais = stats.norm.rvs(size=1000)
#criando distribuição nao normal
dados_nao_normais = skewnorm.rvs(a = 10, size = 1000)

sns.displot(dados_normais)
#plt.show()
sns.displot(dados_nao_normais)
#plt.show()


#usando os graficos de qqplot
qqplot(dados_normais, line ='s')
qqplot(dados_nao_normais, line='s')
plt.show()

#usando shapiro
_, p = shapiro(dados_nao_normais)
print(p)
alpha = 0.5
if alpha < p:
    print('distribuição normal')
else:
    print('distribuição não normal')