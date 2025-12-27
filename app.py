import streamlit as st

st.set_page_config(
    page_title="AI Emergency First Aid Guide",
    page_icon="🚑",
    layout="centered"
)

# ------------------ HOME PAGE ------------------

st.markdown(
    """
    <h1 style='text-align: center;'>🚑 AI Emergency First Aid Guide</h1>
    <h4 style='text-align: center; color: grey;'>
    Quick guidance until professional help arrives
    </h4>
    """,
    unsafe_allow_html=True
)

st.write("")
st.warning(
    "⚠️ This application provides educational first-aid guidance only. "
    "In real emergencies, always contact local emergency services immediately."
)

st.write("")
st.write("### How can we help you right now?")

col1, col2 = st.columns(2)

with col1:
    st.page_link(
        "pages/1_Emergency_Guide.py",
        label="🚑 Describe an Emergency",
        help="Get step-by-step first aid instructions"
    )

with col2:
    st.page_link(
        "pages/3_Image_Emergency.py",
        label="🖼️ Upload an Injury Image",
        help="Identify injury from an image"
    )

st.write("")

st.page_link(
    "pages/2_Emergency_History.py",
    label="📜 View Emergency History",
    help="See past emergencies and responses"
)

st.write("")
st.markdown(
    "<p style='text-align: center; color: grey;'>"
    "Stay calm. Help is on the way."
    "</p>",
    unsafe_allow_html=True
)
