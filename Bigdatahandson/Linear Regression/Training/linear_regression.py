import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Salary_dataset.csv")

x = data.iloc[:,-2].values.reshape(-1,1)
y = data.iloc[:,-1].values.reshape(-1,1)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train,y_train)

y_pre = lr.predict(x_test)

from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import root_mean_squared_log_error
r2 = r2_score(y_test,y_pre)
mse = mean_squared_error(y_test,y_pre)
rmse = root_mean_squared_log_error(y_test,y_pre)
print(r2)
print(mse)
print(rmse)

x = plt.plot(y_test)
y = plt.plot(y_pre)
plt.xlabel("Actual Value")
plt.ylabel("Predicted Value")
plt.show()

import pickle
model = r"C:\Users\sevug\Documents\AI Projects\Machine Learning\Supervised Learning\Linear Regression\Testing\salary_prediction_model.pkl"
with open(model,'wb') as file:
    pickle.dump(lr,file)
file.close()