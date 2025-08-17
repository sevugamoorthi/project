import pickle
model = "naive_bayes.pkl"
model = pickle.load(open(model,'rb'))
vectorizer = "count_vectorizer.pkl"
vectorizer = pickle.load(open(vectorizer,'rb'))
values = ["Had your mobile 11 months or more? U R entitled to Update to the latest colour mobiles with camera for Free! Call The Mobile Update Co FREE on 08002986030"]
from nltk.stem.wordnet import WordNetLemmatizer
# from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import string
stop = set(stopwords.words(("english")))
punc = set(string.punctuation)
lemmatizer = WordNetLemmatizer()
import re
def clean(msg):
    msg = " ".join([i for i in msg.lower().split() if i not in stop])
    msg = "".join([i for i in msg if i not in punc])
    msg = "".join([lemmatizer.lemmatize(i) for i in msg])
    msg = re.sub(r"\d+","",msg)
    msg = re.sub(r"\s+"," ",msg)
    return msg

for i in range(len(values)):
    values[i] = clean(values[i])

vectorizer = vectorizer.transform(values)

prediction = model.predict(vectorizer)
print(prediction[0])