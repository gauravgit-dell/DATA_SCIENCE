import pandas as pd

# Read the CSV file
df = pd.read_csv("student_data.csv")

# Display the original dataset
print("\nOriginal Dataset")
print(df)

# Filtering
print("\nStudents with marks greater than 80")
filtered_data = df[df["Marks"] > 80]
print(filtered_data)

# Grouping
print("\nGrouping data according to gender")
grouped_data = df.groupby("Gender")
print(grouped_data.first())

# Aggregation
print("\nAverage marks")
print(df["Marks"].mean())

print("\nMaximum marks")
print(df["Marks"].max())

print("\nMinimum marks")
print(df["Marks"].min())

print("\nTotal marks")
print(df["Marks"].sum())

# Sorting
print("\nSorting data according to marks")
sorted_data = df.sort_values(by="Marks", ascending=False)
print(sorted_data)

# Reshaping
print("\nPivot table")

pivot_table = df.pivot_table(
    values="Marks",
    index="Gender",
    aggfunc="mean"
)

print(pivot_table)

# Saving the transformed data
sorted_data.to_csv("transformed_data.csv", index=False)

print("\nData wrangling completed successfully.")