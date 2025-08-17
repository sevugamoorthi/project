import pickle

poly_model = "poly_model.pkl"

model = pickle.load(open(poly_model,'rb'))

values = [-4.316559446725467,
-4.213984764590729,
-3.9496610890515707,
-3.578553716228682,
-3.455711698065576,
-3.1084401208909964,
-3.0813033243034563,
-2.672460827006454,
-2.652286792936049,
-2.6514980333001315]
for value in values:
    value = [[value]]
    prediction = model.predict(value)
    print(f"If the temperate is: {value[0][0]}, then {prediction[0][0]} units can be sale!")