"""
Docstring for pandas.pandasSeriesBasic

Demonstrates basic usage of pandas.Series: creation, indexing, arithmetic,
aggregation, and boolean selection.

A pandas Series is a one-dimensional labeled array capable of holding any data
type. It is one of the two primary data structures in the pandas library,
the other being the DataFrame. A Series is analogous to a single column in a
spreadsheet or table.

Key components:
- Data: The values stored in the Series (e.g., numbers, strings, Python objects).
- Index: Labels associated with each data value used for identification and
    retrieval. If no index is specified, integer labels starting from 0 are
    assigned automatically.

"""
import pandas as pd
import numpy as np

# Basic Series creation from integers with default index
s1 = pd.Series([10, 20, 30, 40])
print("Series s1:\n", s1, "\n")

# Series creation from a list with custom index
s2 = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
print("Series s2:\n", s2, "\n")

# Series creation from a dictionary (index inferred from keys)
s3 = pd.Series({'x': 1, 'y': 2, 'z': 3})
print("Series s3:\n", s3, "\n") 

# Accessing elements by label and by integer position
print("s2['b']:", s2['b'])
print("s2.iloc[2]:", s2.iloc[2], "\n")  


