# navigation_routes.py

from your_semester_pages import fy_fs, fy_ss, sy_fs, sy_ss, ty_fs, ty_ss, foy_fs, foy_ss
from extracurricular_pages import cybersecurity, database, datascience, mobile_dev, web_dev
from daily_practice_pages import typing, leetcode
from life_hacks_pages import distractions, personal_time_table, punctuality

# Academic map
academic_map = {
    ("First Year", "First Semester"): fy_fs,
    ("First Year", "Second Semester"): fy_ss,
    ("Second Year", "First Semester"): sy_fs,
    ("Second Year", "Second Semester"): sy_ss,
    ("Third Year", "First Semester"): ty_fs,
    ("Third Year", "Second Semester"): ty_ss,
    ("Fourth Year", "First Semester"): foy_fs,
    ("Fourth Year", "Second Semester"): foy_ss,
}

# Extracurricular map
extracurricular_map = {
    "Web Development": web_dev,
    "Mobile App Development": mobile_dev,
    "CyberSecurity": cybersecurity,
    "Database Management": database,
    "Data Science": datascience
}

# Daily practice map
daily_practice_map = {
    "Typing": typing,
    "LeetCode": leetcode
}

# Life hacks
life_hacks_map = {
    "Distractions": distractions,
    "Personal TimeTable": personal_time_table,
    "Punctuality": punctuality
}
