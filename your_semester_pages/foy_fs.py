import streamlit as st
import pandas as pd 

def render():
    st.title("Fourth Year - First Semester 7/8")
    st.write("Welcome to your first semester of fourth year!")

    course_summary = pd.DataFrame({
        "Course Code": ["CSM 477", "CSM 481", "CSM 483", "CSM 491", "CSM 495", "CSM 497", "MAS 261"],
        "Course Name": ["DATA COMMUNICATIONS",
                        "INFORMATION SYSTEMS I",
                        "OPERATING SYSTEMS ",
                        "GRAPH THEORY AND ITS APPLICATIONS ",
                        "INTRODUCTION TO SOFTWARE ENGINEERING",
                        "EXPERT SYSTEMS",
                        "PRINCIPLES OF MANAGEMENT"],
        "Credits": ["3", "3", "3", "2", "2", "2", "3"]
    })

    st.table(course_summary)
