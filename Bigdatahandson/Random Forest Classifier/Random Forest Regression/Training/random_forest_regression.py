import pandas as pd

data = pd.read_csv("CarPrice_Assignment.csv")
df = pd.DataFrame(data)
# df.drop(columns=["CarName"],inplace=True)
# print(df)
x = df.iloc[:,1:-1]
# print(x)
y = df.iloc[:,-1]
# print(y)
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse_output=False)
for column in df.select_dtypes("object"):
    print(column)
print(x)
x = ohe.fit_transform(x[["CarName","fueltype","aspiration","doornumber","carbody","drivewheel","enginelocation","enginetype","cylindernumber","fuelsystem"]])
print(x)
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor
count = 0
count_j = 0
acc = 0.0
# for i in range(101):
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=80)
# for j in range(101):
rf = RandomForestRegressor(n_estimators=5,criterion='squared_error',random_state=85)
rf.fit(x_train,y_train)

y_pred = rf.predict(x_test)

from sklearn.metrics import r2_score,mean_squared_error
r2 = r2_score(y_test,y_pred)
mse = mean_squared_error(y_test,y_pred)
# if r2 > acc:
#     count = i
#     count_j = j
#     acc = r2
import pickle

model = r"C:\Users\sevug\Documents\AI Projects\Machine Learning\Supervised Learning\Random Forest Classifier\Random Forest Regression\Testing\random_forest_classifier.pkl"
encoder = r"C:\Users\sevug\Documents\AI Projects\Machine Learning\Supervised Learning\Random Forest Classifier\Random Forest Regression\Testing\one_hot_encoder.pkl"
pickle.dump(rf, open(model, 'wb'))
pickle.dump(ohe,open(encoder,'wb'))
print(r2)
# print(f"Count is: {count}, j is: {count_j}, accuracy is: {acc}")



