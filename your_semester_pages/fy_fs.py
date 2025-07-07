import streamlit as st
import pandas as pd

def render():
    st.title("First Year - First Semester 1/8")
    st.write("Welcome to your first semester of first year!")
    # Add your custom logic here

    course_summary = pd.DataFrame({
        "Course Code": ["CSM 151", "CSM 157", "CSM 165", "CSM 153", "ECON 151", "ENGL 157", "MATH 161"],
        "Course Name": ["INFORMATION TECHNOLOGY I",
                        "INTRODUCTION TO STRUCTURED PROGRAM DESIGN",
                        "DISCRETE MATHEMATICS FOR COMPUTER SCIENCE I",
                        "CIRCUIT THEORY",
                        "ELEMENTS OF ECONOMICS I",
                        "COMMUNICATION SKILLS I",
                        "INTRODUCTORY PURE MATHEMATICS I"],
        "Credits": ["3", "3", "3", "2", "3", "2", "3"]
    })

    st.table(course_summary)