import numpy as np
from sklearn.model_selection import train_test_split

class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        self.epochs = epochs
        self.lr = lr
        self.m = 0
        self.c = 0
        self.X_test = np.ndarray
        self.y_test = np.ndarray
        self.loss = 0


    def fit(self, X: np.array, y: np.array):
        n = float(len(X))  # Number of elements in X
        self.m = 0
        self.c = 0

        for i in range(self.epochs):
            y_pred = self.m * X + self.c  # The current predicted value of Y
            residuals = y - y_pred
            D_m = (-2 / n) * sum(X * residuals)  # Derivative wrt m
            D_c = (-2 / n) * sum(residuals)  # Derivative wrt c
            self.m = self.m - self.lr * D_m  # Update m
            self.c = self.c - self.lr * D_c  # Update c

        self.loss = np.sum(residuals ** 2)


    def predict(self, X):
        return self.m * X * self.c