import pandas as pd

# Load the CSV file
df = pd.read_csv("student_data.csv")

print("Original Dataset")
print(df)

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(0)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Remove extra spaces
df["Name"] = df["Name"].str.strip()

# Convert names to uppercase
df["Name"] = df["Name"].str.upper()

# Standardize gender values
df["Gender"] = df["Gender"].replace({
    "M": "Male",
    "F": "Female",
    "male": "Male",
    "female": "Female"
})

print("\nCleaned Dataset")
print(df)

# Check missing values after cleaning
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Check duplicates after cleaning
print("\nDuplicate rows after cleaning:")
print(df.duplicated().sum())

# Save the cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("\nData cleaning completed successfully.")
