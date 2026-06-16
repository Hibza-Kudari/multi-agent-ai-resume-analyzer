# Multi-Agent AI Resume Analyzer

An intelligent AI-powered career assistant built using Python, Streamlit, Ollama, OCR, ATS-based resume evaluation, and autonomous AI agents. The system analyzes resumes, identifies skill gaps, evaluates ATS compatibility, generates personalized interview questions, and provides actionable career recommendations.

---

## Overview

Multi-Agent AI Resume Analyzer leverages OCR, Natural Language Processing (NLP), Large Language Models (Ollama Llama 3.2), and a collaborative multi-agent architecture to automate resume screening and career guidance.

The application simulates a real-world AI workflow where specialized agents work together to evaluate resumes, match job requirements, identify missing skills, and prepare candidates for interviews.

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
* Resume text extraction
* ATS Resume Scoring
* Resume quality evaluation

### Skill Assessment

* Skill Extraction
* Missing Skills Detection
* Job Description Matching
* Skill Gap Analysis
* Learning Recommendations

### AI-Powered Career Guidance

* AI Resume Feedback using Ollama (Llama 3.2)
* Personalized Career Recommendations
* Resume Improvement Suggestions

### Interview Preparation

* Personalized Interview Question Generation
* Technical Questions
* Project-Based Questions
* HR Questions
* Role-Specific Assessments

### Dashboard & Reporting

* Interactive Dashboard
* Visual Skill Match Analysis
* Download AI Feedback
* Download Interview Questions

---

## Multi-Agent Architecture

The system consists of four specialized AI agents that collaborate to analyze resumes and generate career insights.

### ATS Agent

* Calculates ATS score
* Evaluates resume quality
* Matches resumes against job descriptions
* Measures keyword relevance

### Skill Gap Agent

* Extracts technical and soft skills
* Identifies missing skills
* Recommends learning areas
* Suggests improvements

### Interview Agent

* Generates personalized interview questions
* Creates technical assessments
* Produces HR interview questions
* Builds project-based evaluations

### Supervisor Agent

* Coordinates all agents
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
* Prompt Engineering
* Multi-Agent Systems

### NLP & Resume Processing

* EasyOCR
* PyMuPDF
* Resume Parsing
* Skill Extraction

### Data Visualization

* Plotly

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

* Supports PDF Resume Analysis
* Processes both digital and scanned resumes
* Extracts 100+ common technical skills
* Generates personalized interview questions
* Performs ATS-based job matching
* Provides AI-generated career feedback
* Detects missing skills based on job descriptions

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
