# 🚀 Smart ATS Resume Analyzer

An AI-powered Applicant Tracking System (ATS) Resume Analyzer built
using **Flask** that evaluates resumes against job descriptions,
calculates match scores, identifies missing keywords, and provides
intelligent improvement suggestions using the **Google Gemini API**.

------------------------------------------------------------------------

## 📌 Problem Statement

In today's competitive job market, many resumes are filtered out by
Applicant Tracking Systems (ATS) before reaching recruiters. These
systems analyze resumes for keyword relevance and job alignment.

This project provides a scalable AI-based solution to:

-   Evaluate resume compatibility with job descriptions
-   Identify missing keywords
-   Suggest structured improvements
-   Increase interview success probability

------------------------------------------------------------------------

## 💼 Business Use Cases

-   ✅ Resume optimization for ATS compliance
-   ✅ Intelligent keyword gap analysis
-   ✅ Career counseling & HR resume evaluation
-   ✅ Scalable resume analysis solution for institutions
-   ✅ Enhanced job search strategy support

------------------------------------------------------------------------

## ✨ Key Features

### 🔹 Resume--Job Description Match Score

Calculates percentage match between resume and job description.

### 🔹 Keyword Identification

Detects important missing skills and keywords.

### 🔹 AI-Powered Profile Summary

Uses Gemini API for structured analysis and actionable feedback.

### 🔹 Interactive Web Interface

Built using **Flask (Backend)** and **HTML, CSS, JavaScript (Frontend)**
for seamless user experience.

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   **Backend:** Python, Flask\
-   **Frontend:** HTML, CSS, JavaScript\
-   **AI Integration:** Google Gemini API\
-   **Machine Learning:** Scikit-learn\
-   **NLP Techniques:** Text preprocessing, keyword extraction\
-   **PDF Processing:** Resume text extraction libraries\
-   **Environment Management:** Virtual Environment (.env support)

------------------------------------------------------------------------

## ⚙️ How It Works

1️⃣ **Upload Resume (PDF)**\
User uploads resume through the web interface.

2️⃣ **Enter Job Description**\
User pastes job description in the input field.

3️⃣ **Processing & AI Analysis** - Extracts text from PDF - Applies NLP
preprocessing - Compares resume with job description - Uses Gemini API
for intelligent analysis - Generates match score & suggestions

4️⃣ **Results Display** - 📊 Match Score (%) - 🔍 Missing Keywords - 📝
Profile Summary & Improvement Suggestions

------------------------------------------------------------------------

## 📂 Project Structure

    smart-ats-resume-analyzer/
    │
    ├── flask_app.py        # Main Flask application
    ├── helper.py           # Resume parsing & AI logic
    ├── templates/
    │   └── index.html      # Frontend HTML
    ├── static/
    │   ├── style.css       # Styling
    │   └── main.js         # Frontend JS
    ├── requirements.txt
    ├── .env
    └── README.md

------------------------------------------------------------------------

## 🧪 Installation & Setup

### 1️⃣ Clone the Repository

``` bash
git clone <repository-url>
cd smart-ats-resume-analyzer
```

### 2️⃣ Create Virtual Environment

``` bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

**Windows**

``` bash
venv\Scripts\activate
```

**Mac/Linux**

``` bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

### 5️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

    GOOGLE_API_KEY=your_api_key_here

### 6️⃣ Run the Application

``` bash
python flask_app.py
```

OR

``` bash
set FLASK_APP=flask_app.py
flask run
```

Application runs on:

    http://127.0.0.1:5000/

------------------------------------------------------------------------

## 🔮 Future Enhancements

-   Support for `.docx` resumes\
-   Role-based feedback customization\
-   Multilingual resume analysis\
-   Resume analytics dashboard\
-   Integration with job portals\
-   Resume improvement history tracking

------------------------------------------------------------------------

## 🎯 Project Highlights

-   Full-stack implementation (Flask + HTML/CSS/JS)
-   Real-world ATS optimization use case
-   AI-powered resume intelligence
-   NLP + Machine Learning integration
-   Production-ready project structure

------------------------------------------------------------------------

## 👨‍💻 Author

Developed an ATS-based resume analyzer to score resumes and suggest
improvements. Integrated Gemini API for intelligent resume parsing and
skill extraction. Built a responsive Flask-based web interface using
HTML and CSS for end-user accessibility.

