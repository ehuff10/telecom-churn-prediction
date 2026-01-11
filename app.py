import streamlit as st
import pandas as pd
import joblib

# Load model artifacts
MODEL_PATH = "models/final_churn_model.joblib"
THRESHOLD_PATH = "models/final_threshold.joblib"

model = joblib.load(MODEL_PATH)
threshold = joblib.load(THRESHOLD_PATH)

st.title("Telecom Churn Risk Predictor")

st.write(
    "Enter customer information below. This tool prioritizes identifying "
    "customers at high risk of churn so retention teams can intervene."
)

# -------------------------
# Input form
# -------------------------
with st.form("customer_form"):
    tenure = st.number_input("Tenure (months)", min_value=0, 
max_value=100, value=12)
    monthly_charges = st.number_input("Monthly Charges ($)", 
min_value=0.0, value=70.0)
    total_charges = st.number_input("Total Charges ($)", min_value=0.0, 
value=800.0)

    international_plan = st.selectbox("International Plan", ["No", "Yes"])
    voice_mail_plan = st.selectbox("Voice Mail Plan", ["No", "Yes"])

    customer_service_calls = st.number_input(
        "Customer Service Calls", min_value=0, max_value=20, value=1
    )

    total_usage_minutes = st.number_input(
        "Total Usage Minutes", min_value=0.0, value=600.0
    )

    total_usage_calls = st.number_input(
        "Total Usage Calls", min_value=0, value=300
    )

    submit = st.form_submit_button("Predict Churn Risk")

# -------------------------
# Prediction
# -------------------------
if submit:
    input_data = pd.DataFrame(
        [{
            "tenure": tenure,
            "monthly_charges": monthly_charges,
            "total_charges": total_charges,
            "international_plan": international_plan,
            "voice_mail_plan": voice_mail_plan,
            "customer_service_calls": customer_service_calls,
            "total_usage_minutes": total_usage_minutes,
            "total_usage_calls": total_usage_calls
        }]
    )

    churn_prob = model.predict_proba(input_data)[0, 1]
    churn_flag = churn_prob >= threshold

    st.subheader("Prediction Result")

    st.write(f"Churn Probability: **{churn_prob:.2%}**")

    if churn_flag:
        st.error("⚠️ High Risk of Churn — Retention Action Recommended")
    else:
        st.success("✅ Low Risk of Churn")


