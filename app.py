import streamlit as st
import pandas as pd
import joblib

@st.cache_resource
def load_model(path):
    try:
        return joblib.load(path)
    except FileNotFoundError:
        st.error(f"Error: Model file '{path}' not found.")
        st.stop()
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.stop()

model = load_model("best_salary_model.pkl")

st.set_page_config(page_title="Employee Salary Predictor", layout="centered")


st.markdown("""
<style>
/* General padding fix */
div.block-container {
    padding-top: 1.5rem;
}

/* Main Title */
h2.main-title {
    color: #007bff;
    text-align: center;
    font-size: 2.2em;
    margin-bottom: 10px;
}

/* Section Titles */
h2.form-title {
    font-size: 1.2em;
    font-weight: bold;
    color: #3b82f6;
    text-align: center;
    margin: 5px 0;
}

/* Info Box */
.info-box-simple {
    border: 1px solid #4a5568;
    border-radius: 8px;
    padding: 12px;
    margin-bottom: 20px;
    background-color: #1a202c;
    display: grid;
    gap: 5px;
}

/* Predict Button Wrapper */
.predict-button-wrapper {
    display: flex;
    justify-content: center;
    margin-top: 10px;
}

/* Predict Button */
button.st-emotion-cache-19rxjzo {
    background-color: #143d75 !important;
    color: white !important;
    border: none;
    padding: 12px 30px;
    font-weight: bold;
    border-radius: 8px;
    font-size: 1.1em;
    cursor: pointer;
    transition: background-color 0.3s ease;
}
button.st-emotion-cache-19rxjzo:hover {
    background-color: #e63946 !important;
}

/* Result Box */
.result-box-simple {
    margin-top: 30px;
    padding: 20px;
    border-radius: 12px;
    background-color: #1a202c;
    color: #e2e8f0;
    font-size: 16px;
    font-weight: bold;
    text-align: center;
    border: 2px solid #00B386;
}
.result-box-simple h4 {
    margin-bottom: 10px;
    font-size: 1.1em;
}
.result-box-simple p.salary {
    font-size: 1.8em;
    margin: 0;
    color: #e2e8f0;
}
.result-box-simple p.note {
    margin-top: 10px;
    font-size: 1em;
    font-style: italic;
    color: #a0aec0;
}

/* Footer */
.footer {
    margin-top: 60px;
    padding-top: 20px;
    border-top: 1px solid #ccc;
    text-align: center;
    font-size: 14px;
    color: #888;
}
.footer a {
    color: #007bff;
    text-decoration: none;
    margin: 0 8px;
}
.footer a:hover {
    text-decoration: underline;
}
/* Footer Styling */
.footer {
    position: relative;
    bottom: 0;
    width: 100%;
    padding: 15px 0;
    text-align: center;
    font-size: 14px;
    color: #888;
    background-color: transparent;
    margin-bottom: 0;
}
.footer a {
    color: #007bff;
    text-decoration: none;
    margin: 0 8px;
}
.footer a:hover {
    text-decoration: underline;
}
footer, .st-emotion-cache-1avcm0n {
    display: none;
}
html, body {
    margin: 0;
    padding: 0;
}
html, body, .main, .block-container {
    height: 100%;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
}

.block-container {
    flex: 1 0 auto;
}

/* Footer Styling */
.footer {
    flex-shrink: 0;
    padding: 16px 0 10px 0;
    text-align: center;
    font-size: 17px;
    color: #fff;  /* White text */
    line-height: 1.5;
    background-color: transparent; /* No background color */
    width: 100%;
    margin: 0;
    border-top: none;
}

/* Hide horizontal line if any */
hr {
    display: none;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<h2 class='main-title'>💼 Employee Salary Predictor</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="info-box-simple">
<p>📘 <b>Algorithm Used:</b> Linear Regression</p>
<p>📈 <b>Model R² Score:</b> 89.11%</p>
<p>📊 <b>Evaluation:</b> Compares predicted vs actual salaries.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<h2 class='form-title'>📝 Enter Employee Details</h4>", unsafe_allow_html=True)

age = st.number_input("Age", min_value=18, max_value=100, value=30)
gender = st.selectbox("Gender", ["Male", "Female"])
degree = st.selectbox("Degree", ["Bachelors", "Masters", "PhD"])

job_titles = sorted([
    'Software Engineer', 'Data Analyst', 'Senior Manager',
       'Sales Associate', 'Director', 'Marketing Analyst',
       'Product Manager', 'Sales Manager', 'Marketing Coordinator',
       'Senior Scientist', 'Software Developer', 'HR Manager',
       'Financial Analyst', 'Project Manager', 'Customer Service Rep',
       'Operations Manager', 'Marketing Manager', 'Senior Engineer',
       'Data Entry Clerk', 'Sales Director', 'Business Analyst',
       'VP of Operations', 'IT Support', 'Recruiter', 'Financial Manager',
       'Social Media Specialist', 'Software Manager', 'Junior Developer',
       'Senior Consultant', 'Product Designer', 'CEO', 'Accountant',
       'Data Scientist', 'Marketing Specialist', 'Technical Writer',
       'HR Generalist', 'Project Engineer', 'Customer Success Rep',
       'Sales Executive', 'UX Designer', 'Operations Director',
       'Network Engineer', 'Administrative Assistant',
       'Strategy Consultant', 'Copywriter', 'Account Manager',
       'Director of Marketing', 'Help Desk Analyst',
       'Customer Service Manager', 'Business Intelligence Analyst',
       'Event Coordinator', 'VP of Finance', 'Graphic Designer',
       'UX Researcher', 'Social Media Manager', 'Director of Operations',
       'Senior Data Scientist', 'Junior Accountant',
       'Digital Marketing Manager', 'IT Manager',
       'Customer Service Representative', 'Business Development Manager',
       'Senior Financial Analyst', 'Web Developer', 'Research Director',
       'Technical Support Specialist', 'Creative Director',
       'Senior Software Engineer', 'Human Resources Director',
       'Content Marketing Manager', 'Technical Recruiter',
       'Sales Representative', 'Chief Technology Officer',
       'Junior Designer', 'Financial Advisor', 'Junior Account Manager',
       'Senior Project Manager', 'Principal Scientist',
       'Supply Chain Manager', 'Senior Marketing Manager',
       'Training Specialist', 'Research Scientist',
       'Junior Software Developer', 'Public Relations Manager',
       'Operations Analyst', 'Product Marketing Manager',
       'Senior HR Manager', 'Junior Web Developer',
       'Senior Project Coordinator', 'Chief Data Officer',
       'Digital Content Producer', 'IT Support Specialist',
       'Senior Marketing Analyst', 'Customer Success Manager',
       'Senior Graphic Designer', 'Software Project Manager',
       'Supply Chain Analyst', 'Senior Business Analyst',
       'Junior Marketing Analyst', 'Office Manager', 'Principal Engineer',
       'Junior HR Generalist', 'Senior Product Manager',
       'Junior Operations Analyst', 'Senior HR Generalist',
       'Sales Operations Manager', 'Senior Software Developer',
       'Junior Web Designer', 'Senior Training Specialist',
       'Senior Research Scientist', 'Junior Sales Representative',
       'Junior Marketing Manager', 'Junior Data Analyst',
       'Senior Product Marketing Manager', 'Junior Business Analyst',
       'Senior Sales Manager', 'Junior Marketing Specialist',
       'Junior Project Manager', 'Senior Accountant', 'Director of Sales',
       'Junior Recruiter', 'Senior Business Development Manager',
       'Senior Product Designer', 'Junior Customer Support Specialist',
       'Senior IT Support Specialist', 'Junior Financial Analyst',
       'Senior Operations Manager', 'Director of Human Resources',
       'Junior Software Engineer', 'Senior Sales Representative',
       'Director of Product Management', 'Junior Copywriter',
       'Senior Marketing Coordinator', 'Senior Human Resources Manager',
       'Junior Business Development Associate', 'Senior Account Manager',
       'Senior Researcher', 'Junior HR Coordinator',
       'Director of Finance', 'Junior Marketing Coordinator',
       'Junior Data Scientist', 'Senior Operations Analyst',
       'Senior Human Resources Coordinator', 'Senior UX Designer',
       'Junior Product Manager', 'Senior Marketing Specialist',
       'Senior IT Project Manager', 'Senior Quality Assurance Analyst',
       'Director of Sales and Marketing', 'Senior Account Executive',
       'Director of Business Development', 'Junior Social Media Manager',
       'Senior Human Resources Specialist', 'Senior Data Analyst',
       'Director of Human Capital', 'Junior Advertising Coordinator',
       'Junior UX Designer', 'Senior Marketing Director',
       'Senior IT Consultant', 'Senior Financial Advisor',
       'Junior Business Operations Analyst',
       'Junior Social Media Specialist',
       'Senior Product Development Manager', 'Junior Operations Manager',
       'Senior Software Architect', 'Junior Research Scientist',
       'Senior Financial Manager', 'Senior HR Specialist',
       'Senior Data Engineer', 'Junior Operations Coordinator',
       'Director of HR', 'Senior Operations Coordinator',
       'Junior Financial Advisor', 'Director of Engineering'
])
job_title = st.selectbox("Job Title", job_titles)
experience = st.number_input("Years of Experience", min_value=0, max_value=50, value=5)

st.markdown("<div class='predict-button-wrapper'>", unsafe_allow_html=True)
predict = st.button("Predict Salary")
st.markdown("</div>", unsafe_allow_html=True)

if predict:
    try:
        input_data = pd.DataFrame([{
            "Age": age,
            "Gender_Encode": {"Male": 1, "Female": 0, "Other": 2}.get(gender, 2),
            "Degree_Encode": {"Bachelors": 0, "Masters": 1, "PhD": 2}.get(degree, 0),
            "Job_Title_Encode": {title: idx for idx, title in enumerate(job_titles)}.get(job_title, 0),
            "Experience_Years": experience
        }])
        prediction = model.predict(input_data)[0]

        st.markdown(f"""
        <div class="result-box-simple">
            <h4>💰 Estimated Annual Salary:</h4>
            <p class="salary">₹ {prediction:,.2f}</p>
            <p class="note">Based on your profile details</p>
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Prediction failed: {e}")

st.markdown("<h3 style='color:#007bff; text-align:center;'>📊 Model Evaluation</h3>", unsafe_allow_html=True)
st.image("model_evaluation.png", caption="Actual vs. Predicted Salary", use_container_width=True)

st.markdown("""
<div class="footer">
    Developed by <b>Pavan Putta</b> |
    <a href="https://www.linkedin.com/in/pavan-putta-84ba3528b/" target="_blank">LinkedIn</a> |
    <a href="https://github.com/PavanPutta14" target="_blank">GitHub</a>
</div>
""", unsafe_allow_html=True)

