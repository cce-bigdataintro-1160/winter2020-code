#!/usr/bin/env python3

import numpy as np
import pandas as pd


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')

# We finally get to look at Pandas! This is how we create a Series manually. A series is just like a numpy vector but
# now we have labeled fields
orders = pd.Series(data=[300.50, 60, 123.40, 60, np.nan],
                   index=['Customer 1', 'Customer 2', 'Customer 3', 'Customer 4', 'Customer 5'])

# A few basic functions to printing series
pretty_print("This is how we can print a Series", orders.to_string())
pretty_print("This is how we can select the first line only", orders.head(n=1))

# Now we see the functions that can quickly provide insights on a dataset
pretty_print("This is how we can see the labels of each value", orders.index)
pretty_print("Pandas can automagically infer the type for a Series by checking all values for us", orders.dtypes)
pretty_print("Printing the shape of a Series", orders.shape)
pretty_print("Describing a Series", orders.describe())

# A few more advanced methods capable of transforming our series
pretty_print("Sorting all values in a series", orders.sort_values())
pretty_print("Counting occurrences of different values in a series", orders.value_counts())
pretty_print("Checking for null elements in a Series", orders.isnull())
