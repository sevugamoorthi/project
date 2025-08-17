import pickle

with open("fish_predicted_model.pkl",'rb') as file:
    model = pickle.load(file)

values = "5.6, 4.6, 9.5, 2.7, 6.8, 5.2"
values = map(float, values.split(','))
values = [list(values)]
prediction = model.predict(values)
print(prediction[0])