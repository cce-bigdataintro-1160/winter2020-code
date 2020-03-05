import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA

iris = datasets.load_iris()
cancer = datasets.load_breast_cancer()
wine = datasets.load_wine()
boston = datasets.load_boston()
diabetes = datasets.load_diabetes()

# PCA or dimensionality reduction, is a technique that allows you to have a consolidated
# view of multiple features in a smaller dimension. Very useful to plot 2d and 3d visualizations
# over a large number of features
pca = PCA(n_components=2)
proj = pca.fit_transform(iris.data)
plt.scatter(proj[:, 0], proj[:, 1], c=iris.target, edgecolors='black')
plt.colorbar()
plt.show()
