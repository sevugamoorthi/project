import pandas as pd

data = pd.read_csv("Fish.csv")

# from sklearn.preprocessing import LabelEncoder
# lb = LabelEncoder()
# data["Species"] = lb.fit_transform(data["Species"])

x = data.iloc[:,1:].values
y = data.iloc[:,0].values

# y = pd.get_dummies(y,columns=["Species"],prefix="")
# y = y.replace({"_Bream":{True:1,False:0},"_Parkki":{True:1,False:0},"_Perch":{True:1,False:0},"_Pike":{True:1,False:0},"_Roach":{True:1,False:0},"_Smelt":{True:1,False:0},"_Whitefish":{True:1,False:0}})

# max_acc = 0.0
# count_i = 0
# for i in range(101):
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25,random_state=64)

from sklearn.preprocessing import StandardScaler
sd = StandardScaler()
x_train = sd.fit_transform(x_train)
x_test = sd.transform(x_test)


from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(x_train,y_train)

y_pred = lr.predict(x_test)
# print(f"Probability: {lr.predict_proba(x_test)}")
print(f"Score is: {lr.score(x_test,y_test)}")
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(f"cm is: {cm}")
    # if max_acc < acc:
    #     max_acc = acc
    #     count_i = i
# print(max_acc,count_i)
import pickle

model = r"C:\Users\sevug\Documents\AI Projects\Machine Learning\Supervised Learning\Logistic Regression\Testing\fish_predicted_model.pkl"

with open(model,'wb')as file:
    pickle.dump(lr,file)
file.close()