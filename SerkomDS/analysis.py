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
data.drop_duplicates()
data.fillna(axis=0) #0 row, 1 column

### Matplotlib
#histogram hanya untuk 1 kolom
data['namakolom'].hist()
plt.title('Judul Grafik')
plt.xlabel('Nama Label X')
plt.ylabel('Nama Label Y')
plt.show()

#Boxplot untuk 1 kolom
data.boxplot(column='namakolom')
plt.title('Judul Grafik')
plt.ylabel('Nama Label Y')
plt.show()

#Scatter plot 2 kolom
data.plot.scatter(x='kolomx', y='kolomy')
plt.title()
plt.xlabel()
plt.ylabel()
plt.show()

#Barplot 2 kolom
plt.bar(data['kolomA'], data['kolomB'])
plt.title()
plt.xlabel()
plt.ylabel()
plt.show()

###Seaborn
sns.scatterplot(x,y)
sns.lineplot(x,y)
sns.barplot(x,y)
sns.histplot(x,y)
sns.boxplot(x,y)
sns.pairplot(data, hue='species')
sns.heatmap(data=data.corr())

#Pandas Cleaning Data
data = data.drop(column='namakolom')
data['kolomA'] = data['kolomA'].replace('KataAwal','KataGanti')

###Drop Outliers
Q1 = data['A'].quantile(0.25)
Q3 = data['A'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
filtered_data = data[(data['A'] >= lower_bound) & (data['A'] <= upper_bound)]