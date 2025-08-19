import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate a sample dataset for transportation routes, inventory, and maintenance
np.random.seed(42)

# Sample data: columns for distance, fuel cost, time (hours), and load (tons)
transport_data = pd.DataFrame({
    'distance_km': np.random.randint(100, 1000, 100),
    'fuel_cost_per_km': np.random.uniform(0.5, 1.5, 100),
    'time_hours': np.random.uniform(1, 10, 100),
    'load_tons': np.random.uniform(5, 50, 100)
})

# Sample inventory data for warehousing and manufacturing
inventory_data = pd.DataFrame({
    'product_id': np.arange(1, 101),
    'stock': np.random.randint(50, 500, 100),
    'demand_rate': np.random.uniform(0.1, 2.0, 100)  # Units sold per day
})

# Sample maintenance data for mining and manufacturing machinery
maintenance_data = pd.DataFrame({
    'machine_id': np.arange(1, 51),
    'hours_used': np.random.uniform(100, 5000, 50),
    'failure_rate': np.random.uniform(0.01, 0.1, 50)  # Failure probability
})

# Route optimization using Linear Regression (for simplicity)
X_transport = transport_data[['distance_km', 'fuel_cost_per_km', 'load_tons']]
y_transport = transport_data['time_hours']

model_transport = LinearRegression()
model_transport.fit(X_transport, y_transport)

# Inventory management using Decision Tree Regressor
X_inventory = inventory_data[['stock', 'demand_rate']]
y_inventory = inventory_data['stock']

model_inventory = DecisionTreeRegressor()
model_inventory.fit(X_inventory, y_inventory)

# Predictive maintenance using a simple Neural Network
X_maintenance = maintenance_data[['hours_used']]
y_maintenance = maintenance_data['failure_rate']

model_maintenance = Sequential()
model_maintenance.add(Dense(16, input_dim=1, activation='relu'))
model_maintenance.add(Dense(8, activation='relu'))
model_maintenance.add(Dense(1, activation='sigmoid'))  # Output is a probability

model_maintenance.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model_maintenance.fit(X_maintenance, y_maintenance, epochs=500, verbose=1)

import pickle

model_for_transport = r"C:\Users\sevug\Documents\Academor Project\Testing\transport_prediction_model.pkl"
model_for_inventory = r"C:\Users\sevug\Documents\Academor Project\Testing\inventor_prediction_model.pkl"
model_for_maintenance = r"C:\Users\sevug\Documents\Academor Project\Testing\maintenance_prediction_model.pkl"

with open(model_for_transport,'wb') as file:
    pickle.dump(model_transport, file)
file.close()

with open(model_for_inventory,'wb') as file:
    pickle.dump(model_inventory, file)
file.close()

with open(model_for_maintenance,'wb') as file:
    pickle.dump(model_maintenance, file)
file.close()

"""
Explanation of the Python Program
Route Optimization:
I used a linear regression model to optimize transport routes, predicting how much time the transport will take based on distance, fuel cost, and the load.

Inventory Management:
A decision tree regressor predicts the optimal stock level required for products in warehousing and manufacturing based on the current stock and demand rate.

Predictive Maintenance:
A neural network is used to predict failure rates for machinery based on their hours of usage, providing insights into when preventive maintenance should be done in mining and manufacturing industries.
"""
