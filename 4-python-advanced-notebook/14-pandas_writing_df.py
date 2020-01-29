#!/usr/bin/env python3

# install pyarrow, pandavro

import pandas as pd
import pandavro as pdx


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


# Make sure to install xlrd with pip3!!!
df = pd.read_csv('data/insurance.csv', header=0)

df.to_excel('data/created_train.xlsx')
df.to_x('data/created_train.xlsx')
df.to_json('data/created_train.json', orient='records')
# df.to_parquet('data/created_train.parquet')
pdx.to_avro('data/created_train.avro', df)
