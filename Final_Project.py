import pandas as pd
import seaborn as sns
import datetime as dt
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.cluster import KMeans
import numpy as np
# графики в svg выглядят более четкими
%config InlineBackend.figure_format = 'svg'
import warnings
warnings.filterwarnings('ignore')
# увеличим дефолтный размер графиков
from pylab import rcParams
rcParams["figure.figsize"] = 10, 6
sns.set_style("whitegrid", {'axes.grid' : True})

data = pd.read_csv("dataset.csv", sep = ";")
data.head()
data.shape
data.info()
data.isnull().sum()
data = data[~data["Товар"].isnull()]
data.shape
data = data.drop_duplicates(subset = None, keep = 'first', inplace = False)
data.shape
data["Дата"] = pd.to_datetime(data["Дата"])
data["Количество"] = data["Количество"].astype(int)
data.info()
data.head()

data[['Количество', 'Сумма']].describe()
sns.distplot(data["Сумма"].astype(int))
data['Только дата'] = data['Дата'].dt.date
just_data = data[['Сумма', 'Только дата']].groupby('Только дата').sum().sort_values('Только дата', ascending = True).reset_index()
just_data.head()

plt.plot(just_data['Только дата'], just_data['Сумма'])
plt.title('График зависимости суммы от даты')
plt.ylabel('Сумма')
plt.show()

plt.hist(data['Дата'].dt.hour.values, bins=24)
plt.xlabel('Часы')
plt.ylabel('Количество')
plt.title('Диаграмма зависимости частоты покупок от часов')

profit = data[['Товар', 'Количество', 'Сумма']].groupby('Товар').sum().sort_values('Сумма', ascending = False).reset_index()
profit.head()

sum_data = data.groupby(['Товар'])['Количество', 'Сумма'].sum().reset_index()
sum_data

sum_data['Процент продаж'] = sum_data['Сумма'] / sum_data['Сумма'].sum() * 100
sum_data['Процент кол-ва'] = sum_data['Количество'] / sum_data['Количество'].sum() * 100
sum_data = sum_data.sort_values('Процент продаж', ascending = False)
sum_data['Сумма продаж'] = sum_data['Процент продаж'].cumsum()
sum_data = sum_data.sort_values('Процент кол-ва', ascending = False)
sum_data['Сумма кол-ва'] = sum_data['Процент кол-ва'].cumsum()
sum_data.head()

sns.set()
ax = sns.scatterplot(x = 'Сумма продаж', y = 'Сумма кол-ва', color = "rebeccapurple", data = sum_data)
plt.show()

corr = sum_data.corr()
corr_greater_than_50 = corr[corr>=.5]
corr_greater_than_50

sns.heatmap(corr_greater_than_50, cmap = "Blues", annot = True)

purchase_rate = data[['Дата', 'Сумма']]
purchase_rate.set_index('Дата', inplace = True)
purchase_rate = purchase_rate.resample('M').sum().sort_values('Дата', ascending = True)
purchase_rate

sns.set()
ax = sns.scatterplot(x = 'Дата', y = 'Сумма', color = "gold", data = purchase_rate)
plt.show()