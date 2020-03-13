import numpy as np
from sklearn.datasets import load_boston

boston_housing = load_boston()
columns_names = boston_housing.feature_names
y = boston_housing.target
X = boston_housing.data

# Splitting features and target datasets into: train and test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35)

# Training a Linear Regression model with fit()
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train, y_train)

from joblib import dump, load
# Saving our trained model in a file to be used later
dump(lm, 'my_model.joblib')

# Retrieving our trained model from the file to predict
loaded_lm = load('my_model.joblib')

# Predicting the results for our test dataset
predicted_values = loaded_lm.predict(X_test)
from sklearn import metrics
print(f"Printing RMSE error: {np.sqrt(metrics.mean_squared_error(y_test, predicted_values))}")
