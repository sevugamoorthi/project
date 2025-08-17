import pickle
import pandas as pd

model = "random_forest_classifier.pkl"
encoder = "one_hot_encoder.pkl"
model = pickle.load(open(model,'rb'))
ohe = pickle.load(open(encoder,'rb'))
values = "2,bmw 320i,gas,std,two,sedan,rwd,front,101.2,176.8,64.8,54.3,2395,ohc,four,108,mpfi,3.5,2.8,8.8,101,5800,23,29"
values = values.split(',')
columns = "symboling,CarName,fueltype,aspiration,doornumber,carbody,drivewheel,enginelocation,wheelbase,carlength,carwidth,carheight,curbweight,enginetype,cylindernumber,enginesize,fuelsystem,boreratio,stroke,compressionratio,horsepower,peakrpm,citympg,highwaympg"
list = columns.split(',')
# print(list)
df = pd.DataFrame([values],columns=[list])

df = ohe.transform(df[["CarName","fueltype","aspiration","doornumber","carbody","drivewheel","enginelocation","enginetype","cylindernumber","fuelsystem"]])
prediction = model.predict(df)
print(f"Car price is: {prediction[0]}")