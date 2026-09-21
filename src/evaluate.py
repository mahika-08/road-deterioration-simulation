import pandas as pd

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error
)

import numpy as np


FILE = "results/predictions.csv"

df = pd.read_csv(FILE)


actual = df["future_deterioration"]
predicted = df["predicted_deterioration"]


mae = mean_absolute_error(
    actual,
    predicted
)

rmse = np.sqrt(
    mean_squared_error(
        actual,
        predicted
    )
)


print("\n" + "=" * 50)
print("ROAD DETERIORATION PREDICTION RESULTS")
print("=" * 50)

print(f"\nMean Absolute Error : {mae:.2f}")
print(f"RMSE                : {rmse:.2f}")


print("\nRisk distribution:")

print(
    df["risk"].value_counts()
)


print("\nHighest predicted-risk sections:")

high_risk = df.sort_values(
    "predicted_deterioration",
    ascending=False
).head(10)


print(
    high_risk[
        [
            "section_id",
            "road_condition",
            "future_condition",
            "predicted_deterioration",
            "risk"
        ]
    ].to_string(index=False)
)


print("\nSimulation completed.")