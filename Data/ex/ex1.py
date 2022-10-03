# from unicodedata import name
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np



# data_set_1 = pd.read_csv("https://raw.githubusercontent.com/emaddar/Python_SAS_DEV_IA/main/Data/ex1data1.txt",
#     header=None, names=["Population", "Profit"])
# # print(data_set_1.head())

# # make plot of dataframe. by default, matplotlib backend is used.
# # data_set_1.plot(kind='scatter', x='Population', y='Profit')
# # plt.show()

# x = np.array(data_set_1.iloc[:, :1])
# y = np.array(data_set_1.iloc[:, 1:])

# # number of training examples
# m = len(x)
# print(f"m = {m}")
# # insert np.ones(m) to column 0
# X = np.insert(x, 0, np.ones(m), axis=1)
# # print(X)
# # init theta with 0s
# init_theta = np.zeros((2,1))
# print(f"init_theta = {init_theta}")



# iterations = 3000
# alpha = 0.01

# print(f"x shape {X.shape}")
# print(f"y shape = {y.shape}")
# print(f"init theta;shape = {init_theta.shape}")



# ## Computing the cost function
# def vectorized_compute_cost(X, y, theta):
#     m = len(y)
#     h = X @ theta
#     diff = h - y
#     res = 1 / (2 * m) * np.sum(np.square(diff)) 
#     return res



# ## Gradient descent
# def gradientDescent(X, y, theta, alpha, iterations):
#     new_theta = theta.copy()
#     costs = []
#     for it in range(iterations):
#         sum = np.zeros(new_theta.shape)
#         m = len(X)
#         for i in range(m):
#             sum += (new_theta.T @ np.array([X[i]]).T - y[i]).item() * np.array([X[i]]).T
#         new_theta -= alpha * 1 / (2 * m) * sum
#         new_cost = vectorized_compute_cost(X, y, new_theta)
#         costs.append(new_cost)
#     return new_theta, costs

# learned_theta, costs = gradientDescent(X, y, init_theta, alpha, iterations)

# print(learned_theta)
# print(costs[-5 : -1])


# # predict values for population sizes of 35,000 and 70,000
# prediction1 = (learned_theta.T @ np.array([[1], [3.5]])).item()
# prediction2 = (learned_theta.T @ np.array([[1], [7]])).item()
# print("prediction 1: population 3.5, profit {}".format(prediction1))
# print("prediction 1: population 7, profit {}".format(prediction2))

















# # visualize result
# x_vector = np.linspace(data_set_1.Population.min(), data_set_1.Population.max(), 100)
# x_constructed = np.insert(np.array([x_vector]), 0, np.ones(100), axis=0)
# y_constructed = learned_theta.T @ x_constructed
# y_vector = y_constructed.flatten()

# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,16))
# ax1.plot(x, y, "o", label="training data")
# ax1.plot(x_vector, y_vector, "-", label="prediction")
# ax1.legend()
# ax1.set_title("Predicted Profit")
# ax1.set_xlabel("Population")
# ax1.set_ylabel("Profit")
# ax2.plot(range(1, iterations + 1), costs, "-")
# ax2.set_title("Cost")
# ax2.set_xlabel("Iterations")
# ax2.set_ylabel("Cost")
# plt.show()