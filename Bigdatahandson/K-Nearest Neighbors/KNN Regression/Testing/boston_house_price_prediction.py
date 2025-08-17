import pickle

model = "Knn_regression.pkl"
model = pickle.load(open(model,'rb'))
values = "0.17004,12.50,7.870,0,0.5240,6.0040,85.90,6.5921,5,311.0,15.20,386.71,17.10"
values = map(float,values.split(","))

values = [list(values)]
prediction = model.predict(values)
print(prediction)