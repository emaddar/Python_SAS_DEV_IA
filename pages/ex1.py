from unicodedata import name
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


names = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"]
df = pd.read_fwf("https://raw.githubusercontent.com/emaddar/Python_SAS_DEV_IA/main/Data/housing.data", header=None, names = names)
# data_set_1.plot(kind='scatter', x='Population', y='Profit')
# plt.show()


# Insert X0 Column
Xd = df.drop(columns=['MEDV'])
Xd.insert(0, 'X0', 1)
print(Xd.head())


# numpy array format
X = Xd.values
y = df.MEDV.values
# sample size
m = len(df.index)
print(m)
# Initialize theta

# number of features
n = X.shape[1]
print(n)

theta = np.ones(n)
print(theta)


hypo = X@theta
# print(hypo)