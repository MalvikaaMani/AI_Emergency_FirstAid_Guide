import streamlit as st
from PIL import Image

from backend.rag_engine import RAGEngine
from backend.medical_image_classifier import classify_medical_image
from backend.image_emergency_mapper import map_medical_label_to_query
from backend.db import log_event

# METADATA
from backend.emergency_metadata import (
    get_emergency_category,
    get_emergency_severity,
    get_donts
)

# READINESS & TIMELINE
from backend.emergency_readiness import (
    get_readiness_checklist,
    get_timeline_tip
)

# ---------------- INITIALIZE ----------------
rag = RAGEngine()

st.set_page_config(page_title="Image-Based Emergency Detection")
st.title("🖼️ Medical Image-Based Emergency Detection")

st.warning(
    "⚠ This system is for educational assistance only. "
    "Always call emergency services in real emergencies."
)

uploaded_file = st.file_uploader(
    "Upload an image showing the injury",
    type=["jpg", "jpeg", "png"]
)

# ---------------- IMAGE PROCESSING ----------------
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Injury Image", width=300)

    with st.spinner("Analyzing image using medical vision model..."):
        label, confidence = classify_medical_image(image)

    st.subheader("🧠 Image Analysis Result")
    st.write(f"Detected Condition: **{label}**")
    st.write(f"Confidence Score: **{round(confidence, 3)}**")

    emergency_query = map_medical_label_to_query(label)

    if emergency_query and confidence > 0.40:
        st.success(f"Identified Emergency: **{emergency_query}**")

        response, meta = rag.get_response_with_meta(emergency_query)

        category = get_emergency_category(emergency_query)
        severity = get_emergency_severity(
            emergency_query,
            meta.get("similarity_distance", 1.5)
        )

        log_event(
            query="Image Upload",
            category=category,
            method=meta["method"]
        )

        st.subheader("🚑 First Aid Instructions")
        st.success(response)

        st.info(
            f"🏷 **Category:** {category}  \n"
            f"🚦 **Severity:** {severity}"
        )

        # ❌ WHAT NOT TO DO
        st.subheader("❌ What NOT to Do")
        for item in get_donts(category):
            st.error(item)

        # 🧰 READINESS CHECKLIST
        st.subheader("🧰 Emergency Readiness Checklist")
        for item in get_readiness_checklist(category):
            st.checkbox(item, value=True, disabled=True)

        # ⏱ TIMELINE TIP
        st.subheader("⏱ Emergency Timeline Tip")
        st.info(get_timeline_tip(category))

        # 📞 QUICK CALL
        st.subheader("📞 Emergency Quick Call")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                """
                **🇮🇳 India**
                - Emergency: **112**
                - Ambulance: **108**
                """
            )
        with col2:
            st.markdown(
                """
                **🌍 International**
                - USA / Canada: **911**
                - UK / Ireland: **999**
                - EU: **112**
                """
            )

        st.error("🚨 Call emergency services immediately if the condition worsens.")

    else:
        st.error(
            "❌ Unable to confidently determine the emergency from the image. "
            "Please seek immediate professional medical help."
        )
