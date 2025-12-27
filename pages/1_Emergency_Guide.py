import streamlit as st
from backend.rag_engine import RAGEngine
from backend.db import init_db, log_event
from backend.voice_input import capture_voice_input

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

# ---------------- INITIALIZATION ----------------
init_db()
rag = RAGEngine()

st.set_page_config(page_title="Emergency First Aid Guide")
st.title("🩺 Emergency First Aid Guide")

st.warning(
    "⚠ This system is for educational assistance only. "
    "Always call emergency services in real emergencies."
)

# ---------------- SESSION STATE ----------------
st.session_state.setdefault("query", "")
st.session_state.setdefault("response", None)
st.session_state.setdefault("meta", None)

# ---------------- VOICE INPUT ----------------
if st.button("🎙️ Speak Emergency"):
    with st.spinner("Listening..."):
        spoken_text = capture_voice_input()

    if spoken_text:
        st.session_state.query = spoken_text
        st.success(f"You said: {spoken_text}")
    else:
        st.error("Could not recognize speech.")

# ---------------- TEXT INPUT ----------------
st.session_state.query = st.text_area(
    "Describe the emergency:",
    value=st.session_state.query,
    height=150,
    placeholder="Example: My friend was bitten by a snake"
)

# ---------------- PROCESS ----------------
if st.button("Get First Aid Help"):
    if st.session_state.query.strip() == "":
        st.error("Please describe the emergency.")
    else:
        with st.spinner("Analyzing emergency and retrieving first aid steps..."):
            response, meta = rag.get_response_with_meta(st.session_state.query)

        st.session_state.response = response
        st.session_state.meta = meta

        log_event(
            query=st.session_state.query,
            category=meta["category"],
            method=meta["method"]
        )

# ---------------- DISPLAY ----------------
if st.session_state.response:
    st.subheader("✅ First Aid Instructions")
    st.success(st.session_state.response)

    category = get_emergency_category(st.session_state.query)
    severity = get_emergency_severity(
        st.session_state.query,
        st.session_state.meta["similarity_distance"]
    )

    col1, col2 = st.columns(2)
    with col1:
        st.info(f"🏷 **Category:** {category}")
    with col2:
        st.warning(f"🚦 **Severity:** {severity}")

    # ❌ WHAT NOT TO DO
    st.subheader("⛔ What NOT to Do")
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
