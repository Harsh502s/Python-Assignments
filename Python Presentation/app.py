# Making Ad prediction Web App using Streamlit

# Importing Libraries

import streamlit as st
import pickle

# Importing the pickle file
with open(
    r"C:\Users\harsh\College\Python-Assignments\Python Presentation\gnbmodel.pkl",
    "rb",
) as f:
    model = pickle.load(f)
    pass

# Title of the Web App

st.title("Ad Click Prediction Web App")

# Taking Input fron the user

daily_time_spent_on_site = st.number_input(
    "Daily Time Spent on Site(in min)"
)  # Daily Time Spent on Site in minutes

age = st.slider("Age", 6, 90)  # Age of the user

area_income = st.number_input("Area Income")  # Area Income in USD

daily_internet_usage = st.number_input(
    "Daily Internet Usage(in min)"
)  # Daily Internet Usage in minutes

Gender = st.selectbox("Gender", ["Male", "Female"])

sex = None
if Gender == "Male":
    sex = 1
else:
    sex = 0
    pass

if st.button("Predict"):
    ypred = model.Predict(
        [[daily_time_spent_on_site, age, area_income, daily_internet_usage, sex]]
    )
    if ypred == 0:
        st.write("The user will not click on the ad")
    else:
        st.write("The user will click on the ad")
