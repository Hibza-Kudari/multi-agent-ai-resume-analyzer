import re


def _extract_keywords(text):
    """
    Extract meaningful keywords from text: lowercase words,
    stripped of punctuation, excluding very short/common words.
    """
    STOPWORDS = {
        "the", "and", "for", "with", "this", "that", "from",
        "are", "was", "were", "will", "have", "has", "had",
        "you", "your", "our", "their", "a", "an", "in", "on",
        "of", "to", "is", "as", "be", "or", "at", "by", "we",
    }

    words = re.findall(r"[a-zA-Z][a-zA-Z0-9+#.]*", text.lower())

    keywords = [
        w for w in words
        if len(w) > 2 and w not in STOPWORDS
    ]

    return keywords


def ats_agent(resume_text, job_description):
    """
    ATS Agent: scores resume-job fit based on keyword overlap.

    Extracts keywords from the job description, checks how many
    appear in the resume, and produces a score out of 100 along
    with the specific matched/missing keywords so the result is
    explainable, not just a number.
    """

    if not job_description or not job_description.strip():
        return {
            "ats_score": 0,
            "matched_keywords": [],
            "missing_keywords": [],
            "message": "No job description provided — cannot score ATS match.",
        }

    jd_keywords = set(_extract_keywords(job_description))
    resume_keywords = set(_extract_keywords(resume_text))

    if not jd_keywords:
        return {
            "ats_score": 0,
            "matched_keywords": [],
            "missing_keywords": [],
            "message": "Could not extract keywords from job description.",
        }

    matched = sorted(jd_keywords & resume_keywords)
    missing = sorted(jd_keywords - resume_keywords)

    raw_score = (len(matched) / len(jd_keywords)) * 100
    ats_score = round(min(raw_score, 100))

    if ats_score >= 75:
        message = "Strong keyword match with job description."
    elif ats_score >= 50:
        message = "Moderate keyword match — consider adding more relevant terms."
    else:
        message = "Low keyword match — resume may be filtered out by ATS systems."

    return {
        "ats_score": ats_score,
        "matched_keywords": matched[:25],
        "missing_keywords": missing[:25],
        "message": message,
    }