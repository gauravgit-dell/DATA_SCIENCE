# Linear Regression

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Load dataset
df = pd.read_csv("linear_regression_data.csv")

# Display dataset
print("Dataset:")
print(df)

# Select input and output columns
X = df[["Hours"]]
y = df["Marks"]

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Linear Regression model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE  :", mae)
print("MSE  :", mse)
print("RMSE :", rmse)
print("R2 Score:", r2)

# Coefficients
print("\nIntercept:", model.intercept_)
print("Coefficient:", model.coef_[0])

# Plot
plt.scatter(X_test, y_test)
plt.plot(X_test, y_pred)
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.title("Linear Regression")
plt.show()
