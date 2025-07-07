import streamlit as st
from navigation_routes import academic_map, extracurricular_map, daily_practice_map, life_hacks_map

st.set_page_config(
    page_title="Learn CS in KNUST",
    page_icon="👨‍💻",
)

# ───────────────────────────────────────
# Navigation Mode
st.sidebar.title("🔍 Navigation Mode")
mode = st.sidebar.radio("What would you like to explore?", ["Academic", "Extracurricular", "Daily Practice", "Life Hacks"])

# ───────────────────────────────────────
# Academic
if mode == "Academic":
    st.sidebar.title("📚 Academic Navigation")
    year = st.sidebar.selectbox("Select Academic Year", list({k[0] for k in academic_map.keys()}))
    semester = st.sidebar.radio("Select Semester", ["First Semester", "Second Semester"])
    page = academic_map.get((year, semester))
    if page:
        page.render()

# ───────────────────────────────────────
# Extracurricular
elif mode == "Extracurricular":
    st.sidebar.title("🚀 Extracurriculars")
    activity = st.sidebar.radio("Choose an Activity", list(extracurricular_map.keys()))
    page = extracurricular_map.get(activity)
    if page:
        page.render()

# ───────────────────────────────────────
# Daily Practice
elif mode == "Daily Practice":
    st.sidebar.title("🧠 Daily Practice")
    practice = st.sidebar.radio("Choose a Daily Practice", list(daily_practice_map.keys()))
    page = daily_practice_map.get(practice)
    if page:
        page.render()

# ───────────────────────────────────────
# Life Hacks
elif mode == "Life Hacks":
    st.sidebar.title("😓 CS is HARD")
    hacks = st.sidebar.radio("Choose a Life Hack", list(life_hacks_map.keys()))
    page = life_hacks_map.get(hacks)
    if page:
        page.render()
