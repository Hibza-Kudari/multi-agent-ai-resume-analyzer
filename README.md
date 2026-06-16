# Multi-Agent AI Resume Analyzer

An AI-powered career assistant built with Python, Streamlit, Ollama, OCR, ATS-based skill matching, and autonomous AI agents for resume analysis, interview preparation, and career guidance.

## Features

* Upload Resume PDFs
* OCR support for scanned resumes
* Skill Extraction
* ATS Resume Scoring
* Job Description Matching
* Missing Skills Detection
* AI-Powered Resume Feedback using Ollama
* Personalized Interview Question Generator
* Download AI Feedback
* Download Interview Questions
* Interactive Dashboard
* Visual Skill Match Analysis

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

## Tech Stack

* Python
* Streamlit
* Ollama (Llama 3.2)
* EasyOCR
* PyMuPDF
* Plotly

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

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
## AI Interview Preparation

Generate personalized interview questions based on:

- Resume content
- Candidate skills
- Projects mentioned in the resume
- Job Description requirements

Question Categories:

- Technical Questions
- Project-Based Questions
- HR Questions

Powered by Ollama (Llama 3.2).

## Future Improvements

* Resume Recommendations
* PDF Report Export
* Multi-Resume Comparison
* Cloud Deployment

## Author

Hibza Kudari
