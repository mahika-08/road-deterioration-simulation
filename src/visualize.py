import os
import pandas as pd
import matplotlib.pyplot as plt


DATA_FILE = "data/road_history.csv"
PREDICTION_FILE = "results/predictions.csv"

os.makedirs("results", exist_ok=True)


# ============================================================
# 1. Road condition over time
# ============================================================

df = pd.read_csv(DATA_FILE)

plt.figure(figsize=(11, 6))

# Show 8 example roads
sections = df["section_id"].unique()[:8]

for section in sections:

    road = df[df["section_id"] == section]

    plt.plot(
        road["month"],
        road["road_condition"],
        linewidth=2,
        label=section
    )


plt.axvline(
    24,
    linestyle="--",
    linewidth=2,
    label="Prediction Point"
)

plt.title(
    "Road Condition Over Time",
    fontsize=16
)

plt.xlabel("Month")
plt.ylabel("Road Condition (0 = Poor, 100 = Good)")

plt.ylim(0, 105)

plt.grid(
    alpha=0.2
)

plt.legend(
    ncol=2
)

plt.tight_layout()

plt.savefig(
    "results/deterioration_over_time.png",
    dpi=150
)

plt.close()


# ============================================================
# 2. Actual vs predicted deterioration
# ============================================================

df = pd.read_csv(PREDICTION_FILE)

plt.figure(figsize=(8, 6))

plt.scatter(
    df["future_deterioration"],
    df["predicted_deterioration"],
    alpha=0.7
)

minimum = min(
    df["future_deterioration"].min(),
    df["predicted_deterioration"].min()
)

maximum = max(
    df["future_deterioration"].max(),
    df["predicted_deterioration"].max()
)

plt.plot(
    [minimum, maximum],
    [minimum, maximum],
    linestyle="--",
    linewidth=2,
    label="Perfect Prediction"
)

plt.title(
    "Actual vs Predicted Deterioration",
    fontsize=16
)

plt.xlabel("Actual Deterioration")
plt.ylabel("Predicted Deterioration")

plt.grid(alpha=0.2)

plt.legend()

plt.tight_layout()

plt.savefig(
    "results/actual_vs_predicted.png",
    dpi=150
)

plt.close()


# ============================================================
# 3. Risk map
# ============================================================

risk_order = {
    "LOW": 0,
    "MEDIUM": 1,
    "HIGH": 2
}

df["risk_value"] = df["risk"].map(risk_order)

df = df.sort_values("section_id")

plt.figure(figsize=(14, 3))

plt.scatter(
    range(len(df)),
    [1] * len(df),
    c=df["risk_value"],
    cmap="RdYlGn_r",
    s=180,
    vmin=0,
    vmax=2
)

plt.yticks([])

plt.xticks(
    range(0, len(df), 10),
    df["section_id"].iloc[::10]
)

plt.title(
    "Predicted Road Deterioration Risk",
    fontsize=16
)

plt.xlabel("Road Section")

plt.grid(
    axis="x",
    alpha=0.2
)

plt.tight_layout()

plt.savefig(
    "results/risk_map.png",
    dpi=150
)

plt.close()


print("Visualizations generated.")

print("\nFiles created:")

print("results/deterioration_over_time.png")
print("results/actual_vs_predicted.png")
print("results/risk_map.png")