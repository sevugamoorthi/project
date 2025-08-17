import pandas as pd

data = pd.read_csv("boston.csv")

x = data.iloc[:,:-1]
y = data.iloc[:,-1]

count = 0
count_j = 0
acc = 0.0
from sklearn.model_selection import train_test_split
# for i in range(101):
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25,random_state=50)
# for j in range(101):
from sklearn.tree import DecisionTreeRegressor
dt = DecisionTreeRegressor(random_state=87)
dt.fit(x_train,y_train)

y_pred = dt.predict(x_test)

from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
r2 = r2_score(y_test,y_pred)
mse = mean_squared_error(y_pred,y_test)
print(mse)
print(r2)
print(dt.score(x_test,y_test))
# if r2 > acc:
#     count = i
#     acc = r2
#     count_j = j

# print(f"count: {count},accuracy: {acc}, count_j:{count_j}")
import pickle
model = r"C:\Users\sevug\Documents\AI Projects\Machine Learning\Supervised Learning\Decision Tree\Decision Tree Regression\Tesing\decision_tree_regression.pkl"
pickle.dump(dt,open(model,'wb'))
