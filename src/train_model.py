import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Load data
df = pd.read_csv("data/laptop_data.csv")

# Remove ID and target column
X = df.drop(["ID", "Price_USD"], axis=1)
y = df["Price_USD"]

# Categorical columns
categorical_features = [
    "Brand",
    "CPU"
]

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)

# Model pipeline
model = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ))
])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)

score = r2_score(y_test, predictions)

print(f"R2 Score: {score:.2f}")

# Save model
joblib.dump(model, "models/model.pkl")

print("Model Saved Successfully")