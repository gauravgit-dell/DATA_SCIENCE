from sklearn.preprocessing import MinMaxScaler
data = {[20,20000], [25,50000], [30,80000]}
scalar = MinMaxScaler()
normdata = scalar.fit_transform(data)
print(normdata)