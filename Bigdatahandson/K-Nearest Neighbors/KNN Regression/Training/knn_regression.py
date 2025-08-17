import pandas as pd

data = pd.read_csv("boston.csv")

x = data.iloc[:,:-1]
y = data.iloc[:,-1]

from sklearn.model_selection import train_test_split
# count_i = 0
# acc = 0.0
# count_j = 0
# for i in range(101):
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.20,random_state=77)
    # for j in range(1,6):
from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor(n_neighbors=3)
knn.fit(x_train,y_train)

y_pred = knn.predict(x_test)
from sklearn.metrics import r2_score
r2 = r2_score(y_test,y_pred)
print(r2)
# if acc < r2:
#     acc = r2
#     count_i = i
#     count_j = j
import pickle
model = r"C:\Users\sevug\Documents\AI Projects\Machine Learning\Supervised Learning\K-Nearest Neighbors\KNN Regression\Testing\Knn_regression.pkl"
pickle.dump(knn, open(model, 'wb'))
# print(f'Count i is: {count_i}, count j is {count_j} accuracy is: {acc}')

