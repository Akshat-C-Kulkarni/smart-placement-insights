<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 200" width="900" height="200">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0f172a"/>
      <stop offset="100%" style="stop-color:#1e3a5f"/>
    </linearGradient>
    <linearGradient id="accent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#38bdf8"/>
      <stop offset="100%" style="stop-color:#818cf8"/>
    </linearGradient>
  </defs>
  <rect width="900" height="200" fill="url(#bg)" rx="12"/>
  <!-- Grid lines -->
  <line x1="0" y1="50" x2="900" y2="50" stroke="#ffffff08" stroke-width="1"/>
  <line x1="0" y1="100" x2="900" y2="100" stroke="#ffffff08" stroke-width="1"/>
  <line x1="0" y1="150" x2="900" y2="150" stroke="#ffffff08" stroke-width="1"/>
  <line x1="150" y1="0" x2="150" y2="200" stroke="#ffffff08" stroke-width="1"/>
  <line x1="300" y1="0" x2="300" y2="200" stroke="#ffffff08" stroke-width="1"/>
  <line x1="600" y1="0" x2="600" y2="200" stroke="#ffffff08" stroke-width="1"/>
  <line x1="750" y1="0" x2="750" y2="200" stroke="#ffffff08" stroke-width="1"/>
  <!-- Bar chart decoration -->
  <rect x="680" y="120" width="18" height="60" fill="#38bdf820" rx="3"/>
  <rect x="706" y="90" width="18" height="90" fill="#38bdf840" rx="3"/>
  <rect x="732" y="60" width="18" height="120" fill="#38bdf860" rx="3"/>
  <rect x="758" y="40" width="18" height="140" fill="#38bdf880" rx="3"/>
  <rect x="784" y="70" width="18" height="110" fill="#38bdf860" rx="3"/>
  <rect x="810" y="100" width="18" height="80" fill="#38bdf840" rx="3"/>
  <rect x="836" y="50" width="18" height="130" fill="#818cf860" rx="3"/>
  <!-- Scatter plot dots -->
  <circle cx="640" cy="80" r="4" fill="#38bdf8" opacity="0.8"/>
  <circle cx="620" cy="130" r="3" fill="#818cf8" opacity="0.6"/>
  <circle cx="660" cy="110" r="5" fill="#38bdf8" opacity="0.5"/>
  <circle cx="600" cy="60" r="3" fill="#f472b6" opacity="0.7"/>
  <!-- Title -->
  <text x="50" y="85" font-family="'Courier New', monospace" font-size="34" font-weight="bold" fill="url(#accent)">Smart Placement</text>
  <text x="50" y="128" font-family="'Courier New', monospace" font-size="34" font-weight="bold" fill="url(#accent)">Insights</text>
  <text x="50" y="160" font-family="monospace" font-size="13" fill="#94a3b8">ML-powered Student Placement Prediction &amp; Analytics</text>
  <!-- Tag -->
  <rect x="50" y="170" width="110" height="18" rx="9" fill="#38bdf820"/>
  <text x="105" y="183" font-family="monospace" font-size="10" fill="#38bdf8" text-anchor="middle">Machine Learning</text>
</svg>

# Smart Placement Insights

> **ML-based system to analyze placement factors and predict student placement likelihood**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)](https://jupyter.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Pandas](https://img.shields.io/badge/Pandas-Data-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Status](https://img.shields.io/badge/Status-Complete-22c55e?style=flat-square)]()

</div>

---

## Overview

**Smart Placement Insights** is a machine learning pipeline designed to assist academic institutions in understanding and predicting student placement outcomes. By analyzing historical placement data, the system identifies key factors influencing campus recruitment and builds predictive models to estimate a student's likelihood of getting placed.

This project bridges the gap between raw academic/extracurricular data and actionable placement intelligence — offering both prediction capability and interpretable insights for students and institutions alike.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   Smart Placement Insights                   │
│                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │  Raw Data    │───▶│  EDA &       │───▶│  Feature     │  │
│  │  Ingestion   │    │  Cleaning    │    │  Engineering │  │
│  └──────────────┘    └──────────────┘    └──────┬───────┘  │
│                                                 │           │
│  ┌──────────────┐    ┌──────────────┐    ┌──────▼───────┐  │
│  │  Prediction  │◀───│  Model       │◀───│  Encoding &  │  │
│  │  Output      │    │  Evaluation  │    │  Scaling     │  │
│  └──────────────┘    └──────────────┘    └──────────────┘  │
│                                                             │
│  Models: Logistic Regression · Decision Tree · Random Forest│
└─────────────────────────────────────────────────────────────┘
```

---

## Key Features

- **Exploratory Data Analysis (EDA)** — Visual analysis of placement trends across CGPA, skills, internships, and extracurriculars
- **Multi-Model Comparison** — Evaluates multiple classifiers and selects the best-performing model
- **Feature Importance Analysis** — Identifies the top factors driving placement outcomes
- **Placement Probability Scoring** — Outputs a probability score for each student profile
- **Insight Visualizations** — Clear, interpretable charts for academic decision-makers

---

## Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.9+ |
| Notebook | Jupyter |
| Data Processing | Pandas, NumPy |
| ML Models | scikit-learn |
| Visualization | Matplotlib, Seaborn |

---

## Getting Started

```bash
# Clone the repository
git clone https://github.com/Akshat-C-Kulkarni/smart-placement-insights.git
cd smart-placement-insights

# Install dependencies
pip install -r requirements.txt

# Launch the notebook
jupyter notebook
```

---

## Project Structure

```
smart-placement-insights/
├── data/                  # Raw and processed datasets
├── notebooks/             # EDA and modeling notebooks
├── models/                # Saved model artifacts
├── utils/                 # Helper functions
├── requirements.txt
└── README.md
```

---

## Results

The model achieves high accuracy in predicting placement outcomes, with key findings:

- **CGPA** and **internship experience** are among the strongest predictors
- **Communication skills** and **technical aptitude** have significant combined impact
- Random Forest outperforms other baselines in cross-validation

---

## Author

**Akshat C. Kulkarni**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/akshatckulkarni)
[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=flat-square&logo=github)](https://github.com/Akshat-C-Kulkarni)

---

<div align="center"><sub>Built with Python · scikit-learn · Jupyter</sub></div>
