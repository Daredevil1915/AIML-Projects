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

total_bedrooms=st.number_input("Total Bedrooms in that area",min_value=0,value=0,step=1)
households=st.number_input("Total Households",min_value=1,value=1,step=1)
median_income=st.number_input("Median Income of that area", min_value=0.0,format="%.4f",value=35000.0,step=1000.0)
housing_median_age=st.number_input("Housing Median Age", min_value=0,value=25,step=1)
rooms_per_house=st.number_input("Rooms per House", min_value=0.0,value=5.0,format="%.2f",step=0.5)
population_per_household=st.number_input("Population per Household", min_value=0.0,value=3.0,format="%.2f",step=0.1)
ocean_proximity=st.selectbox("Ocean Proximity", ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"])



if(households>0):
    bedrooms_per_house=total_bedrooms/households
else:
    bedrooms_per_house=0


if st.button("Predict Price"):
    if total_bedrooms==0 and median_income==0 and housing_median_age==0:
        st.success("🏡Estimated House Price: $0.00")
    else:
        median_income=median_income/10000
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
