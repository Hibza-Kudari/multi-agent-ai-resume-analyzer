from ollama_helper import ask_ollama


def interview_agent(
    resume_text,
    job_description
):

    prompt = f"""
You are an expert technical interviewer.

Resume:

{resume_text}

Job Description:

{job_description[:3000]}

IMPORTANT RULES:

1. Generate questions ONLY from information explicitly present in the resume.
2. Use project names exactly as written.
3. Use technologies exactly as written.
4. Do NOT invent projects.
5. Do NOT invent technologies.
6. Do NOT invent skills.
7. Do NOT invent certifications.
8. Do NOT invent work experience.
9. Do NOT mention TensorFlow, PyTorch, CNN, AWS, Docker, OpenCV, LangChain, FastAPI, etc. unless they appear in the resume.
10. If a project is mentioned, generate questions specifically about that project.
11. Questions must be personalized to this candidate.
12. Return ONLY interview questions.

Output format:

### Technical Questions
1.
2.
3.

### Project Questions
1.
2.
3.

### HR Questions
1.
2.
"""

    return ask_ollama(prompt)