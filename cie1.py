import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    "Year": [
        1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006,
        2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
        2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022
    ],

    "Annual_Revenue": [
        13.3, 14.2, 14.9, 15.4, 17.1, 18.6, 19.1, 20.9,
        22.8, 23.5, 22.7, 24.1, 27.0, 27.6, 28.1, 27.4,
        25.4, 24.6, 22.8, 21.3, 21.4, 19.2, 23.2, 23.2
    ],

    "Growth_Rate": [
        np.nan, 7, 4, 4, 11, 8, 3, 9,
        9, 3, -3, 6, 12, 2, 2, -2,
        -7, -3, -7, -7, 1, -10, 21, 0
    ],

    "Q1": [
        np.nan, np.nan, np.nan, np.nan, 3.8, 4.4, 4.8, 4.9,
        5.3, 5.6, 5.1, 5.6, 6.1, 6.5, 6.6, 6.7,
        6.0, 5.9, 5.7, 5.1, 5.0, 4.7, 5.1, 5.7
    ],

    "Q2": [
        np.nan, np.nan, np.nan, np.nan, 4.3, 4.7, 5.1, 5.4,
        5.8, 6.1, 5.6, 5.9, 6.9, 6.9, 7.1, 7.2,
        6.5, 6.3, 6.0, 5.4, 5.3, 3.8, 5.9, 5.7
    ],

    "Q3": [
        np.nan, np.nan, np.nan, np.nan, 4.5, 4.9, 5.3, 5.5,
        5.9, 6.3, 6.0, 6.3, 7.2, 7.2, 7.3, 7.0,
        6.6, 6.4, 5.8, 5.4, 5.6, 5.4, 6.2, 5.9
    ],

    "Q4": [
        np.nan, np.nan, np.nan, 3.0, 4.6, 4.5, 3.9, 5.1,
        5.8, 5.6, 6.0, 6.2, 6.8, 7.0, 7.1, 6.6,
        6.3, 6.0, 5.3, 5.4, 5.4, 5.3, 6.0, 5.9
    ]
}

df = pd.DataFrame(data)

# Display dataset
print(df)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Calculate year-to-year revenue change
df["Revenue_Change"] = df["Annual_Revenue"].diff()

# Calculate growth independently from annual revenue
df["Calculated_Growth"] = (
    df["Annual_Revenue"].pct_change() * 100
)

# Calculate quarterly total only where all quarters exist
quarters = ["Q1", "Q2", "Q3", "Q4"]

df["Quarterly_Total"] = df[quarters].sum(
    axis=1,
    min_count=4
)

# Difference between quarterly total and annual reported revenue
df["Difference"] = (
    df["Quarterly_Total"] - df["Annual_Revenue"]
)

print("\nQuarterly Comparison:")
print(
    df[
        ["Year", "Annual_Revenue",
         "Quarterly_Total", "Difference"]
    ].dropna(subset=["Quarterly_Total"])
)