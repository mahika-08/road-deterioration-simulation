import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# Page configuration
# ============================================================


st.set_page_config(
    page_title="Road Deterioration Simulation",
    page_icon="🛣️",
    layout="wide"
)


# ============================================================
# Light theme
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #f7f9fc;
        color: #1f2937;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3 {
        color: #111827;
    }

    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        text-align: center;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# Load data
# ============================================================

history = pd.read_csv("data/road_history.csv")
predictions = pd.read_csv("results/predictions.csv")


# ============================================================
# Header
# ============================================================

st.title("🛣️ Road Deterioration Prediction")

st.markdown(
    """
    ### Predicting road deterioration before it becomes severe

    This simulation studies whether historical road condition,
    traffic, rainfall, road age, damage and repair history can
    help identify road sections that are likely to deteriorate
    in the near future.
    """
)


# ============================================================
# Summary metrics
# ============================================================

total_sections = len(predictions)

high_risk = len(
    predictions[predictions["risk"] == "HIGH"]
)

medium_risk = len(
    predictions[predictions["risk"] == "MEDIUM"]
)

low_risk = len(
    predictions[predictions["risk"] == "LOW"]
)


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Road Sections",
        total_sections
    )

with col2:
    st.metric(
        "High Risk",
        high_risk
    )

with col3:
    st.metric(
        "Medium Risk",
        medium_risk
    )

with col4:
    st.metric(
        "Low Risk",
        low_risk
    )


st.divider()


# ============================================================
# Risk overview
# ============================================================

st.header("Predicted Inspection Risk")

st.markdown(
    "The system predicts deterioration over the next 6 months "
    "using information available at Month 24."
)


# Sort highest risk first
risk_table = predictions.sort_values(
    "predicted_deterioration",
    ascending=False
).copy()


def highlight_risk(value):

    if value == "HIGH":
        return "background-color: #fee2e2; color: #991b1b"

    if value == "MEDIUM":
        return "background-color: #fef3c7; color: #92400e"

    return "background-color: #dcfce7; color: #166534"


display_columns = [
    "section_id",
    "road_condition",
    "predicted_deterioration",
    "predicted_condition",
    "risk"
]


st.dataframe(
    risk_table[display_columns]
    .style
    .map(highlight_risk, subset=["risk"])
    .format({
        "road_condition": "{:.1f}",
        "predicted_deterioration": "{:.1f}",
        "predicted_condition": "{:.1f}"
    }),
    use_container_width=True,
    hide_index=True
)


# ============================================================
# Road condition history
# ============================================================

st.header("Road Condition Over Time")

selected_section = st.selectbox(
    "Select a road section",
    sorted(history["section_id"].unique())
)


section_data = history[
    history["section_id"] == selected_section
]


fig, ax = plt.subplots(
    figsize=(10, 4)
)

ax.plot(
    section_data["month"],
    section_data["road_condition"],
    linewidth=2
)

ax.axvline(
    24,
    linestyle="--",
    linewidth=2,
    label="Prediction point"
)

ax.set_title(
    f"Road Condition — {selected_section}"
)

ax.set_xlabel("Month")

ax.set_ylabel(
    "Condition (0 = poor, 100 = good)"
)

ax.set_ylim(0, 105)

ax.grid(
    alpha=0.2
)

ax.legend()

fig.tight_layout()

st.pyplot(fig)


# ============================================================
# Actual vs predicted
# ============================================================

st.header("Prediction vs Actual Result")

fig, ax = plt.subplots(
    figsize=(8, 6)
)

ax.scatter(
    predictions["future_deterioration"],
    predictions["predicted_deterioration"],
    alpha=0.7
)

minimum = min(
    predictions["future_deterioration"].min(),
    predictions["predicted_deterioration"].min()
)

maximum = max(
    predictions["future_deterioration"].max(),
    predictions["predicted_deterioration"].max()
)

ax.plot(
    [minimum, maximum],
    [minimum, maximum],
    linestyle="--",
    linewidth=2
)

ax.set_xlabel(
    "Actual deterioration"
)

ax.set_ylabel(
    "Predicted deterioration"
)

ax.set_title(
    "Actual vs Predicted Deterioration"
)

ax.grid(alpha=0.2)

fig.tight_layout()

st.pyplot(fig)


# ============================================================
# Road risk visualization
# ============================================================

st.header("Road Risk Map")

st.markdown(
    "Each block represents a simulated road section. "
    "The color represents predicted deterioration risk."
)


risk_colors = {
    "LOW": "#22c55e",
    "MEDIUM": "#f59e0b",
    "HIGH": "#ef4444"
}


fig, ax = plt.subplots(
    figsize=(14, 2.5)
)

for i, row in predictions.sort_values("section_id").reset_index().iterrows():

    ax.scatter(
        i,
        0,
        s=180,
        color=risk_colors[row["risk"]]
    )

ax.set_xlim(-1, len(predictions))

ax.set_ylim(-1, 1)

ax.set_yticks([])

ax.set_xlabel("Road sections")

ax.set_title(
    "Predicted Deterioration Risk"
)

ax.grid(
    axis="x",
    alpha=0.2
)

fig.tight_layout()

st.pyplot(fig)


# ============================================================
# Explanation
# ============================================================

st.divider()

st.header("What this simulation demonstrates")

st.markdown(
    """
    **Traditional approach**

    Detect damage after it becomes visible.

    **This simulation**

    Uses road history and surrounding factors to estimate
    which sections may deteriorate in the future.

    The result is an **inspection priority**, not an automatic
    repair decision.

    **Important:** All data in this project is simulated.
    It is intended to demonstrate the problem and prediction
    approach, not to represent real road conditions.
    """
)