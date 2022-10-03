from unicodedata import name
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_set_1 = pd.read_csv("https://raw.githubusercontent.com/chtunsw/ml_notes/master/ml_course/exercises/01_Linear_Regression/data/ex1data1.txt", header=None, names=["Population", "Profit"])
# data_set_1.plot(kind='scatter', x='Population', y='Profit')
# plt.show()

x = np.array(data_set_1.iloc[:, :1])
y = np.array(data_set_1.iloc[:, 1:])

#print(y)

# number of training examples
m = len(x)
# insert np.ones(m) to column 0
X = np.insert(x, 0, np.ones(m), axis=1)
#print(X)
# init theta with 0s
init_theta = np.zeros((2,1))
#print(init_theta)
iterations = 10000
alpha = 0.001

# print(x.shape)
# print(y.shape)
# print(init_theta.shape)



# simpler vectorized method
def vectorized_compute_cost(X, y, theta):
    m = len(y)
    h = X @ theta
    diff = h - y
    res = 1 / (2 * m) * np.sum(np.square(diff)) 
    return res
# print(vectorized_compute_cost(X, y, init_theta))


# init theta with [[-1],[2]]
# print(vectorized_compute_cost(X, y, np.array([[-1],[2]])))




# vectorized gradient descent method
def gradientDescent(X, y, theta, alpha, iterations):
    new_theta = theta.copy()
    costs = []
    for it in range(iterations):
        sum = np.zeros(new_theta.shape)
        m = len(X)
        for i in range(m):
            sum += (new_theta.T @ np.array([X[i]]).T - y[i]).item() * np.array([X[i]]).T
        new_theta -= alpha * 1 / (2 * m) * sum
        new_cost = vectorized_compute_cost(X, y, new_theta)
        costs.append(new_cost)
        deff = costs[it] - costs[it - 1]
        print(f"Iteration :{it} , cout : {'{:.20f}'.format(deff)}")
    return new_theta, costs

learned_theta, costs = gradientDescent(X, y, init_theta, alpha, iterations)

print(learned_theta)
print(costs[-10 : -1])
df = pd.DataFrame(costs, columns =['cout'])
df['iteration'] = df.index
df.plot(kind='scatter', x = "iteration", y = "cout")
plt.show()