from pathlib import Path

import pandas as pd
import streamlit as st


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "hillstrom.csv"

st.set_page_config(page_title="Email Experiment", layout="wide")
st.title("Email Marketing Experiment")
st.caption("Hillstrom / MineThatData randomised email campaign")

if not DATA_FILE.exists():
    st.error("Run `python download_data.py` first.")
    st.stop()

df = pd.read_csv(DATA_FILE)

summary = (
    df.groupby("segment")
    .agg(
        customers=("segment", "size"),
        visit_rate=("visit", "mean"),
        conversion_rate=("conversion", "mean"),
        revenue_per_customer=("spend", "mean"),
    )
)

st.subheader("Campaign performance")

display = summary.copy()
display["visit_rate"] = display["visit_rate"] * 100
display["conversion_rate"] = display["conversion_rate"] * 100

st.dataframe(
    display.style.format(
        {
            "visit_rate": "{:.2f}%",
            "conversion_rate": "{:.2f}%",
            "revenue_per_customer": "${:.2f}",
        }
    ),
    use_container_width=True,
)

c1, c2 = st.columns(2)

with c1:
    st.markdown("**Conversion rate**")
    st.bar_chart(summary["conversion_rate"])

with c2:
    st.markdown("**Revenue per customer**")
    st.bar_chart(summary["revenue_per_customer"])

st.subheader("Breakdown by previous purchase channel")

channel = (
    df.groupby(["channel", "segment"])["conversion"]
    .mean()
    .unstack()
)

st.dataframe(
    channel.style.format("{:.2%}"),
    use_container_width=True,
)
