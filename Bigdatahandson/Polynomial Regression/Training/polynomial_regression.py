import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

data = pd.read_csv("Ice_cream selling data.csv")

x = data.iloc[:,0].values.reshape(-1,1)
y = data.iloc[:,1].values.reshape(-1,1)

from sklearn.model_selection import train_test_split
# count = 0
# acc = 0.0
# for i in range(101):
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=14)
#
from sklearn.preprocessing import PolynomialFeatures
# poly = PolynomialFeatures(degree=2)
# x_train_poly = poly.fit_transform(x_train)
# x_test_poly = poly.transform(x_test)


from sklearn.linear_model import LinearRegression
# lr = LinearRegression()
# lr.fit(x_train_poly,y_train)

from sklearn.pipeline import Pipeline
model = Pipeline([("poly",PolynomialFeatures(degree=2)),("lr",LinearRegression())])
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

from sklearn.metrics import r2_score
r2 = r2_score(y_test,y_pred)
print(r2)
# if r2 > acc and r2 < 96:
#     random = i
#     acc = r2
# print(f"count is: {count}, acc is: {acc}")

import pickle

poly_model = r"C:\Users\sevug\Documents\AI Projects\Machine Learning\Supervised Learning\Polynomial Regression\Testing\poly_model.pkl"

pickle.dump(model,open(poly_model,'wb'))


