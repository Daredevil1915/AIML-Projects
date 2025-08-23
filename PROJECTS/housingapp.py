import joblib
import streamlit as st
import numpy as np
import pandas as pd
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PREPROCESSOR_PATH = SCRIPT_DIR/"preprocessor.joblib"
MODEL_PATH = SCRIPT_DIR/"model.joblib"


preprocessor = joblib.load(PREPROCESSOR_PATH)
model = joblib.load(MODEL_PATH)

st.title("🏠 California House Price Prediction")

total_bedrooms=st.number_input("Total Bedrooms in that area",min_value=0.0,format="%.0f")
households=st.number_input("Total Households",min_value=1.0,format="%.0f")
median_income=st.number_input("Median Income of that area", min_value=0.0, format="%.4f")
housing_median_age=st.number_input("Housing Median Age", min_value=0.0, format="%.0f")
rooms_per_house=st.number_input("Rooms per House", min_value=0.0, format="%.2f")
population_per_household=st.number_input("Population per Household", min_value=0.0, format="%.2f")
ocean_proximity=st.selectbox("Ocean Proximity", ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"])

median_income=median_income/10000

if(households>0):
    bedrooms_per_house=total_bedrooms/households
else:
    bedrooms_per_house=0


if st.button("Predict Price"):
    if total_bedrooms==0 and median_income==0 and housing_median_age==0:
        st.success("🏡Estimated House Price: $0.00")
    else:    
        input_df = pd.DataFrame([{
    "housing_median_age": housing_median_age,
    "median_income": median_income,
    "rooms_per_house": rooms_per_house,
    "bedrooms_per_house": bedrooms_per_house,
    "population_per_household": population_per_household,
    "ocean_proximity": ocean_proximity
    }])

        prediction=model.predict(input_df)
        prediction=np.expm1(prediction) 

        st.success(f"🏡Estimated House Price: ${prediction[0]:,.2f}")
