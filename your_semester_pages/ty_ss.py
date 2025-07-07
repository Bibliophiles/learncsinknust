import streamlit as st
import pandas as pd 

def render():
    st.title("Third Year - Second Semester 6/8")
    st.write("Welcome to your second semester of third year!")
    # Add your custom logic here

    course_summary = pd.DataFrame({
        "Course Code": ["ACF 256", "CSM 352", "CSM 354", "CSM 358", "CSM 366", "CSM 374", "CSM 376", "CSM 388", "CSM 394"],
        "Course Name": ["FINANCIAL ACCOUNTING II",
                        "COMPUTER ARCHITECTURE",
                        "COMPUTER GRAPHICS",
                        "E-COMMERCE",
                        "MINI PROJECT",
                        "REAL-TIME AND EMBEDDED SYSTEMS",
                        "RESEARCH METHOD AND IT PROJECT",
                        "DATA STRUCTURES II", 
                        "OPERATIONS RESEARCH II"],
        "Credits": ["3", "3", "2", "3", "2", "2", "2", "3", "2"]
    })

    st.table(course_summary)