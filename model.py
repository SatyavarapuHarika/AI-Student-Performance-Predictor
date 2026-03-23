import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import pickle

# Load data
data = pd.read_csv("student_data.csv")

X = data[['hours_studied', 'attendance']]
y = data['marks']

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
model = RandomForestRegressor()
model.fit(X_scaled, y)

# Save files
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(scaler, open("scaler.pkl", "wb"))

print("Model trained successfully!")