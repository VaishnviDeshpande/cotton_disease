<<<<<<< HEAD
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("cotton_crop_disease_cleaned.csv")

# Correct column names
stage_col = "Crop_Stage"
target_col = "Crop_Disease"
features = ["Crop_Stage", "Temperature(°C)", "Humidity(%)", "Soil_Moisture(%)", "Rainfall(mm)", "Soil_pH"]

# Label Encoding
stage_encoder = LabelEncoder()
df["Stage_Enc"] = stage_encoder.fit_transform(df[stage_col])

disease_encoder = LabelEncoder()
df["Disease_Enc"] = disease_encoder.fit_transform(df[target_col])

# Preparing X and y
X = df[["Stage_Enc", "Temperature(°C)", "Humidity(%)", "Soil_Moisture(%)", "Rainfall(mm)", "Soil_pH"]]
y = df["Disease_Enc"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and encoders
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(stage_encoder, open("stage_encoder.pkl", "wb"))
pickle.dump(disease_encoder, open("disease_encoder.pkl", "wb"))

print("Model training completed!")
print("Files generated: model.pkl, stage_encoder.pkl, disease_encoder.pkl")
=======
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("cotton_crop_disease_cleaned.csv")

# Correct column names
stage_col = "Crop_Stage"
target_col = "Crop_Disease"
features = ["Crop_Stage", "Temperature(°C)", "Humidity(%)", "Soil_Moisture(%)", "Rainfall(mm)", "Soil_pH"]

# Label Encoding
stage_encoder = LabelEncoder()
df["Stage_Enc"] = stage_encoder.fit_transform(df[stage_col])

disease_encoder = LabelEncoder()
df["Disease_Enc"] = disease_encoder.fit_transform(df[target_col])

# Preparing X and y
X = df[["Stage_Enc", "Temperature(°C)", "Humidity(%)", "Soil_Moisture(%)", "Rainfall(mm)", "Soil_pH"]]
y = df["Disease_Enc"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and encoders
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(stage_encoder, open("stage_encoder.pkl", "wb"))
pickle.dump(disease_encoder, open("disease_encoder.pkl", "wb"))

print("Model training completed!")
print("Files generated: model.pkl, stage_encoder.pkl, disease_encoder.pkl")
>>>>>>> 35b4f3fbb49cc6be6f07b36a97432ead70bbdfb8
