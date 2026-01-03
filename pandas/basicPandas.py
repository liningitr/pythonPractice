import pandas as pd
import numpy as np

# /home/ning/dev/github/pythonPractice/pandas/basicPandas.py
# GitHub Copilot
# Simple demo of basic pandas features


# Two core data structures
# 1️⃣ DataFrame (2D table, rows + columns)
# 2️⃣ Series (1D, column)



def main():
    # 1. Create DataFrame from dict
    df = pd.DataFrame({
        "id": [1, 2, 3, 4, 5],
        "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
        "score": [85, 92, np.nan, 88, 76],
        "group": ["A", "B", "A", "B", "A"]
    })
    print("Initial DataFrame:\n", df, "\n")

    # 2. Basic inspection
    print("Head:\n", df.head(), "\n")
    print("Info:")
    df.info()
    print("\nDescribe:\n", df.describe(include="all"), "\n")

    # 3. Selection and indexing
    print("Select columns:\n", df[["name", "score"]], "\n")
    print("Select by label (loc) row 2:\n", df.loc[1], "\n")
    print("Select by position (iloc) first 3 rows:\n", df.iloc[:3], "\n")

    # 4. Filtering
    print("Filter score > 80:\n", df[df["score"] > 80], "\n")

    # 5. Add/modify columns
    df["passed"] = df["score"] >= 80
    df["score_filled"] = df["score"].fillna(df["score"].mean())
    print("After adding columns:\n", df, "\n")

    # 6. GroupBy and aggregation
    grouped = df.groupby("group").agg(
        count=("id", "size"),
        avg_score=("score_filled", "mean"),
        passed_sum=("passed", "sum")
    )
    print("GroupBy aggregation:\n", grouped, "\n")

    # 7. Pivot table
    pivot = pd.pivot_table(df, values="score_filled", index="group", columns="passed", aggfunc="mean")
    print("Pivot table:\n", pivot, "\n")

    # 8. Merge / join
    extra = pd.DataFrame({
        "id": [2, 3, 5],
        "city": ["NY", "LA", "SF"]
    })
    merged = pd.merge(df, extra, on="id", how="left")
    print("Merged DataFrame:\n", merged, "\n")

    # 9. Handling missing data
    print("Rows with any NA:\n", df[df.isna().any(axis=1)], "\n")
    print("Drop rows with NA in 'score':\n", df.dropna(subset=["score"]), "\n")

    # 10. Time series basics
    dates = pd.date_range("2025-01-01", periods=6, freq="D")
    ts = pd.Series([1, 3, np.nan, 2, 5, 4], index=dates, name="value")
    print("Time series:\n", ts, "\n")
    print("Resampled (2-day sum):\n", ts.resample("2D").sum(), "\n")
    print("Fill forward:\n", ts.ffill(), "\n")

    # 11. Read / write CSV
    csv_path = "pandas_demo.csv"
    df.to_csv(csv_path, index=False)
    print(f"Wrote demo CSV to {csv_path}")
    df2 = pd.read_csv(csv_path)
    print("Read back CSV:\n", df2.head(), "\n")

if __name__ == "__main__":
    main()