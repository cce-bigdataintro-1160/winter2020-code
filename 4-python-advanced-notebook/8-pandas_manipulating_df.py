#!/usr/bin/env python3

import numpy as np
import pandas as pd


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


titanic = pd.read_csv(filepath_or_buffer='data/titanic/train.csv',
                      sep=',',
                      header=0)

# # Getting DataFrames information
pretty_print("Titanic dataframe", titanic)
# pretty_print("Titanic columns", titanic.columns)

# Dropping DataFrame rows
# pretty_print("Dropping the row with index 1", titanic.drop(1))
# pretty_print("Dropping the entire column Embarked", titanic.drop('Embarked', axis=1)) #inplace=True

#
# # Multiplying DataFrame values and adding columns
# titanic['SquaredFare'] = titanic['Fare'] ** 2
# pretty_print("Showing we added the SquaredFare column", titanic.to_string())
#
# # Cleaning up DataFrames by removing null values
# pretty_print("Dropping all rows with null values", titanic.dropna())
# pretty_print("Dropping all columns with null values", titanic.dropna(axis=1))
#
# # Cleaning up DataFrames by replacing null values with other values
# pretty_print("Filling all null values will FILL VALUE", titanic.fillna(value='FILL VALUE'))
titanic['CorrectedAge'] = titanic['Age'].fillna(value=titanic['Age'].mean())
pretty_print("Showing we added the CorrectedAge column", titanic[['Age', 'CorrectedAge']])
