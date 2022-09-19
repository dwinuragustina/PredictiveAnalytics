# -*- coding: utf-8 -*-
"""Predictive Analytics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X_HPfI_OXTPG4TSvO6ekMeRwgiq6Jcf-

Nama : Dwi Nur Agustina

SIB ID : M123Y0191

SIB Group : M01

Pertama-tama, melakukan import library yang akan digunakan untuk data analisis, data visualisasi, data preprocessing dan modelling
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
# %matplotlib inline

# library for data preprocessing
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV, train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer

# library for modeling
from sklearn.svm import SVR
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor

"""Melakukan loading pada dataset yang digunakan"""

path = 'EURUSD_BID_sample.csv'
df = pd.read_csv(path)
df.head()

"""Mencetak dataset yang digunakan"""

print(f'Data memiliki {df.shape[0]} records dan {df.shape[1]} columns.')

"""Dataset yang digunakan memiliki 14880 records dan 6 columns.

1. Time : merupakan tanggal dan waktu data tersebut direkam
2. Open : merupakan harga pembukaan pada hari tersebut
3. High : merupakan harga tertinggi pada hari tersebut
4. Low : merupakan harga terendah pada hari tersebut
5. Close : merupakan harga penutupan pada hari tersebut
6. Volume : merupakan banyaknya transaksi pada hari tersebut
"""

df.info()

"""Mencetak missing value dalam dataframe"""

print('Total missing value dalam dataframe : ', df.isnull().sum().sum(), 'records')

"""Dari output diatas, dapat dilihat bahwa dataframe tidak memiliki missing value, sehingga bisa melanjutkan ke tahap berikutnya."""

df.describe()

"""Data visualiation dengan menggunakan boxplot dari library seaborn"""

numerical_col = [col for col in df.columns if df[col].dtypes == 'float64']
plt.figure(figsize = (15,8))
sns.boxplot(data = df[numerical_col])
plt.show()

"""Output diatas merupakan visualisasi outlier pada data. Dimana pada output tersebut menggunakan boxplot dan library seaborn."""

Q1 = df.quantile(.25)
Q3 = df.quantile(.75)
IQR = Q3 - Q1
bottom = Q1 - 1.5 * IQR
top = Q3 + 1.5 * IQR
df = df[~((df < bottom) | (df > top)).any(axis=1)]
df.head()

"""Mencetak jumlah data pada dataset"""

print(f'Data memiliki {df.shape[0]} records dan {df.shape[1]} columns.')

"""Melakukan univariate analysis"""

cols = 3
rows = 2
fig = plt.figure(figsize=(cols * 5, rows * 5))

for i, col in enumerate(numerical_col):
  ax = fig.add_subplot(rows, cols, i + 1)
  sns.histplot(x = df[col], bins = 30, kde = True, ax = ax)
fig.tight_layout()
plt.show()

"""Melakukan multivariate analysis"""

sns.pairplot(df[numerical_col], diag_kind = 'kde')
plt.show()

"""Membuat matriks korelasi untuk numerical feature"""

plt.figure(figsize = (15,8))
corr = df[numerical_col].corr().round(2)
sns.heatmap(data = corr, annot = True, vmin = -1, vmax = 1, cmap = 'coolwarm', linewidth = 1)
plt.title('Matriks korelasi untuk numerical feature', size = 15)
plt.show()

"""Selanjutnya, akan melakukan penghapusan pada kolom 'Time', 'Volume', dan 'Close'. Hal tersebut dikarenakan kolom-kolom tersebut dirasa tidak diperlukan oleh model dan data tersebut akan mengganggu model dalam proses training."""

df = df.drop(['Time', 'Volume', 'Close'], axis = 1)
df.head()

"""Melakukan splitting pada dataset"""

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2, random_state = 42)

print('Total X_train :', len(X_train), 'records')
print('Total y_train :', len(y_train), 'records')
print('Total X_test :', len(X_test), 'records')
print('Total y_test :', len(y_test), 'records')

"""Untuk melakukan normalisasi data, akan menggunakan library MinMaxScaler. Fungsi dari normalisasi pada data agar model lebih cepat dalam mempelajari data, karena data telah diubah pada rentang tertentu seperti antara 0 dan 1."""

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

models = pd.DataFrame(columns = ['train_mse', 'test_mse'], index = ['SVR', 'KNN', 'GradientBoosting'])

"""Langkah selanjutnya melakukan hyperparameter tuning. Hyperparameter tuning adalah salah satu teknik yang dilakukan akan model dapat berjalan dengan performa terbaik. Biasanya dalam hyperparameter tuning, hyperparameter akan ditentukan secara acak oleh teknisi. Namun jika tidak ingin mencoba coba hyperparameter mana yang terbaik, dapat menggunakan GridSearch. GridSearch merupakan sebuah teknik yang memungkinkan untuk menguji beberapa hyperparameter sekaligus pada sebuah model."""

def grid_search(model, hyperparameters):
  results = GridSearchCV(
      model,
      hyperparameters,
      cv = 5,
      verbose = 1,
      n_jobs = 6)

  return results
  
svr = SVR()
hyperparameters = {
    'kernel': ['rbf'],
    'C': [0.001, 0.01, 0.1, 10, 100, 1000],
    'gamma': [0.3, 0.03, 0.003, 0.0003]
}

svr_search = grid_search(svr, hyperparameters)
svr_search.fit(X_train, y_train)
print(svr_search.best_params_)
print(svr_search.best_score_)

"""n_neighbors, hyperparameter ini adalah jumlah tetangga yang diperlukan untuk menentukan letak data baru."""

knn = KNeighborsRegressor()
hyperparameters = {
    'n_neighbors': range(1, 10)}

knn_search = grid_search(knn, hyperparameters)
knn_search.fit(X_train, y_train)
print(knn_search.best_params_)
print(knn_search.best_score_)

"""Model training"""

svr = SVR(C = 10, gamma = 0.3, kernel = 'rbf')
svr.fit(X_train, y_train)

"""Gradient Boosting Regression"""

gradient_boost = GradientBoostingRegressor(criterion = 'squared_error', learning_rate = 0.01, n_estimators = 1000)
gradient_boost.fit(X_train, y_train)

"""K-Nearest Neighbors (KNN)"""

knn = KNeighborsRegressor(n_neighbors = 9)
knn.fit(X_train, y_train)

"""Model evaluation"""

model_dict = {
    'SVR': svr,
    'GradientBoosting': gradient_boost,
    'KNN': knn,
}

for name, model in model_dict.items():
  models.loc[name, 'train_mse'] = mean_squared_error(y_train, model.predict(X_train))
  models.loc[name, 'test_mse'] = mean_squared_error(y_test, model.predict(X_test))

models.head()

"""Plot diagram"""

models.sort_values(by = 'test_mse', ascending = False).plot(kind = 'bar', zorder = 3)