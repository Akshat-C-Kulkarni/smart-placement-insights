import streamlit as st
import joblib
import numpy as np
import pandas as pd
import warnings

# --------------------------------------------------
# Must be the FIRST Streamlit command
# --------------------------------------------------
st.set_page_config(page_title="Smart Placement Insights", layout="centered")
warnings.filterwarnings("ignore")

# --------------------------------------------------
# Load model and scaler
# --------------------------------------------------
@st.cache_resource
def load_artifacts():
    model = joblib.load("model/placement_model.joblib")
    scaler = joblib.load("model/scaler.joblib")
    return model, scaler

model, scaler = load_artifacts()

# --------------------------------------------------
# App Title and Description
# --------------------------------------------------
st.title("🎓 Smart Placement Insights and Prediction System")
st.markdown("""
Welcome to the **Placement Prediction Dashboard**!  
Enter a student’s details below to predict their **placement likelihood** using the trained ML model.
""")

# --------------------------------------------------
# Input Form
# --------------------------------------------------
with st.form("placement_form"):
    st.subheader("🧾 Enter Student Details")

    IQ = st.number_input("IQ", min_value=0, max_value=200, value=0)
    Prev_Sem_Result = st.number_input("Previous Semester Result (%)", min_value=0, max_value=100, value=0)
    CGPA = st.number_input("CGPA", min_value=0.0, max_value=10.0, value=0.0, format="%.2f")
    Academic_Performance = st.number_input("Academic Performance (%)", min_value=0, max_value=100, value=0)
    Internship_Experience = st.selectbox("Internship Experience", ["Yes", "No"])
    Extra_Curricular_Score = st.number_input("Extra Curricular Score (1-10)", min_value=0, max_value=10, value=0)
    Communication_Skills = st.number_input("Communication Skills (1-10)", min_value=1, max_value=10, value=1)
    Projects_Completed = st.number_input("Projects Completed", min_value=0, max_value=20, value=0)

    submitted = st.form_submit_button("🔍 Predict Placement")

# --------------------------------------------------
# Prediction Logic
# --------------------------------------------------
if submitted:
    internship = 1 if Internship_Experience == "Yes" else 0

    # ✅ Create DataFrame with correct column names and order
    input_df = pd.DataFrame([{
        'IQ': IQ,
        'Prev_Sem_Result': Prev_Sem_Result,
        'CGPA': CGPA,
        'Academic_Performance': Academic_Performance,
        'Internship_Experience': internship,
        'Extra_Curricular_Score': Extra_Curricular_Score,
        'Communication_Skills': Communication_Skills,
        'Projects_Completed': Projects_Completed
    }])

    # Scale input properly
    input_scaled = scaler.transform(input_df)

    # Predict
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    # Display Result
    st.subheader("📊 Prediction Result")
    if prediction == 1:
        st.success(f"✅ The student is **likely to get placed**! (Confidence: {probability*100:.2f}%)")
    else:
        st.error(f"❌ The student is **unlikely to get placed**. (Confidence: {(1-probability)*100:.2f}%)")

    # --------------------------------------------------
    # Optional: Show user inputs in a summary table
    # --------------------------------------------------
    st.markdown("### 🧩 Input Summary")
    st.dataframe(input_df)
