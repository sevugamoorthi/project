import pandas as pd

data = pd.read_csv("letter-recognition.csv")

x = data.iloc[:,1:]
y = data.iloc[:,0]

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# count = 0
# count_j = 0
# acc = 0.0
# for i in range(51):
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25,random_state=19)
# for j in range(51):
svc = SVC(kernel='poly',degree=3,C=1.0)
svc.fit(x_train,y_train)

y_pred = svc.predict(x_test)
score = svc.score(x_test,y_test)
print(score)
#     if score > acc:
#         count = i
#         # count_j = j
#         acc = score
# print(f'count: {count}, Count_j: {count_j}, accuracy: {acc}')
import pickle
model = r"C:\Users\sevug\Documents\AI Projects\Machine Learning\Supervised Learning\Support Vector Machine\Tesing\svm.pkl"
pickle.dump(svc,open(model,'wb'))

