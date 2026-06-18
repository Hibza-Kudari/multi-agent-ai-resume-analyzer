import json
import re
import ollama


def extract_skills_from_jd(job_description, model="llama3.2"):
    """
    Uses the local LLM to extract a clean list of required skills
    from ANY job description, regardless of role/domain (engineering,
    HR, sales, marketing, etc.) — replaces the fixed SKILLS list
    approach for JD-side skill detection.

    Returns a list of skill strings, e.g. ["Python", "Recruitment",
    "Excel", "Stakeholder Management"].
    """

    if not job_description or not job_description.strip():
        return []

    prompt = f"""
Extract the key skills, tools, and qualifications required for this job.
Include both technical and non-technical skills relevant to the role
(e.g. software tools, soft skills, domain knowledge, certifications).

Respond ONLY with a JSON array of short skill names, nothing else.
No explanations, no markdown, no preamble.

Example format:
["Python", "Recruitment", "Excel", "Communication"]

Job Description:
{job_description}
"""

    try:
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )

        raw = response["message"]["content"].strip()

        # Strip markdown code fences if the model added them anyway
        raw = re.sub(r"^```(?:json)?|```$", "", raw, flags=re.MULTILINE).strip()

        skills = json.loads(raw)

        if not isinstance(skills, list):
            return []

        # Clean and dedupe, preserve original casing for display
        cleaned = []
        seen = set()

        for s in skills:
            if not isinstance(s, str):
                continue
            s_clean = s.strip()
            key = s_clean.lower()
            if s_clean and key not in seen:
                cleaned.append(s_clean)
                seen.add(key)

        return cleaned

    except (json.JSONDecodeError, KeyError, Exception) as e:
        print("Skill extraction failed:", e)
        return []