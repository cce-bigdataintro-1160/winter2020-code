import numpy as np
from sklearn import metrics
from sklearn.datasets import load_boston

boston_housing = load_boston()
columns_names = boston_housing.feature_names
y = boston_housing.target
X = boston_housing.data

# Splitting features and target datasets into: train and test
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35)

# Training a model using multiple differents algorithms and comparing the results
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import Lasso

for Model in [LinearRegression, GradientBoostingRegressor, ElasticNet, KNeighborsRegressor, Lasso]:
    model = Model()
    model.fit(X_train, y_train)
    predicted_values = model.predict(X_test)
    print(f"Printing RMSE error for {Model}: {np.sqrt(metrics.mean_squared_error(y_test, predicted_values))}")
