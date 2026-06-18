# 🤖 Multi-Agent AI Resume Analyzer

Multi-Agent AI Resume Analyzer is an AI-powered career assistant that combines OCR, Large Language Models (Ollama Llama 3.2), and a collaborative multi-agent architecture to automate resume screening and career guidance.

The system analyzes resumes against job descriptions, dynamically extracts role requirements, evaluates ATS compatibility, identifies skill gaps, generates personalized interview questions, and provides actionable recommendations. Unlike traditional ATS tools, the analyzer supports both technical and non-technical roles through domain-agnostic job requirement extraction and confidence-aware scoring.

## 🚀 Features

### 📄 Resume Parsing
- Extracts text directly from PDF resumes using PyMuPDF.
- Automatically falls back to EasyOCR for scanned or image-based resumes.
- Supports both digital and scanned PDF formats.

### 🎯 ATS & Job Match Analysis
- Dynamically extracts role requirements from job descriptions.
- Computes ATS compatibility and job-match scores.
- Domain-Agnostic ATS Analysis and Multi-Agent Decision Workflow
- Works across technical and non-technical domains (AI/ML, HR, Marketing, Finance, etc.).
- Includes confidence-aware scoring to prevent misleading results from insufficient job description data.
- Personalized Interview Preparation and AI-Powered Career Feedback
---
---

## Screenshots

### Home Page
![Home](screenshots/home.png)

### Resume Analysis
![Analysis](screenshots/analysis.png)

### Skills Detection
![Skills](screenshots/skills.png)

### AI Feedback
![AI Feedback](screenshots/ai_analysis.png)

### Interview Questions Generator
![Interview Questions](screenshots/interview_questions.png)

---

### Resume Analysis

* Upload Resume PDFs
* OCR support for scanned resumes
* Resume text extraction using PyMuPDF and EasyOCR
* ATS Compatibility Analysis
* Confidence-Aware Job Matching
* Resume Quality Evaluation

### Skill Assessment

* Dynamic Skill Extraction from Job Descriptions
* Domain-Agnostic Skill Gap Analysis
* Missing Skills Detection
* Job Description Matching
* Learning Recommendations

### AI-Powered Career Guidance

* AI Resume Feedback using Ollama (Llama 3.2)
* Personalized Career Recommendations
* Resume Improvement Suggestions
* Career Readiness Assessment

### Interview Preparation

* Personalized Interview Question Generation
* Technical Questions
* Project-Based Questions
* HR Questions
* Role-Specific Assessments

### Dashboard & Reporting

* Interactive Dashboard
* ATS Compatibility Metrics
* Visual Skill Match Analysis
* Download AI Feedback
* Download Interview Questions

---

### Multi-Agent Workflow
- Supervisor agent routes tasks based on intermediate analysis.
- ATS Analysis Agent evaluates resume-job fit.
- Skill Gap Agent identifies missing skills from dynamically extracted job requirements.
- Interview Agent generates role-specific interview questions.

### ATS Agent

* Calculates ATS compatibility
* Analyzes resume-job alignment
* Performs confidence-aware job matching
* Detects low-information job descriptions
* Generates job match metrics

### Skill Gap Agent

* Extracts role requirements dynamically
* Identifies missing skills from job descriptions
* Performs domain-agnostic skill-gap analysis
* Suggests learning priorities

### Interview Agent

* Generates personalized interview questions
* Creates technical assessments
* Produces HR interview questions
* Builds project-based evaluations
* Adapts questions to job requirements

### Supervisor Agent

* Coordinates all agents
* Routes analysis workflows
* Aggregates agent outputs
* Generates final recommendations
* Produces consolidated analysis reports

---

## System Architecture

```text
Resume PDF
     │
     ▼
OCR / Text Extraction
     │
     ▼
Supervisor Agent
     │
 ┌───┼─────────┐
 ▼   ▼         ▼
ATS Skill   Interview
Agent Gap     Agent
      Agent
 └────┼────────┘
      ▼
Final Career Report
```

---



---

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Artificial Intelligence

* Ollama
* Llama 3.2
* OCR-Based Resume Parsing
* Dynamic Skill Extraction

### NLP & Resume Processing

* EasyOCR
* PyMuPDF
* Resume Parsing
* Skill Extraction

### Data Visualization

* Plotly
* Pandas
* NumPy

### Development Tools

* Git
* GitHub

---

## Skills Demonstrated

* Artificial Intelligence
* Multi-Agent Systems
* Large Language Models (LLMs)
* Natural Language Processing (NLP)
* OCR Processing
* Resume Parsing
* ATS Optimization
* Prompt Engineering
* Python Development
* Streamlit Application Development
* Data Visualization
* Career Intelligence Systems

---

## Performance

* Supports Digital and Scanned PDF Resumes
* Domain-Agnostic Resume Evaluation
* Dynamic Skill Extraction from Job Descriptions
* Confidence-Aware ATS Scoring
* Personalized Interview Question Generation
* Multi-Agent Career Guidance Workflow
* Automated Skill Gap Detection

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/ai-resume-analyzer.git
```

### Navigate to Project Directory

```bash
cd ai-resume-analyzer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## Project Structure

```text
src/
│
├── agents/
│   ├── ats_agent.py
│   ├── skill_gap_agent.py
│   ├── interview_agent.py
│   └── supervisor_agent.py
│
├── app.py
├── ocr_helper.py
├── ollama_helper.py
├── skills.py
├── requirements.txt
│
└── screenshots/
```

---

## AI Interview Preparation

The Interview Agent generates customized interview questions based on:

* Resume content
* Candidate skills
* Projects listed in the resume
* Job description requirements
* ATS evaluation results

### Question Categories

* Technical Questions
* Project-Based Questions
* Behavioral Questions
* HR Questions
* Role-Specific Questions

Powered by Ollama (Llama 3.2).

---

## Future Enhancements

* Resume Ranking System
* Multi-Resume Comparison
* AI Career Roadmap Generator
* PDF Report Export
* Recruiter Dashboard
* Cloud Deployment
* LangChain Integration
* Vector Database Support
* RAG-Based Resume Analysis
* Interview Performance Evaluation

---

## Author

**Hibza Kudari**

B.Tech Student – Artificial Intelligence & Machine Learning

Passionate about Artificial Intelligence, Machine Learning, Generative AI, and Intelligent Agent Systems.
