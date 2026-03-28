# AI-Resume-Analyzer
The AI Resume Analyzer is a web-based application that evaluates a candidate’s resume against a given job description using Natural Language Processing (NLP). The system extracts text from uploaded resumes (PDF/DOCX), identifies relevant keywords, and compares them with job requirements to generate an ATS (Applicant Tracking System) score

## 📌 Overview

AI Resume Analyzer is a Python-based web application that analyzes resumes and compares them with job descriptions to generate an ATS score and skill gap insights.


## 🚀 Features

* Upload Resume (PDF/DOCX)
* Extract text automatically
* Keyword extraction using NLP
* Job description matching
* ATS score calculation
* Matched and missing skills display


## 🛠️ Tech Stack

* Python
* Flask
* spaCy (NLP)
* scikit-learn
* pdfminer.six
* python-docx

## 📁 Project Structure

ai-resume-analyzer/
│
├── app.py
├── utils/
│   ├── parser.py
│   ├── analyzer.py
│   └── scorer.py
│
├── templates/
│   └── index.html
├── uploads/
├── requirements.txt
└── README.md

---

## ⚙️ Installation

### 1. Clone Repository

git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Download NLP Model

python -m spacy download en_core_web_sm


## ▶️ Run the Project

python app.py


## 📊 How It Works

1. User uploads resume
2. System extracts text from file
3. Job description is analyzed
4. Keywords are matched
5. ATS score is generated
6. Missing skills are suggested


## 🔮 Future Improvements

* Semantic matching using BERT
* Resume formatting suggestions
* Grammar checking
* Export report as PDF
* Dashboard with charts

## 📌 Use Cases

* Students improving resumes
* Job seekers preparing for ATS systems
* HR screening automation


## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.


## 📜 License

This project is open-source and available under the MIT License.
