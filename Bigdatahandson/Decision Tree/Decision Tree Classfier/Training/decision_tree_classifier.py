import pandas as pd

data = pd.read_csv("drug200.csv")

df = pd.DataFrame(data)

x = df.iloc[:,:-1]
y = df.iloc[:,-1]

print(x)
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse_output=False)
x = ohe.fit_transform(x[["Sex","BP","Cholesterol"]])
x_df = pd.DataFrame(x,columns=ohe.get_feature_names_out(["Sex","BP","Cholesterol"]))
print(pd.DataFrame(x_df))

# from sklearn.preprocessing import LabelEncoder
# lb = LabelEncoder()
# x["Sex"] = lb.fit_transform(x["Sex"])
# x["Cholesterol"] = lb.fit_transform(x["Cholesterol"])
# x["BP"] = lb.fit_transform(x["BP"])


# count = 0
# max_acc = 0.0
# cm = 0
# count_j = 0
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
# for i in range(101):
x_train,x_test,y_train,y_test = train_test_split(x_df,y,test_size=0.15,random_state=45)
    # for j in range(101):
from sklearn.tree import DecisionTreeClassifier
dc = DecisionTreeClassifier()
dc.fit(x_train,y_train)

y_pred = dc.predict(x_test)
cm = confusion_matrix(y_test, y_pred)

print(dc.score(x_test,y_test))
# acc = dc.score(x_test,y_test)

#         if acc > max_acc:
#             max_acc = acc
#             count = i
#             count_j = j
#             cm = cm
# print(f'Count is: {count},count of j: {count_j} accuracy is: {max_acc}, confusion matrix: {cm}')

import pickle
model = r"C:\Users\sevug\Documents\AI Projects\Machine Learning\Supervised Learning\Decision Tree\Decision Tree Classfier\Testing\decision_tree_classifier.pkl"
ohe_file = r"C:\Users\sevug\Documents\AI Projects\Machine Learning\Supervised Learning\Decision Tree\Decision Tree Classfier\Testing\ohe_encoder.pkl"
pickle.dump(dc, open(model,'wb'))
pickle.dump(ohe,open(ohe_file,'wb'))

