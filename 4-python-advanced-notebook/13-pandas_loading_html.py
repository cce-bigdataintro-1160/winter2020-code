#!/usr/bin/env python3

import pandas as pd


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


html_tables = pd.read_html('https://www.dividend.com/dividend-stocks/high-dividend-yield-stocks/')

pretty_print("High Dividend Stocks", html_tables[0].to_string())
pretty_print("High Dividend Columns", html_tables[0].columns)
pretty_print("High Dividend Info", html_tables[0].info())
pretty_print("High Dividend Description", html_tables[0].describe().to_string())
