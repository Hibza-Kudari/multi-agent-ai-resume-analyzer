from agents.ats_agent import ats_agent
from agents.skill_gap_agent import skill_gap_agent
from agents.interview_agent import interview_agent

def supervisor_agent(resume_text, job_description):

    report = {}

    # Run ATS Analysis
    ats_result = ats_agent(
        resume_text,
        job_description
    )

    report["ats"] = ats_result

    # Run Skill Gap Analysis
    gap_result = skill_gap_agent(
        resume_text,
        job_description
    )

    interview_result = interview_agent(
    resume_text,
    job_description
)

    report["interview"] = interview_result

    report["skill_gap"] = gap_result

    return report