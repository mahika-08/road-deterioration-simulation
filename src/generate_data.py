import os
import numpy as np
import pandas as pd


# -----------------------------
# Configuration
# -----------------------------

NUM_SECTIONS = 100
NUM_MONTHS = 36
RANDOM_SEED = 42

np.random.seed(RANDOM_SEED)


# -----------------------------
# Create road sections
# -----------------------------

def create_road_sections():
    sections = []

    for i in range(1, NUM_SECTIONS + 1):

        road_type = np.random.choice(
            ["Residential", "Main Road", "Highway", "Industrial"],
            p=[0.30, 0.35, 0.20, 0.15]
        )

        # Road age in years
        road_age = np.random.randint(1, 16)

        # Average daily traffic
        if road_type == "Residential":
            traffic = np.random.randint(1000, 5000)

        elif road_type == "Main Road":
            traffic = np.random.randint(5000, 15000)

        elif road_type == "Highway":
            traffic = np.random.randint(15000, 40000)

        else:
            traffic = np.random.randint(7000, 20000)

        # Initial road condition
        initial_condition = np.random.uniform(75, 98)

        sections.append({
            "section_id": f"S{i:03d}",
            "road_type": road_type,
            "road_age": road_age,
            "traffic": traffic,
            "initial_condition": round(initial_condition, 2)
        })

    return sections


# -----------------------------
# Generate monthly rainfall
# -----------------------------

def generate_rainfall(month):
    """
    Simulates monthly rainfall.

    Months 1-12 represent one year.
    Rainfall is higher during the middle months.
    """

    month_in_year = ((month - 1) % 12) + 1

    # Simulated seasonal pattern
    rainfall_pattern = {
        1: 25,
        2: 20,
        3: 25,
        4: 35,
        5: 55,
        6: 120,
        7: 180,
        8: 160,
        9: 110,
        10: 65,
        11: 35,
        12: 25
    }

    base_rainfall = rainfall_pattern[month_in_year]

    # Small random variation
    rainfall = np.random.normal(
        base_rainfall,
        max(base_rainfall * 0.15, 5)
    )

    return max(0, round(rainfall, 2))


# -----------------------------
# Generate repair event
# -----------------------------

def generate_repair(month, last_repair_month):
    """
    Occasionally generates a road repair.
    """

    months_since_repair = month - last_repair_month

    # Repairs become more likely after several months
    if months_since_repair < 8:
        return False

    repair_probability = min(
        0.02 + (months_since_repair - 8) * 0.005,
        0.08
    )

    return np.random.random() < repair_probability


# -----------------------------
# Generate complete dataset
# -----------------------------

def generate_dataset():

    sections = create_road_sections()

    records = []

    for section in sections:

        condition = section["initial_condition"]

        last_repair_month = 0
        repair_count = 0

        for month in range(1, NUM_MONTHS + 1):

            rainfall = generate_rainfall(month)

            repair_event = generate_repair(
                month,
                last_repair_month
            )

            repair_quality = 0.0

            # -----------------------------
            # Apply repair
            # -----------------------------

            if repair_event:

                repair_count += 1
                last_repair_month = month

                # Repair quality between 0.5 and 0.9
                repair_quality = np.random.uniform(0.5, 0.9)

                # Repair improves condition
                improvement = 15 * repair_quality

                condition += improvement

                # Prevent condition from exceeding 100
                condition = min(condition, 100)

            # -----------------------------
            # Damage level
            # -----------------------------

            damage_level = max(
                0,
                (100 - condition) / 100
            )

            # -----------------------------
            # Store record
            # -----------------------------

            records.append({
                "section_id": section["section_id"],
                "road_type": section["road_type"],
                "month": month,
                "road_age": section["road_age"],
                "traffic": section["traffic"],
                "rainfall": rainfall,
                "road_condition": round(condition, 2),
                "damage_level": round(damage_level, 4),
                "repair_event": int(repair_event),
                "repair_quality": round(repair_quality, 3),
                "repair_count": repair_count,
                "months_since_repair": month - last_repair_month
            })

    return pd.DataFrame(records)


# -----------------------------
# Save dataset
# -----------------------------

def main():

    print("Generating simulated road data...")

    df = generate_dataset()

    os.makedirs("data", exist_ok=True)

    output_path = "data/road_history.csv"

    df.to_csv(output_path, index=False)

    print(f"\nDataset created: {output_path}")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nRoad sections:")
    print(df["section_id"].nunique())

    print("\nMonths:")
    print(df["month"].nunique())


if __name__ == "__main__":
    main()