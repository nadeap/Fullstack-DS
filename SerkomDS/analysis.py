import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('namadata.csv')
data = pd.read_excel('data.xlsx')

data.head()
data.tail()
data.info()
data.describe()
data.shape
data.isnull().sum()
data.corr()
data.column()
data.nunique()
data.unique()
data['kolom'].value_counts()
data.duplicated().sum()

### Matplotlib
#histogram hanya untuk 1 kolom
data['namakolom'].hist()
plt.title('Judul Grafik')
plt.xlabel('Nama Label X')
plt.ylabel('Nama Label Y')
plt.show()

sns.heatmap(data=data.corr())
