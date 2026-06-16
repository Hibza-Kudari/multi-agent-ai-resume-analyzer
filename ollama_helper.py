import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def ask_ollama(prompt):

    try:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3.2:latest",
                "prompt": prompt,
                "stream": False
            },
            timeout=300
        )

        response.raise_for_status()

        return response.json()["response"]

    except Exception as e:

        return f"❌ Ollama Error: {str(e)}"


def get_ai_feedback(
    resume_text,
    job_description,
    missing_skills
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