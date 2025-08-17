import pandas as pd

data = pd.read_excel("Pumpkin_Seeds_Dataset.xlsx")
# df = pd.DataFrame(data)
# df = pd.unique(data["Class"])

x = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

count_i = 0
count_j = 0
acc = 0.0

# for i in range(101):
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.20,random_state=100)
# for j in range(101):
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=5,criterion='gini',random_state=100)
rf.fit(x_train,y_train)

y_pred = rf.predict(x_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)
score = rf.score(x_test,y_test)
print(score)
# if acc < score:
#     acc = score
#     count_i = i
#     count_j = j

# print(f"Count i is: {count_i}, count j is: {count_j}, acc is: {acc}")
import pickle

model = r"C:\Users\sevug\Documents\AI Projects\Machine Learning\Supervised Learning\Random Forest Classifier\Random Foreset Classifier\Testing\random_forest_classifier_model.pkl"
with open(model,"wb") as file:
    pickle.dump(rf,file)
file.close()
# model = pickle.load(open(model,"rb"))

