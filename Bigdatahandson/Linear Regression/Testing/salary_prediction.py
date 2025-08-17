import pickle
model = "salary_prediction_model.pkl"

with open(model,'rb') as file:
    model = pickle.load(file)

years = [4.1, 4, 6, 8, 2.4356, 8.4, 2, 3]
for year in years:
    year = [[year]]
    prediction = model.predict(year)
    print(f"Predicted of salary of given year :{prediction[0][0]}")
    file.close()