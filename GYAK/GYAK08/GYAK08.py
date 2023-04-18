import numpy as np
from sklearn.datasets import load_iris
import pandas as pd
from LinearRegressionSkeleton import LinearRegression as LinReg

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

model = LinReg(10000, -0.002)

X = df['petal width (cm)'].values
y = df['sepal length (cm)'].values

model.fit(X, y)

y_test_pred = np.array([model.predict(X) for X in model.X_test])
results = pd.DataFrame({"Predictions": y_test_pred, "Real": model.y_test})