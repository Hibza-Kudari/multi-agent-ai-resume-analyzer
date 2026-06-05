import streamlit as st
import plotly.express as px

from skills import SKILLS
from ocr_helper import extract_text_from_pdf
from ollama_helper import get_ai_feedback

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ----------------------------------
# CUSTOM CSS
# ----------------------------------

st.markdown("""
<style>

html, body, [class*="css"] {
    font-size: 15px;
}

h1 {
    font-size: 34px !important;
}

div[data-testid="metric-container"] {
    background-color: #111827;
    padding: 15px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------
# TITLE
# ----------------------------------

st.title("📄 AI Resume Analyzer")

st.write(
    "Upload your resume and compare it with a Job Description."
)

# ----------------------------------
# JOB DESCRIPTION
# ----------------------------------

job_description = st.text_area(
    "💼 Paste Job Description",
    height=200
)

# ----------------------------------
# RESUME UPLOAD
# ----------------------------------

uploaded_file = st.file_uploader(
    "📤 Upload Resume PDF",
    type=["pdf"]
)

# ----------------------------------
# PROCESS RESUME
# ----------------------------------

if uploaded_file:

    with st.spinner("Extracting Resume..."):

        text = extract_text_from_pdf(
            uploaded_file
        )

    # ----------------------------------
    # DEBUG SECTION
    # ----------------------------------

    st.write("Text Length:", len(text))

    with st.expander("📄 View Extracted Text"):
        st.text(text[:3000])

    resume_text = text.lower()

    st.success(
        "✅ Resume extracted successfully!"
    )

    # ----------------------------------
    # SKILL DETECTION
    # ----------------------------------

    found_skills = []

    for skill in SKILLS:

        if skill.lower() in resume_text:
            found_skills.append(skill)

    # ----------------------------------
    # RESUME SCORE
    # ----------------------------------

    score = 0

    score += len(found_skills) * 5

    if "project" in resume_text:
        score += 10

    if "experience" in resume_text:
        score += 15

    if "education" in resume_text:
        score += 10

    if "certification" in resume_text:
        score += 10

    resume_score = min(score, 100)

    # ----------------------------------
    # JOB DESCRIPTION ANALYSIS
    # ----------------------------------

    jd_text = job_description.lower()

    jd_skills = []

    for skill in SKILLS:

        if skill.lower() in jd_text:
            jd_skills.append(skill)

    matched_skills = []
    missing_skills = []

    for skill in jd_skills:

        if skill in found_skills:
            matched_skills.append(skill)

        else:
            missing_skills.append(skill)

    # ----------------------------------
    # MATCH SCORE
    # ----------------------------------

    if len(jd_skills) > 0:

        match_score = int(
            len(matched_skills)
            /
            len(jd_skills)
            * 100
        )

    else:

        match_score = 0

    # ----------------------------------
    # METRICS
    # ----------------------------------

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📊 Resume Score",
            f"{resume_score}/100"
        )

    with col2:
        st.metric(
            "🎯 Job Match",
            f"{match_score}%"
        )

    with col3:
        st.metric(
            "🧠 Skills Found",
            len(found_skills)
        )

    st.divider()

    # ----------------------------------
    # FOUND SKILLS
    # ----------------------------------

    st.subheader("🛠 Skills Found")

    if found_skills:

        for skill in found_skills:
            st.success(skill)

    else:

        st.warning(
            "No skills detected."
        )

    # ----------------------------------
    # MATCHED SKILLS
    # ----------------------------------

    st.subheader("✅ Matched Skills")

    if matched_skills:

        for skill in matched_skills:
            st.success(skill)

    else:

        st.warning(
            "No matched skills."
        )

    # ----------------------------------
    # MISSING SKILLS
    # ----------------------------------

    st.subheader("❌ Missing Skills")

    if missing_skills:

        for skill in missing_skills:
            st.error(skill)

    else:

        st.success(
            "No missing skills."
        )

    st.divider()

    # ----------------------------------
    # PIE CHART
    # ----------------------------------

    chart_data = {
        "Category": [
            "Matched",
            "Missing"
        ],
        "Count": [
            len(matched_skills),
            len(missing_skills)
        ]
    }

    fig = px.pie(
        chart_data,
        values="Count",
        names="Category",
        title="Skill Match Analysis"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.divider()

    # ----------------------------------
    # AI FEEDBACK
    # ----------------------------------

    st.subheader("🤖 AI Resume Review")

    if st.button("Generate AI Feedback"):

        with st.spinner(
            "Analyzing Resume..."
        ):

            feedback = get_ai_feedback(
                text,
                job_description,
                missing_skills
            )

            st.success(
                "Analysis Complete"
            )

            st.write(feedback)

            st.download_button(
                "📥 Download Feedback",
                feedback,
                file_name="resume_feedback.txt"
            )