import nltk
nltk.download('wordnet')
import pandas as pd

data = pd.read_csv("spam.csv")

from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import string
import re

stop = set(stopwords.words(("english")))
punc = set(string.punctuation)
lemmatizer = WordNetLemmatizer()

x = data.iloc[:,1]
y = data.iloc[:,0]

def clean(msg):
    msg = " ".join([i for i in msg.lower().split() if i not in stop])
    msg = "".join([i for i in msg if i not in punc])
    msg = "".join([lemmatizer.lemmatize(i) for i in msg])
    msg = re.sub(r"\d+","",msg)
    msg = re.sub(r"\s+"," ",msg)
    return msg


for i in range(len(x)):
    x[i] = clean(x[i])

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(x)

count = 0
acc = 0.0
from sklearn.model_selection import  train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import r2_score

nb = MultinomialNB()
# for i in range(101):
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25,random_state=37)
nb.fit(x_train,y_train)
y_pred = nb.predict(x_test)
score = nb.score(x_test,y_test)
print(score)
import pickle
model = r"C:\Users\sevug\Documents\AI Projects\Machine Learning\Supervised Learning\Naive Bayes\Testing\naive_bayes.pkl"
pickle.dump(nb,open(model,'wb'))

vector = r"C:\Users\sevug\Documents\AI Projects\Machine Learning\Supervised Learning\Naive Bayes\Testing\count_vectorizer.pkl"
pickle.dump(vectorizer,open(vector,'wb'))
# if score> acc:
#     count = i
#     acc = score

# print(f"Count: {count}, accuracy: {acc}")

