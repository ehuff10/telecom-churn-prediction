import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and threshold
MODEL_PATH = "models/final_churn_model.joblib"
THRESHOLD_PATH = "models/final_threshold.joblib"

model = joblib.load(MODEL_PATH)
threshold = joblib.load(THRESHOLD_PATH)

# Risk tier function
def assign_risk_tier(prob):
    if prob >= 0.75:
        return "Very High Risk"
    elif prob >= 0.50:
        return "High Risk"
    elif prob >= 0.30:
        return "Medium Risk"
    else:
        return "Low Risk"

# App title
st.title("Telecom Churn Risk Assessment Tool")

# User inputs
tenure = st.number_input("Tenure (months)", min_value=0, value=12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=1000.0)
customer_service_calls = st.number_input("Customer Service Calls", min_value=0, value=1)

international_plan = st.selectbox(
    "International Plan",
    ["Yes", "No"]
)

voice_mail_plan = st.selectbox(
    "Voice Mail Plan",
    ["Yes", "No"]
)

# Prediction button
if st.button("Assess Churn Risk"):

    # Raw input
    raw_input = {
        "tenure": tenure,
        "monthly_charges": monthly_charges,
        "total_charges": total_charges,
        "customer_service_calls": customer_service_calls,
        "international_plan": international_plan,
        "voice_mail_plan": voice_mail_plan
    }

    input_data = pd.DataFrame([raw_input])

    # Align with training schema
    expected_features = model.named_steps["preprocessor"].feature_names_in_

    for col in expected_features:
        if col not in input_data.columns:
            input_data[col] = 0

    input_data = input_data[expected_features]

    # Predict
    churn_prob = model.predict_proba(input_data)[0, 1]
    churn_flag = int(churn_prob >= threshold)
    risk_tier = assign_risk_tier(churn_prob)

    # Output
    st.subheader("Prediction Results")
    st.write(f"Churn Probability: {churn_prob:.2%}")
    st.write(f"Predicted Churn: {'Yes' if churn_flag == 1 else 'No'}")
    st.write(f"Risk Tier: {risk_tier}")
