import numpy as np


class Perceptron:
    def __init__(self, num_features, learning_rate=0.001):
        self.lr = learning_rate
        self.weights = np.zeros(num_features)
        self.bias = 0

    def step(self, x):
        return np.where(x > 0, 1, 0)

    def fit(self, X, y, epochs):
        for _ in range(epochs):
            for x_i, y_i in zip(X, y):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.step(linear_output)
                update = self.lr * (y_i - y_predicted)
                self.weights += update * x_i
                self.bias += update

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self.step(linear_output)
        return y_predicted