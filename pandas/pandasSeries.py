import pandas as pd
"""
pandasSeries.py

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

This module demonstrates:
- Creating a Series from a Python list with a custom index.
- Creating a Series from a dictionary (index inferred from keys).
- Accessing elements by label and by integer position (.iloc).
- Performing arithmetic operations on a Series and computing aggregates
    (sum, mean).
- Selecting elements using boolean indexing.
"""


def main():
    # Series from a list with a custom index
    s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
    print("Series from list:")
    print(s, end="\n\n")

    # Series from a dict (index inferred from keys)
    s2 = pd.Series({"x": 1, "y": 2, "z": 3})
    print("Series from dict:")
    print(s2, end="\n\n")

    # Access by label and position
    print("s['b']:", s["b"])
    print("s.iloc[2]:", s.iloc[2], end="\n\n")

    # Arithmetic and aggregation
    print("s + 5:")
    print(s + 5, end="\n\n")
    print("sum:", s.sum(), "mean:", s.mean(), end="\n\n")

    # Boolean indexing
    print("Values > 15:")
    print(s[s > 15])

if __name__ == "__main__":
    main()