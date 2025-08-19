import pandas as pd
import pickle

transport_model = "transport_prediction_model.pkl"
inventory_model = "inventor_prediction_model.pkl"
maintenance_model = "maintenance_prediction_model.pkl"

with open(transport_model,'rb') as file:
    transport_model = pickle.load(file)

# Predict time for a new set of routes
new_routes = pd.DataFrame({
    'distance_km': [150, 800],
    'fuel_cost_per_km': [1.0, 1.3],
    'load_tons': [10, 35]
})

predicted_time = transport_model.predict(new_routes)
print(f"Predicted time for new routes: {predicted_time}")
file.close()

with open(inventory_model,'rb') as file:
    inventory_model = pickle.load(file)

# Predict stock needed for new products
new_inventory = pd.DataFrame({
    'stock': [200, 100],
    'demand_rate': [0.5, 1.2]
})

predicted_stock = inventory_model.predict(new_inventory)
print(f"Predicted stock needed: {predicted_stock}")
file.close()

file = open(maintenance_model,'rb')
maintenance_model = pickle.load(file)

# Predict failure rate for new machinery
new_machines = pd.DataFrame({'hours_used': [500, 1000]})
predicted_failure = maintenance_model.predict(new_machines)
print(f"Predicted failure rates: {predicted_failure}")
file.close()
