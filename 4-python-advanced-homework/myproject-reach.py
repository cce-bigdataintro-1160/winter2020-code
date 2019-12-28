#!/usr/bin/env python3

# To run:
# python3 myproject.py --dataset_path data/boston/housing.data --dataset_sep \s+ --column_names CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT,MEDV

import argparse

import matplotlib.pyplot as plt
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--dataset_path', help='Dataset Path')
parser.add_argument('--dataset_sep', default=',', help='Dataset separator')
parser.add_argument('--column_names', help='Column Names')
args = parser.parse_args()

# We're now creating a dataframe straight from a data file
df = pd.read_csv(filepath_or_buffer=args.dataset_path,
                 sep=args.dataset_sep,
                 header=0)

df.columns = args.column_names.split(',')

print(df.info())
print(df.describe())
print(df.corr())

plt.plot(df['CRIM'])
plt.savefig(f'crime.png')
plt.clf()

plt.scatter(df['MEDV'], df['CRIM'])
plt.savefig(f'crime_to_value.png')
