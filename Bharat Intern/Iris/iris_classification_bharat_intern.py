# -*- coding: utf-8 -*-
"""Iris Classification - Bharat Intern.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-GLMgX_ba_heDT9Fuf8FH1Jgv_lYtc_h
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import warnings
warnings.filterwarnings('ignore')

!pip install scikit-learn
!pip install seaborn

d = pd.read_csv('/content/drive/MyDrive/iris.csv')
d

d.shape

d.describe()

d.info()

d['variety'].value_counts()

"""#**Pre - processing**"""

d.isnull().sum()

"""#**Data Analysis**"""

d['sepal.length'].hist()

d['sepal.width'].hist()

d['petal.length'].hist()

d['petal.width'].hist()

cl = ['red', 'orange', 'blue']
s = ['Virginica', 'Versicolor', 'Setosa']

for i in range(3):
  x = d[d['variety'] == s[i]]
  plt.scatter(x['petal.length'], x['petal.width'], c = cl[i], label = s[i])

plt.xlabel('petal length')
plt.ylabel('petal width')

plt.legend()

for i in range(3):
  x = d[d['variety'] == s[i]]
  plt.scatter(x['petal.length'], x['petal.width'], c = cl[i], label = s[i])

plt.xlabel('petal length')
plt.ylabel('petal width')

plt.legend()

for i in range(3):
  x = d[d['variety'] == s[i]]
  plt.scatter(x['sepal.length'], x['petal.length'], c = cl[i], label = s[i])

plt.xlabel('Sepal length')
plt.ylabel('petal length')

plt.legend()

for i in range(3):
  x = d[d['variety'] == s[i]]
  plt.scatter(x['sepal.width'], x['petal.width'], c = cl[i], label = s[i])

plt.xlabel('Sepal width')
plt.ylabel('petal width')

plt.legend()

"""#**Correlation Matrix**"""

d.corr()

corr = d.corr()

fig, ax = plt.subplots(figsize = (5,4))
sns.heatmap(corr, annot = True, ax = ax, cmap = 'coolwarm')

"""#**Model Training and Testing**"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import pickle

x = d.drop(columns = ['variety'])

y = d[['variety']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.30)

model = LogisticRegression()
model.fit(x_train, y_train)
print("logistic Regression Accuracy: ", model.score(x_test, y_test) * 100)

model.fit(x_train.values, y_train.values)

print("Accuracy: ", model.score(x_test, y_test) * 100)

model = KNeighborsClassifier()
model.fit(x_train.values, y_train.values)
print("K - Neighbors Accuracy: ", model.score(x_test, y_test) * 100)

print("Accuracy: ",model.score( x_test, y_test) * 100)

model = DecisionTreeClassifier()
model.fit(x_train.values, y_train.values)
print("Decision Tree Accuracy: ", model.score(x_test, y_test) * 100)

model.fit(x_train.values, y_train.values)

print("Accuracy: ", model.score(x_test, y_test) * 100)

import pickle
filename = "saved_model.sav"
pickle.dump(model, open(filename, 'wb'))

import pickle

filename = 'saved_model.sav'
try:
  with open(filename, 'wb') as file:
    pickle.dump(model, file)
  print("Model saved successfully")
except Exception as e:
  print(f"Error saving the model: , {e}")

load_model = pickle.load(open(filename, 'rb'))

load_model.predict([(6.0, 2,2, 4.0)])

import sklearn
print(sklearn.__version__)