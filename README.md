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

This project uses a Linear Regression model to predict employee salaries based on input features like age, gender, degree, job title, and years of experience. The model achieves a strong performance with an R² score of 0.8911, meaning it explains about 89% of the variance in salary data. This high R² value indicates that the model fits the data well and is effective at capturing the relationship between employee characteristics and salary outcomes.

Before training, categorical features such as Gender, Degree, and Job Title were label encoded, while numerical features like Age and Experience were standardized using StandardScaler to ensure uniform scaling. In addition, missing values and duplicate records were removed during preprocessing to improve model reliability and accuracy.

Overall, the model provides reliable and consistent salary estimates with a relatively low prediction error. Its strong performance makes it suitable for a variety of applications, including salary benchmarking, workforce planning, compensation strategy design, and HR analytics. By leveraging this model, organizations can gain valuable insights into the factors influencing employee pay and make more informed, data-driven decisions.


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

