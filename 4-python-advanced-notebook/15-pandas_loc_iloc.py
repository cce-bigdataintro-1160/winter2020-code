#!/usr/bin/env python3


import pandas as pd


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


# We're now creating a dataframe straigh from a data file
titanic = pd.read_csv(filepath_or_buffer='data/titanic/train.csv',
                      sep=',',
                      header=0)

# Selecting DataFrame Rows and Columns by name with loc function
pretty_print("Selecting the row 1", titanic.loc[1])
pretty_print("Selecting rows 1, 2 and 3, and also the columns Name and Sex", titanic.loc[[1, 2, 3], ['Name', 'Sex']])
pretty_print("Selecting ranges of rows and columns", titanic.loc[37:43, 'Name':'Cabin'])

# Selecting DataFrame Rows and Columns by index with iloc function
pretty_print("Selecting the row 1 by index", titanic.iloc[1])
pretty_print("Selecting rows 1, 2 and 3, and also the columns Name and Sex by index", titanic.iloc[[1, 2, 3], [3, 4]])
pretty_print("Selecting ranges of rows and columns by index", titanic.iloc[37:49, 3:5])
