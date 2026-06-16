def skill_gap_agent(resume_text, job_description):

    missing_skills = []

    skills_to_check = [
        "LangChain",
        "LangGraph",
        "Docker",
        "AWS"
    ]

    for skill in skills_to_check:
        if skill.lower() not in resume_text.lower():
            missing_skills.append(skill)

    return {
        "missing_skills": missing_skills
    }