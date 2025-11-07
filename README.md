# Smart Placement Insights and Prediction System

## 🎯 Aim
To analyze student academic and behavioral data to identify key factors influencing placement success and predict a student’s placement likelihood using machine learning.

## 🧠 Description
This project builds a machine learning–based prediction system that estimates a student’s chance of getting placed based on various academic and behavioral factors such as CGPA, IQ, internship experience, and communication skills.

The model was trained on the “Eman Fatima – College Placement Analysis” dataset, followed by feature engineering, data balancing using SMOTE, and model optimization.
The final model — a Random Forest Classifier — is deployed through an interactive Streamlit web app that allows users to input student data and view placement predictions in real-time.

## 📊 Dataset
The dataset used in this project is stored locally in the /data/ folder and not uploaded to GitHub to keep the repository lightweight.
You can download the dataset from the same source used in this project — “Eman Fatima – College Placement Analysis” (Kaggle) — and place it inside the data/ folder before running the notebooks.

## ⚙️ Project Structure
smart-placement-insights/<br>
│<br>
├── data/               # Datasets<br>
├── notebooks/          # Jupyter notebooks for EDA and modeling<br>
├── src/                # Python scripts for preprocessing and training<br>
├── app/                # Streamlit app files<br>
├── model/              # Saved model and encoders<br>
├── reports/            # Documentation, visualizations<br>
└── requirements.txt    # Required dependencies to set up the project environment<br>


## 🤖 Model Summary
- Algorithm: Random Forest Classifier
- Handling Imbalance: Applied SMOTE on the training data
- Scaler Used: StandardScaler
### Test Set Performance:
- Accuracy: 99.95%
- Precision: 0.9970
- Recall: 1.0000
- F1-Score: 0.9985

## 🔍 Key Insights
Most impactful features: IQ, Communication Skills, CGPA, and Projects Completed
Students with higher technical, academic, and soft skill indicators show greater placement likelihood
Clear positive correlation between CGPA and Placement Outcome


## 🚀 Output
### An interactive Streamlit-based web dashboard that:
- Accepts student profile inputs
- Displays placement prediction results with confidence scores
- Shows real-time model inference for individual students

## 📦 How to Run the App
### 1. Install dependencies:
pip install -r requirements.txt
### 2. Run the Streamlit app:
streamlit run app/app.py
### 3. Enter student details and view placement predictions instantly.

## 📈 Outcomes
- Built a full end-to-end ML pipeline (EDA → Feature Engineering → Model Training → Deployment)
- Gained insights into factors affecting campus placements
- Hands-on experience in model balancing, evaluation, and deployment using Streamlit
- Deployed a fully functional placement prediction web application

## 🔮 Next Steps / Future Improvements
- Integrate SHAP or LIME for explainable AI insights on individual predictions
- Expand the dataset to include soft-skill and aptitude test metrics
- Enable batch predictions by uploading student data in CSV format
- Deploy the Streamlit app on Render / Hugging Face / Streamlit Cloud for public access
- Integrate a dashboard for placement analytics with department-wise trends


---