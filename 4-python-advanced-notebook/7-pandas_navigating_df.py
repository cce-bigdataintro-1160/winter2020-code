#!/usr/bin/env python3

import pandas as pd


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


# We're now creating a dataframe straight from a data file
titanic = pd.read_csv(filepath_or_buffer='data/titanic/train.csv',
                      sep=',',
                      header=0)

# Getting DataFrames information
pretty_print("Printing an entire dataframe", titanic.to_string())
pretty_print("Show all column names for a dataframe", titanic.columns)

# Selecting DataFrame Columns
pretty_print("Selecting only the name column", titanic['Name'])
pretty_print("Selecting the type of the name column", type(titanic['Name']))
pretty_print("Selecting multiple columns: the Name, Fare and Age columns", titanic[['Name', 'Fare', 'Age']])
pretty_print("Summing up two selected columns", titanic['Fare'] + titanic['Age'])

# Using functions on specific columns
pretty_print("Count for each different values of age", titanic['Age'].value_counts())
pretty_print("Displaying unique values for the Fare Column removing any duplicates", titanic['Fare'].unique())

# Selecting DataFrame Rows by a condition
pretty_print("Selecting rows by criteria, only people with 30> years of age", titanic[titanic['Age'] > 30])
pretty_print("Selecting rows by multiple criteria",
             titanic[(titanic['Age'] > 30) & (titanic['Fare'] > 30) & (titanic['Survived'] == 1)])

# Extracting DataFrame correlations
pretty_print("Extracting dataframe correlation matrix", titanic.corr().to_string())
