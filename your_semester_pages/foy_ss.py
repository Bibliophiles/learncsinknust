import streamlit as st
import pandas as pd 

def render():
    st.title("Fourth Year - Second Semester 8/8")
    st.write("Welcome to your last semester as a KNUST Computer Science Student 🔥!")

    course_summary = pd.DataFrame({
        "Course Code": ["CSM 478", "CSM 482", "CSM 494", "MGT 472", "CSM 490", "CSM 484"],
        "Course Name": ["COMPUTER NETWORKS",
                        "INFORMATION SYSTEMS II",
                        "COMPUTER SECURITY",
                        "PRINCIPLES OF MANAGEMENT II",
                        "PROJECT II",
                        "INTRODUCTION TO COMPILERS"],
        "Credits": ["3", "3", "3", "3", "6", "3"]
    })

    st.table(course_summary)