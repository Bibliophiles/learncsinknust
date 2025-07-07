import streamlit as st
import pandas as pd

def render():
    st.title("First Year - Second Semester 2/8")
    st.write("Welcome to your second semester of first year!")
    # Add your custom logic here

    course_summary = pd.DataFrame({
        "Course Code": ["CSM 152", "MATH 162", "CSM 158", "ECON 152", "MATH 166", "ENGL 158", "CSM 166"],
        "Course Name": ["INFORMATION TECHNOLOGY II", "INTRODUCTORY PURE MATHEMATICS II",
                        "PROGRAMMING WITH C++", "ELEMENTS OF ECONOMICS II",
                        "INTRODUCTION TO PROBABILITY AND STATISTICS", "COMMUNICATION SKILLS II",
                        "DISCRETE MATHEMATICS FOR COMPUTER SCIENCE II"],
        "Credits": ["3", "3", "3", "3", "3", "2", "3"]
    })

    st.table(course_summary)