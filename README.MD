# Network Intrusion Detection System Using Machine Learning

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--learn-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Project Objectives](#project-objectives)
- [Dataset Information](#dataset-information)
- [Technology Stack](#technology-stack)
- [Project Workflow](#project-workflow)
- [Results](#results)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Project Overview

The **Network Intrusion Detection System (NIDS)** Using Machine Learning is a cybersecurity-focused project designed to detect malicious network activities and unauthorized access attempts in real time.

This project applies machine learning techniques to classify network traffic and detect potential cyber threats, enabling proactive threat monitoring and incident response.

## ⚠️ Problem Statement

As organizations increasingly rely on digital infrastructure, cyberattacks such as denial-of-service attacks, unauthorized access attempts, and malicious network activities have become more frequent and sophisticated.

**The objective of this project is to build a machine learning-based intrusion detection system capable of identifying suspicious network activities and classifying potential attacks.**

## 🎪 Project Objectives

- ✅ Analyze network traffic data
- ✅ Detect anomalous and malicious network behavior
- ✅ Perform data preprocessing and feature engineering
- ✅ Train machine learning models for intrusion detection
- ✅ Evaluate model performance using classification metrics
- ✅ Build a scalable security monitoring solution
- ✅ Deploy the model for real-time threat detection

## 📊 Dataset Information

The dataset contains network traffic records and connection-related features used to classify normal and malicious activities.

### Features

**Network Traffic Characteristics:**
- Protocol Type
- Service
- Flag
- Source Bytes
- Destination Bytes
- Connection Duration
- Logged In Status
- Number of Failed Logins
- Count of Connections
- Error Rates
- Traffic Statistics

**Target Variable:**
- Normal Traffic
- Intrusion / Attack

## 🛠️ Technology Stack

### Programming Language
- **Python** (3.8+)

### Machine Learning Libraries
- **Scikit-learn** - Model training and evaluation
- **XGBoost** - Gradient boosting classifier

### Data Analysis & Processing
- **Pandas** - Data manipulation
- **NumPy** - Numerical computations

### Visualization
- **Matplotlib** - Static visualizations
- **Seaborn** - Statistical graphics

### Model Deployment
- **Flask** - Web framework
- **Streamlit** - Interactive dashboards

## 📈 Project Workflow

### 1. Data Collection
- Load network traffic dataset
- Understand data structure and attack categories
- Verify data quality and completeness

### 2. Data Preprocessing
- Handle missing values
- Encode categorical variables
- Scale numerical features
- Address class imbalance if required

### 3. Exploratory Data Analysis (EDA)
- Analyze traffic patterns
- Identify attack distributions
- Study feature correlations
- Detect anomalies and trends

### 4. Feature Engineering
- Select important network features
- Create model-ready datasets
- Improve predictive performance through feature transformation

### 5. Model Development

**Machine learning algorithms evaluated:**
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Gradient Boosting Classifier
- XGBoost Classifier

### 6. Model Evaluation

**Performance metrics used:**
- Accuracy Score
- Precision Score
- Recall Score
- F1 Score
- ROC-AUC Score
- Confusion Matrix

### 7. Deployment

The trained model is deployed through a web application, allowing users to analyze network traffic data and detect potential intrusions in real time.

## 📈 Results

The machine learning model effectively identifies malicious network activities and distinguishes them from normal traffic. The system provides reliable intrusion detection capabilities that can be integrated into existing security infrastructure for enhanced threat detection and response.

## 💻 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/ganeshbgunjal/Network-Intrusion-Detection-System-Using-Machine-Learning.git
cd Network-Intrusion-Detection-System-Using-Machine-Learning
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. **Run the data preprocessing script**
```bash
python preprocess.py
```

2. **Train the model**
```bash
python train.py
```

3. **Launch the web application**
```bash
# Using Streamlit
streamlit run app.py

# Or using Flask
python flask_app.py
```

4. **Access the application**
- Open your browser and navigate to `http://localhost:8000` (Streamlit) or `http://localhost:5000` (Flask)

## 📁 Project Structure

```
Network-Intrusion-Detection-System-Using-Machine-Learning/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── EDA.ipynb
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
├── models/
│   └── trained_model.pkl
├── app.py
├── flask_app.py
├── requirements.txt
├── README.md
└── LICENSE
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Developed by:** [Ganesh B Gunjal](https://github.com/ganeshbgunjal)

**Last Updated:** May 2026
