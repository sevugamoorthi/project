import pickle

model = "knn_classifier_model.pkl"
model= pickle.load(open(model,'rb'))

values = "19.9,13.8,15,16.2,2.9322,1.8792"
values = map(float,values.split(','))
values = [list(values)]

prediction = model.predict(values)
print(prediction[0])