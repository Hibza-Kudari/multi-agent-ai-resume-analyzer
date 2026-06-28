import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,
)


def ask_ollama(prompt):
    """
    Kept the same function name so the rest of the project
    doesn't need to change.
    """

    try:
        response = llm.invoke(prompt)
        return response.content

    except Exception as e:
        return f"❌ Groq Error: {e}"


def get_ai_feedback(
    resume_text,
    job_description,
    missing_skills,
):
    prompt = f"""
You are an expert ATS Resume Reviewer.

Resume:
{resume_text[:2500]}

Job Description:
{job_description}

Missing Skills:
{', '.join(missing_skills)}

Provide:

1. Resume Strengths
2. Resume Weaknesses
3. Missing Skills Analysis
4. ATS Improvement Suggestions
5. ATS Score out of 100

Keep the answer concise.
"""

    return ask_ollama(prompt)