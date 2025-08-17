import pickle

model = "random_forest_classifier_model.pkl"
model = pickle.load(open(model,'rb'))

values = "103882 1321.948 554.4242 239.5097 104693 363.6849	0.9019 0.9923 0.5734 0.747 2.3148 0.656"
values = map(float,values.split())
values = [list(values)]
prediction = model.predict(values)
print(prediction[0])