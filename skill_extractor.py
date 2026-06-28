import json
import re
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,
)


def extract_skills_from_jd(job_description):
    """
    Uses Groq to extract a clean list of required skills
    from any job description.
    """

    if not job_description or not job_description.strip():
        return []

    prompt = f"""
Extract the key skills, tools, and qualifications required for this job.
Include both technical and non-technical skills relevant to the role
(e.g. software tools, soft skills, domain knowledge, certifications).

Respond ONLY with a JSON array of short skill names.

Example:
["Python", "Recruitment", "Excel", "Communication"]

Job Description:
{job_description}
"""

    try:
        response = llm.invoke(prompt)

        raw = response.content.strip()

        # Remove markdown code fences if present
        raw = re.sub(
            r"^```(?:json)?|```$",
            "",
            raw,
            flags=re.MULTILINE,
        ).strip()

        skills = json.loads(raw)

        if not isinstance(skills, list):
            return []

        cleaned = []
        seen = set()

        for skill in skills:
            if not isinstance(skill, str):
                continue

            skill = skill.strip()
            key = skill.lower()

            if skill and key not in seen:
                cleaned.append(skill)
                seen.add(key)

        return cleaned

    except Exception as e:
        print("Skill extraction failed:", e)
        return []