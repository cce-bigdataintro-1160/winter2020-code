import warnings

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings("ignore")

# Load wine dataset
wine = load_wine()
columns_names = wine.feature_names
y = wine.target
X = wine.data

# Scaling data (KNeighbors methods do not scale automatically!)
scaler = StandardScaler()
scaler.fit(X)
scaled_features = scaler.transform(X)

# Splitting dataset
X_train, X_test, y_train, y_test = train_test_split(scaled_features, y, test_size=0.35, random_state=1)

f1_scores = []

# Creating one model for each n neighbors, predicting and storing the result in an array
for Estimator in [KNeighborsClassifier, LogisticRegression, SGDClassifier, GaussianNB]:
    estimator = Estimator()
    estimator.fit(X_train, y_train)
    y_predicted = estimator.predict(X_test)
    f1 = f1_score(y_test, y_predicted, average="macro")
    f1_scores.append(f1)
    print(f'For {type(estimator)} the f1-score is {f1}')

print(f1_scores)

# Plotting results
result_df = pd.DataFrame(zip(['KNeighborsClassifier', 'LogisticRegression', 'SGDClassifier', 'GaussianNB'], f1_scores),
                         columns=['estimator', 'score'])
plt.figure(figsize=(8, 8))
bar_plot = sns.barplot(x='estimator', y='score', data=result_df)
plt.xlabel('Estimator')
plt.ylabel('F1 Score')

for index, row in result_df.iterrows():
    bar_plot.text(row.name, row['score'], round(row['score'], 2), color='black', ha="center")

plt.show()
