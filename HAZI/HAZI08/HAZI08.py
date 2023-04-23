import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error

def load_iris_data() -> sklearn.utils.Bunch:
    return load_iris()


def check_data(bunch) -> pd.DataFrame:
    df = pd.DataFrame(bunch.data, columns=bunch.feature_names)
    return df.head(5)


def linear_train_data(bunch):
    df = pd.DataFrame(bunch.data, columns=bunch.feature_names)
    y = df["sepal length (cm)"].to_numpy()
    X = df.drop("sepal length (cm)", axis=1).to_numpy()
    return X, y


def logistic_train_data(bunch):
    data = pd.DataFrame(bunch.data, columns=bunch.feature_names).to_numpy()
    target = pd.DataFrame(bunch.target).to_numpy()
    return data, target


def split_data(X, y):
    return train_test_split(X, y)


def train_linear_regression(X_train, y_train):
    return LinearRegression().fit(X_train, y_train)


def train_logistic_regression(X_train, y_train):
    return LogisticRegression().fit(X_train, y_train)


def predict(model, X_test):
    return model.predict(X_test)


def plot_actual_vs_predicted(y_test, y_pred):
    fig, ax = plt.subplots()
    ax.set_title('Actual vs Predicted Target Values')
    ax.set_xlabel('Actual')
    ax.set_ylabel('Predicted')
    ax.scatter(y_test, y_pred)
    #plt.show()

def evaluate_model(y_test, y_pred):
    return mean_squared_error(y_test, y_pred)