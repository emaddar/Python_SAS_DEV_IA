from unicodedata import name
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


names = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"]
data_set_1 = pd.read_fwf("https://raw.githubusercontent.com/emaddar/Python_SAS_DEV_IA/main/Data/housing.data", header=None, names = names)
# data_set_1.plot(kind='scatter', x='Population', y='Profit')
# plt.show()


# print(data_set_1.head())
x = np.array(data_set_1.iloc[:, :-2])
y = np.array(data_set_1.iloc[:, -1])

# # number of training examples
m = len(x)
# # insert np.ones(m) to column 0
X = np.insert(x, 0, np.ones(m), axis=1)
n = X.shape[1]


# # init theta with 0s
init_theta = np.zeros((n,1))
# print(init_theta)


iterations = 1000
alpha = 0.00001

print(f"X shape = {X.shape}")
print(f"Y shape = {y.shape}")
print(f"Theta shape = {init_theta.shape}")



# simpler vectorized method
# def fonction_cout(X, y, theta):
#     m = len(y)
#     h = X @ theta
#     difference = h - y
#     square = np.square(difference)
#     J = 1 / (2 * m) * np.sum(square) 
#     return J
# print(fonction_cout(X, y, init_theta))

def fonction_cout(X, y, theta):
    m = len(y)
    J = (1/(2*m))*np.transpose((X@theta - y))@(X@theta - y)
    return J


def gradientDescent(X, y, theta, alpha, iterations):
    cout_list = []
    for i in range(iterations):
    
        theta = theta - alpha*(1/m)*np.transpose(X)@(X@theta - y)
            
        cout_val = fonction_cout(X, y, theta)
        cout_list.append(cout_val)

    return theta, cout_list

learned_theta, costs = gradientDescent(X, y, init_theta, alpha, iterations)


# print(learned_theta)
# print(costs[-5 : -1])
# df = pd.DataFrame(costs, columns =['cout'])
# df['iteration'] = df.index
# df.plot(kind='scatter', x = "iteration", y = "cout")
# plt.show()