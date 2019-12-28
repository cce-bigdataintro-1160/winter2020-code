#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


titanic = pd.read_json('data/food_trucks.json')

pretty_print("Food Trucks dataframe", titanic.to_string())
pretty_print("Food Trucks columns", titanic.columns)
pretty_print("Food Trucks info", titanic.info())
pretty_print("Food Trucks description", titanic.describe().to_string())

plt.close()
