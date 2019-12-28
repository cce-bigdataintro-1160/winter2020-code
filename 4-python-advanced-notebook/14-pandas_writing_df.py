#!/usr/bin/env python3

import pandas as pd


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


# Make sure to install xlrd with pip3!!!
df = pd.read_excel(io='data/titanic/train.xlsx',
                   sheet_name='Sheet1',
                   header=0)

df.to_csv('data/titanic/created_train.csv')

