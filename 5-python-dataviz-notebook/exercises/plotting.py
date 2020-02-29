

import matplotlib.pyplot as plt
import pandas as pd

# Loading dataset
df = pd.read_csv('../data/boston/housing.data',
                 sep='\s+',
                 header=None)

# Setting columns to dataset
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

fig, axes = plt.subplots(1, 1, figsize=(8,8))

axes.scatter(df['LSTAT'], df['AGE'],
             label='LSTATS VS AGE',
            s = df['RM'] ** 3
             )

axes.set_ylabel('AGE')

plt.legend()

plt.savefig('myplot.png')

plt.show()