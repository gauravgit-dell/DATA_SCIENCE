import pandas as pd 
df = pd.read_csv("/Users/gaurav/Downloads/customer.csv")

print("null values")
print(df.isnull().sum())