from agents.ats_agent import ats_agent
from agents.skill_gap_agent import skill_gap_agent
from agents.feedback_agent import feedback_agent
from agents.interview_agent import interview_agent


def supervisor_agent(resume_text, job_description):
    """
    Supervisor Agent:
    Orchestrates the complete resume analysis workflow.

    Workflow:
    1. ATS Analysis
    2. Skill Gap Analysis
    3. AI Feedback
    4. Interview Generation (always runs)
    """

    report = {}
    decisions = []

    # ----------------------------------
    # Step 1: ATS Analysis
    # ----------------------------------

    ats_result = ats_agent(
        resume_text,
        job_description,
    )

    report["ats"] = ats_result

    decisions.append("Ran ATS agent.")

    ats_score = ats_result.get("ats_score", 0)

    # ----------------------------------
    # Step 2: Skill Gap Analysis
    # ----------------------------------

    if job_description and job_description.strip():

        gap_result = skill_gap_agent(
            resume_text,
            job_description,
        )

        report["skill_gap"] = gap_result

        decisions.append("Ran Skill Gap agent.")

    else:

        report["skill_gap"] = {"missing_skills": []}

        decisions.append("Skipped Skill Gap agent (no job description).")

    missing_skills = report["skill_gap"].get("missing_skills", [])

    missing_count = len(missing_skills)

    # ----------------------------------
    # Step 3: AI Feedback (Always)
    # ----------------------------------

    feedback_result = feedback_agent(
        resume_text,
        job_description,
        missing_skills,
    )

    report["feedback"] = feedback_result

    decisions.append("Ran Feedback agent.")

    # ----------------------------------
    # Step 4: Interview Agent (Always)
    # ----------------------------------

    interview_result = interview_agent(
        resume_text,
        job_description,
    )

    report["interview"] = interview_result

    decisions.append(
        f"Ran Interview agent "
        f"(ATS={ats_score}, Missing Skills={missing_count})."
    )

    # ----------------------------------
    # Final Report
    # ----------------------------------

    report["supervisor_decisions"] = decisions

    return report