# 2 Load the insurance.csv in a DataFrame using pandas. Explore the dataset using functions like to_string(), columns,
# index, dtypes, shape, info() and describe(). Use this DataFrame for the following exercises.
import pandas as pd

df = pd.read_csv('data/insurance.csv')

print(df.index)
print(df.columns)
print(df.to_string())
print(df.dtypes)
print(df.shape)
print(df.info())
print(df.describe())

# 3 Print only the column age
print(df['age'])

# 4 Print only the columns age,children and charges
print(df[['age', 'children', 'charges']])

# 5 Print only the first 5 lines and only the columns age,children and charges
print(df[['age', 'children', 'charges']].head(5))

# 6 What is the average, minimum and maximum charges ?
print(df[['charges']].describe())

# 7 What is the age and sex of the person that paid 10797.3362. Was he/she a smoker?
print(df[df['charges'] == 10797.3362][['age', 'sex']])

# 8 What is the age of the person who paid the maximum charge?
print(df[df['charges'] == df['charges'].max()][['age']])

# 9 How many insured people do we have for each region?
print(df['region'].value_counts())

# 10 How many insured people are children?
print(df[df['age'] < 18])

# 11 and 12 Using the method corr(), check if your assumptions were correct.
print(df[['age', 'charges', 'bmi']].corr())
