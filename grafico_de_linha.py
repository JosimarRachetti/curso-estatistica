import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

vendas = {'mes': np.array([1,2,3,4,5,6,7,8,9,10,11,12]),
          'valor': np.array([100,200,120,300,500,198,200,209,130,500,300,120])}

vendas_df = pd.DataFrame(vendas)

sns.relplot(x ='mes', y = 'valor', kind = 'line', data = vendas_df)
plt.show()