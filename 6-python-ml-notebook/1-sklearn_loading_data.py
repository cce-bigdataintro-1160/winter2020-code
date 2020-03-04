import pandas as pd
import numpy as np

# Example 1 - Loading data using our pandas DataFrames (as in all previous classes)
wine_df = pd.read_csv('data/wine.data',
                      sep=',',
                      header=None)
wine_df.columns = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols',
                   'flavanoids',
                   'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280 od315_of_diluted_wines',
                   'proline']

# Separating features(X) and target(y)
X = wine_df.drop('class', axis=1)
y = wine_df['class']

print(f'Dataset X shape: {X.shape}')
print(f'Dataset y shape: {y.shape}')




# Example 2 - Loading data using sklearn dataset
from sklearn.datasets import load_wine
wine = load_wine()

# features(X) and target(y) are already separated
X = wine.data
y = wine.target

print(f'sklearn dataset X shape: {X.shape}')
print(f'sklearn dataset y shape: {y.shape}')

# What's inside this sklearn loaded dataset
print(f'keys: {wine.keys()}')
print(f'data: {wine.data}')
print(f'target: {wine.target}')
print(f'feature_names: {wine.feature_names}')


# Rebuilding pandas DF from dataset (for plotting and statistical facts)
convert_to_df = pd.DataFrame(X, columns=wine.feature_names)
convert_to_df['target'] = y
print(convert_to_df.describe())
