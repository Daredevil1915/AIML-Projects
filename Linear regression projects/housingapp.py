import joblib
import streamlit as st
import numpy as np
import pandas as pd


preprocessor = joblib.load(r"C:\Users\Siddharth Verma\Documents\COURSE\python\Linear regression projects\preprocessor.joblib")
model = joblib.load(r"C:\Users\Siddharth Verma\Documents\COURSE\python\Linear regression projects\model.joblib")

st.title("🏠 California House Price Prediction")

st.write("""
Enter the housing data below.  
💡 *Median Income* is in **tens of thousands** of dollars.  
Example: `8.3252` means $83,252.
""")

median_income = st.number_input("Median Income (×10,000)", min_value=0.0, format="%.4f")
housing_median_age = st.number_input("Housing Median Age", min_value=0.0, format="%.0f")
rooms_per_house = st.number_input("Rooms per House", min_value=0.0, format="%.2f")
population_per_household = st.number_input("Population per Household", min_value=0.0, format="%.2f")

ocean_proximity = st.selectbox("Ocean Proximity", ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"])

if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        "median_income": median_income,
        "housing_median_age": housing_median_age,
      "rooms_per_house": rooms_per_house,
        "population_per_household": population_per_household,
        "ocean_proximity": ocean_proximity
    }])

    prediction = model.predict(input_df)

    st.success(f"🏡 Estimated House Price: ${prediction[0]:,.2f}")
