import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/boston/housing.data',
                 sep='\s+',
                 header=None)

# Setting columns to dataset
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

fig, axes = plt.subplots(1, 1, figsize=(5,5))


# axes[0].plot(df['NOX'].sort_values().reset_index(drop=True))
# axes[0].set_title('nitric oxides concentration')
# axes[0].set_xlabel('Index')
# axes[0].set_ylabel('Nitric oxides concentration')

axes.scatter(df['CRIM'], df['NOX'],
             color='purple',
             marker='s',
             alpha=0.2,
             s=df['MEDV'] ** 1.3)
axes.set_title('Value to NOX')
axes.set_xlabel('CRIME')
axes.set_ylabel('Nitric oxides concentration')

plt.tight_layout()

plt.savefig('nox_medv.png')

plt.close()