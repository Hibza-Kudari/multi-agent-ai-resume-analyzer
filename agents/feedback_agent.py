from ollama_helper import get_ai_feedback


def feedback_agent(
    resume_text,
    job_description,
    missing_skills,
):
    """
    Feedback Agent:
    Generates personalized resume feedback using the LLM.
    """

    feedback = get_ai_feedback(
        resume_text,
        job_description,
        missing_skills,
    )

    return {
        "feedback": feedback
    }