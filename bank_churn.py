import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

st.title("🏦 Bank Churn Prediction")

# Inputs
credit = st.number_input("Credit Score")
age = st.number_input("Age")
tenure = st.number_input("Tenure")
balance = st.number_input("Balance")
products = st.number_input("Num Of Products")
card = st.selectbox("Has Credit Card", [0,1])
active = st.selectbox("Is Active Member", [0,1])
salary = st.number_input("Estimated Salary")
geo = st.selectbox("Geography", ["France", "Spain", "Germany"])
gender = st.selectbox("Gender", ["Male", "Female"])

# Encoding manually
geo_germany = 1 if geo == "Germany" else 0
geo_spain = 1 if geo == "Spain" else 0
gender_male = 1 if gender == "Male" else 0

# Final input (MATCH TRAINING ORDER)
input_data = np.array([[credit, age, tenure, balance, products,
                        card, active, salary,
                        geo_germany, geo_spain,
                        gender_male]])

# Prediction
if st.button("Predict"):
    result = model.predict(input_data)

    if result[0] == 1:
        st.error("⚠️ Customer will Churn")
    else:
        st.success("✅ Customer will Stay")