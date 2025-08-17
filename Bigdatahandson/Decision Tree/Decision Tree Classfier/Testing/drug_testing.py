import pickle
import pandas as pd
model = "decision_tree_classifier.pkl"
ohe_file = "ohe_encoder.pkl"

load_model = pickle.load(open(model,'rb'))
label = pickle.load(open(ohe_file,'rb'))
values = "43,M,HIGH,HIGH,13.972"
#
values = values.split(",")
df = pd.DataFrame([values],columns=["Age","Sex","BP","Cholesterol","Na_to_K"])
df = label.transform(df[["Sex","BP","Cholesterol"]])

predictions = load_model.predict(df)
print(predictions)