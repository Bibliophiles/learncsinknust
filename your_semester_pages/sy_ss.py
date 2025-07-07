import streamlit as st
import pandas as pd

def render():
    st.title("Second Year - Second Semester 4/8")
    st.write("Welcome to your second semester of second year!")
    # Add your custom logic here

    course_summary = pd.DataFrame({
        "Course Code": ["CSM 252", "CSM 254", "CSM 258", "CSM 260", "CSM 264", "CSM 292", "ENGL 264", "CSM 266"],
        "Course Name": ["ANALOGUE AND DIGITAL ELECTRONICS",
                        "PROGRAMMING WITH ASSEMBLY LANGUAGE",
                        "NUMERICAL METHODS AND COMPUTATION",
                        "DATABASE CONCEPTS AND TECHNOLOGIES II",
                        "PROGRAMMING WITH VISUAL BASIC",
                        "SYSTEMS ANALYSIS AND DESIGN II",
                        "LITERATURE IN ENGLISH II", "MOBILE APPLICATIONS"],
        "Credits": ["2", "3", "3", "2", "3", "2", "1", "3"]
    })

    st.table(course_summary)