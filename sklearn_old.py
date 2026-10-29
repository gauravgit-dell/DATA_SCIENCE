from sklearn.preprocessing import MinMaxScaler

data = [[20, 20000], [25, 50000], [30, 80000]]

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

print(scaled_data)