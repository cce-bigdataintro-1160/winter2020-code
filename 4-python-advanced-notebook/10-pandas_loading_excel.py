#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


# Make sure to install xlrd with pip3!!!
titanic = pd.read_excel(io='data/titanic/train.xlsx',
                        sheet_name='Sheet1',
                        header=0)

pretty_print("Titanic dataframe", titanic.to_string())
pretty_print("Titanic dataframe", titanic.columns)
pretty_print("Titanic dataframe", titanic.info())
pretty_print("Titanic dataframe", titanic.describe().to_string())

plt.close()
