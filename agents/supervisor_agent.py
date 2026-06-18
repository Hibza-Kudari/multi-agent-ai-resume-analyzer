from agents.ats_agent import ats_agent
from agents.skill_gap_agent import skill_gap_agent
from agents.interview_agent import interview_agent


def supervisor_agent(resume_text, job_description):
    """
    Supervisor Agent: orchestrates the analysis pipeline with
    conditional logic — later agents only run when earlier
    results justify it, and decisions are logged so the routing
    is explainable.
    """

    report = {}
    decisions = []

    # Step 1: Always run ATS analysis first — it's the cheapest
    # signal and determines whether deeper analysis is worthwhile.
    ats_result = ats_agent(resume_text, job_description)
    report["ats"] = ats_result
    decisions.append("Ran ATS agent (baseline keyword-match check).")

    ats_score = ats_result.get("ats_score", 0)

    # Step 2: Only run skill-gap analysis if there's an actual
    # job description to compare against — otherwise there's
    # nothing meaningful to find a "gap" relative to.
    if job_description and job_description.strip():
        gap_result = skill_gap_agent(resume_text, job_description)
        report["skill_gap"] = gap_result
        decisions.append("Ran skill-gap agent (job description present).")
    else:
        report["skill_gap"] = {"missing_skills": []}
        decisions.append("Skipped skill-gap agent (no job description provided).")

    # Step 3: Only generate interview questions if the ATS score
    # clears a minimum bar — no point prepping interview questions
    # for a resume that wouldn't pass initial screening, unless the
    # missing-skills list is short enough to be closeable.
    missing_count = len(report["skill_gap"].get("missing_skills", []))

    should_generate_interview = (
        ats_score >= 40 or missing_count <= 2
    )

    if should_generate_interview:
        interview_result = interview_agent(resume_text, job_description)
        report["interview"] = interview_result
        decisions.append(
            f"Ran interview agent (ATS score {ats_score}, "
            f"{missing_count} missing skills met threshold)."
        )
    else:
        report["interview"] = None
        decisions.append(
            f"Skipped interview agent (ATS score {ats_score} too low "
            f"and {missing_count} missing skills — recommend strengthening "
            f"resume before interview prep)."
        )

    report["supervisor_decisions"] = decisions

    return report