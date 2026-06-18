from skill_extractor import extract_skills_from_jd


def skill_gap_agent(resume_text, job_description):
    """
    Domain-agnostic skill-gap agent.

    Extracts required skills from the job description dynamically
    (works for any role — engineering, HR, sales, etc.) and checks
    which ones are missing from the resume.
    """

    jd_skills = extract_skills_from_jd(job_description)

    if not jd_skills:
        return {
            "missing_skills": [],
            "message": "Could not determine required skills from the job description.",
        }

    resume_lower = resume_text.lower()

    missing_skills = [
        skill for skill in jd_skills
        if skill.lower() not in resume_lower
    ]

    return {
        "missing_skills": missing_skills,
        "total_required": len(jd_skills),
    }