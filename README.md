# 💼 Employee Salary Predictor

Predict employee salaries based on profile details using a trained machine learning model.  
Built with Python, Streamlit, and scikit-learn, this application provides an interactive and accurate way to estimate salaries using real-world job data.

---

## ✨ Features

- 🔎 Predicts salary based on:
  - Age
  - Gender
  - Educational Qualification
  - Job Title
  - Years of Experience
- 📈 Uses a trained Linear Regression model with high accuracy (R² ≈ 0.89)
- 📊 Visual comparison of actual vs. predicted salaries
- 💡 Clean, responsive UI with custom CSS styling
- ⚡ Real-time, fast, and interactive predictions

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend / ML**:
  - `scikit-learn` for modeling and evaluation
  - `pandas` and `numpy` for data preprocessing
  - `joblib` for model serialization

---

## 🛠️ How to Run the App

### ▶️ Step 1: Clone the repository
```bash
git clone https://github.com/your-username/employee-salary-predictor.git
cd employee-salary-predictor
```
### ▶️ Step 2: Install dependencies
```bash
pip install -r requirements.txt
```
### ▶️ Step 3: Run the Streamlit app
```bash
streamlit run app.py
```
### ▶️ Step 4: Use the App
The app will open in your browser.
Enter employee details like age, gender, degree, job title, and experience.
🎯 The app will display the predicted annual salary instantly!

---

## 📚 Model Info

This project uses a Linear Regression model to predict employee salaries based on input features like age, gender, degree, job title, and years of experience. The model achieves a high accuracy with an R² score of 0.8911, meaning it explains approximately 89% of the variance in salary data.

Before training, categorical features (Gender, Degree, and Job Title) were label encoded, and numerical features (Age and Experience) were standardized using StandardScaler. Missing values and duplicate records were also removed during preprocessing.

Model performance was evaluated using multiple metrics:  
- Mean Absolute Error (MAE): ₹10,570  
- Mean Squared Error (MSE): ₹205 million  
- Root Mean Squared Error (RMSE): ₹14,344  
These results indicate the model provides reliable salary estimates with reasonable prediction error.
---
### 📁 Project Structure
```
├── app.py                   
├── best_salary_model.pkl   
├── model_evaluation.png    
├── Salary Data.csv         
├── requirements.txt        
└── README.md
```              
---
🔗 **Click here to view the application**: [https://employee-salary-prediction-machine-learning.streamlit.app/](https://employee-salary-prediction-machine-learning.streamlit.app/)

