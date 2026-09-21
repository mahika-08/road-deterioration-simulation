import numpy as np
import pandas as pd


# -----------------------------
# Settings
# -----------------------------

INPUT_FILE = "data/road_history.csv"
OUTPUT_FILE = "data/road_history.csv"

np.random.seed(42)


# -----------------------------
# Load generated road data
# -----------------------------

df = pd.read_csv(INPUT_FILE)

df["road_condition"] = 0.0
df["damage_level"] = 0.0
df["previous_condition"] = 0.0
df["repair_event"] = 0
df["repair_quality"] = 0.0
df["months_since_repair"] = 0


# -----------------------------
# Simulate each road section
# -----------------------------

for section_id in df["section_id"].unique():

    section_data = df[df["section_id"] == section_id].index

    # Starting condition
    condition = np.random.uniform(80, 100)

    months_since_repair = np.random.randint(0, 12)

    for index in section_data:

        row = df.loc[index]

        previous_condition = condition

        # -----------------------------
        # Natural deterioration
        # -----------------------------

        # Traffic effect
        traffic_effect = row["traffic"] / 10000 * 1.5

        # Rainfall effect
        rainfall_effect = row["rainfall"] / 150 * 1.5

        # Older roads deteriorate slightly faster
        age_effect = row["road_age"] / 10 * 0.8

        # Existing damage increases future deterioration
        damage_effect = max(0, (100 - condition) / 100) * 2

        # Small random variation
        random_effect = np.random.uniform(0, 0.8)

        deterioration = (
            traffic_effect
            + rainfall_effect
            + age_effect
            + damage_effect
            + random_effect
        )

        # -----------------------------
        # Repair event
        # -----------------------------

        repair_event = 0
        repair_quality = 0.0

        # A repair becomes more likely when
        # the road condition becomes poor.
        if condition < 45 and np.random.random() < 0.35:

            repair_event = 1

            repair_quality = np.random.uniform(0.5, 0.9)

            # Repair improves condition,
            # but does not make the road completely new.
            condition += 35 * repair_quality

            condition = min(condition, 90)

            months_since_repair = 0

        else:
            condition -= deterioration
            months_since_repair += 1

        # Keep condition within 0–100
        condition = np.clip(condition, 0, 100)

        # -----------------------------
        # Calculate damage level
        # -----------------------------

        damage_level = 100 - condition

        # -----------------------------
        # Store values
        # -----------------------------

        df.loc[index, "previous_condition"] = round(
            previous_condition, 2
        )

        df.loc[index, "road_condition"] = round(
            condition, 2
        )

        df.loc[index, "damage_level"] = round(
            damage_level, 2
        )

        df.loc[index, "repair_event"] = repair_event

        df.loc[index, "repair_quality"] = round(
            repair_quality, 2
        )

        df.loc[index, "months_since_repair"] = months_since_repair


# -----------------------------
# Save updated dataset
# -----------------------------

df.to_csv(OUTPUT_FILE, index=False)


print("Road deterioration simulation completed.")

print(f"Total records: {len(df)}")
print(f"Saved to: {OUTPUT_FILE}")

print("\nSample data:")
print(
    df[
        [
            "section_id",
            "month",
            "road_condition",
            "damage_level",
            "repair_event",
            "months_since_repair"
        ]
    ].head(15)
)


# -----------------------------
# Show one road's progression
# -----------------------------

example_section = "S001"

print(f"\nCondition history for {example_section}:")

history = df[df["section_id"] == example_section][
    ["month", "road_condition", "damage_level", "repair_event"]
]

print(history.to_string(index=False))