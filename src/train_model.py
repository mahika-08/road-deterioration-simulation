import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestRegressor


FILE = "data/road_history.csv"

TRAIN_END = 24
PREDICTION_MONTHS = 6


# -----------------------------
# Load data
# -----------------------------

df = pd.read_csv(FILE)


# -----------------------------
# Create future target
# -----------------------------

future = df[df["month"] == TRAIN_END + PREDICTION_MONTHS][
    ["section_id", "road_condition"]
].copy()

future.rename(
    columns={
        "road_condition": "future_condition"
    },
    inplace=True
)


current = df[df["month"] == TRAIN_END].copy()

current = current.merge(
    future,
    on="section_id",
    how="inner"
)


# What we want to predict:
# deterioration over next 6 months

current["future_deterioration"] = (
    current["road_condition"]
    - current["future_condition"]
)


# -----------------------------
# Features
# -----------------------------

features = [
    "road_age",
    "traffic",
    "rainfall",
    "road_condition",
    "damage_level",
    "months_since_repair",
    "repair_quality"
]

X = current[features]
y = current["future_deterioration"]


# -----------------------------
# Train model
# -----------------------------

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    max_depth=6
)

model.fit(X, y)


# -----------------------------
# Save model + prediction data
# -----------------------------

os.makedirs("results", exist_ok=True)

current["predicted_deterioration"] = model.predict(X)

current["predicted_condition"] = (
    current["road_condition"]
    - current["predicted_deterioration"]
)

# Risk levels
def risk_level(value):

    if value < 5:
        return "LOW"
    elif value < 12:
        return "MEDIUM"
    else:
        return "HIGH"


current["risk"] = current["predicted_deterioration"].apply(
    risk_level
)


current.to_csv(
    "results/predictions.csv",
    index=False
)


joblib.dump(
    model,
    "results/road_model.pkl"
)


print("Model trained successfully.")

print("\nPrediction summary:")

print(
    current[
        [
            "section_id",
            "road_condition",
            "future_condition",
            "predicted_deterioration",
            "predicted_condition",
            "risk"
        ]
    ].head(10)
)

print("\nRisk distribution:")
print(current["risk"].value_counts())