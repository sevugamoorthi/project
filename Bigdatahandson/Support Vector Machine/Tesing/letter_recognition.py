import pickle
model = "svm.pkl"
model = pickle.load(open(model,'rb'))
values = "5,9,7,6,4,4,10,3,4,9,10,9,5,8,1,8"
values = map(float,values.split(','))
values = [list(values)]
prediction = model.predict(values)
print(prediction[0])