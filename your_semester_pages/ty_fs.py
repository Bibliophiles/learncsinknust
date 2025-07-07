import streamlit as st
import pandas as pd 

def render():
    st.title("Third Year - First Semester 5/8")
    st.write("Welcome to your first semester of third year!")
    # Add your custom logic here

    course_summary = pd.DataFrame({
        "Course Code": ["ACF 255", "CSM 353", "CSM 357", "CSM 393", "CSM 387", "CSM 395", "CSM 399"],
        "Course Name": ["FINANCIAL ACCOUNTING I",
                        "SURVEY OF PROGRAMMING LANGUAGES",
                        "HUMAN COMPUTER INTERACTION",
                        "OPERATIONS RESEARCH I",
                        "DATA STRUCTURES I",
                        "INTRODUCTION TO ARTIFICIAL INTELLIGENCE",
                        "WEB-BASED CONCEPTS AND DEVELOPMENT"],
        "Credits": ["2", "3", "2", "2", "3", "2", "2"]
    })

    st.table(course_summary)