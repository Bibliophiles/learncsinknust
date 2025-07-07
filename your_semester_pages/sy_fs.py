import streamlit as st
import pandas as pd 

def render():
    st.title("Second Year - First Semester 3/8")
    st.write("Welcome to your first semester of second year!")
    # Add your custom logic here

    course_summary = pd.DataFrame({
        "Course Code": ["CSM 265", "CSM 281", "CSM 297", "ENGL 263", "CSM 291", "CSM 273", "CSM 251", "CSM 255"],
        "Course Name": ["ETHICAL AND LEGAL IMPLICATION OF COMPUTING",
                        "OBJECT ORIENTED PROGRAMMING WITH JAVA",
                        "DATABASE CONCEPTS AND TECHNOLOGIES I",
                        "LITERATURE IN ENGLISH I",
                        "SYSTEM ANALYSIS AND DESIGN I",
                        "LINEAR AND NUMERICAL ALGEBRA",
                        "INTRODUCTORY ELECTRONICS I", "OPEN SOURCE OPERATING SYSTEMS"],
        "Credits": ["2", "3", "2", "1", "2", "3", "2", "2"]
    })

    st.table(course_summary)