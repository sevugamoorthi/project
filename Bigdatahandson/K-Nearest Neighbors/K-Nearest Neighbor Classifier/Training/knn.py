import pandas as pd

data = pd.read_csv("Fish.csv")

x = data.iloc[:,1:]
y = data.iloc[:,0]

# max_acc = 0
# count_i = 0
# count_j = 0
# for i in range(1,101):
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.15,random_state=20)
    # for j in range(1,6):
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train,y_train)
#
y_pred = knn.predict(x_test)
acc = knn.score(x_test,y_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
# print(cm)
# if acc > max_acc:
#     max_acc = acc
#     count_i = i
#     count_j = j
# print(f"Acc is {max_acc}, count i is {count_i} and count j is {count_j}")

import pickle
model = r"C:\Users\sevug\Documents\AI Projects\Machine Learning\Supervised Learning\K-Nearest Neighbors\K-Nearest Neighbor Classifier\Testing\knn_classifier_model.pkl"
model = pickle.dump(knn,open(model,"wb"))

