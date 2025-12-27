import streamlit as st
import pandas as pd
from backend.db import fetch_logs

st.title("📜 Emergency History & Logs")
st.caption("Past emergency requests and system responses")

logs = fetch_logs()

if logs:
    df = pd.DataFrame(
        logs,
        columns=["ID", "Timestamp", "Input Source", "Emergency Type", "Method"]
    )

    df["Input Source"] = df["Input Source"].apply(
        lambda x: "🖼️ Image" if x == "Image Upload" else "⌨️ Text"
    )

    st.dataframe(df, use_container_width=True)
else:
    st.info("No emergency records found yet.")
