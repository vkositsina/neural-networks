# import matplotlib.pyplot as plt
import numpy as np


X = np.array([
    [-2, 4, -1],
    [4, 1, -1],
    [1, 6, -1],
    [2, 4, -1],
    [6, 2, -1],

])
y = np.array([-1, -1, 1, 1, 1])

def perceptron_sgd_plot(X, Y):
    '''
    train perceptron and plot the total loss in each epoch.

    :param X: data samples
    :param Y: data labels
    :return: weight vector as a numpy array
    '''
    w = np.zeros(len(X[0]))
    eta = 1
    n = 30
    errors = []

    for t in range(n):
        total_error = 0
        for i, x in enumerate(X):
            if (np.dot(X[i], w) * Y[i]) <= 0:
                total_error += (np.dot(X[i], w) * Y[i])
                w = w + eta * X[i] * Y[i]
        errors.append(total_error * -1)

    print(w)
    return w


# for d, sample in enumerate(X):
#     # Plot the negative samples
#     if d < 2:
#         plt.scatter(sample[0], sample[1], s=120, marker='_', linewidths=2, color='black')
#     # Plot the positive samples
#     else:
#         plt.scatter(sample[0], sample[1], s=120, marker='+', linewidths=2, color='purple')

# Add our test samples
# plt.scatter(5, 8, s=120, marker='+', linewidths=2, color='green')
# plt.scatter(8, 1, s=120, marker='_', linewidths=2, color='blue')

# Print the hyperplane calculated by perceptron_sgd()
w = perceptron_sgd_plot(X, y)
x2 = [w[0], w[1], -w[1], w[0]]
x3 = [w[0], w[1], w[1], -w[0]]

x2x3 = np.array([x2, x3])
X, Y, U, V = zip(*x2x3)
# ax = plt.gca()
# ax.quiver(X, Y, U, V, scale=1, color='blue')
# plt.show()
