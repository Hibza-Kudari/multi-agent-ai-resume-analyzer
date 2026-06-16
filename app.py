import streamlit as st
import plotly.express as px

from skills import SKILLS
from ocr_helper import extract_text_from_pdf
from ollama_helper import get_ai_feedback
from agents.interview_agent import interview_agent

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)
st.markdown("""
<style>

.skill-container {
    margin-bottom: 10px;
}

.skill-tag-blue {
    display:inline-block;
    padding:6px 12px;
    margin:4px;
    border-radius:20px;
    background:#1e3a8a;
    color:white;
    font-size:13px;
    font-weight:500;
}

.skill-tag-green {
    display:inline-block;
    padding:6px 12px;
    margin:4px;
    border-radius:20px;
    background:#14532d;
    color:white;
    font-size:13px;
    font-weight:500;
}

.skill-tag-red {
    display:inline-block;
    padding:6px 12px;
    margin:4px;
    border-radius:20px;
    background:#7f1d1d;
    color:white;
    font-size:13px;
    font-weight:500;
}

</style>
""", unsafe_allow_html=True)
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
# SKILLS FOUND
# ----------------------------------

    st.subheader("🧠 Skills Found")

    if found_skills:

        found_html = '<div class="skill-container">'

        for skill in found_skills:
            found_html += (
                f'<span class="skill-tag-blue">{skill}</span>'
            )

        found_html += "</div>"

        st.markdown(
            found_html,
            unsafe_allow_html=True
        )

    else:

        st.warning(
            "No skills detected."
        )

    st.divider()

    # ----------------------------------
    # MATCHED SKILLS
    # ----------------------------------

    st.subheader("✅ Matched Skills")

    if matched_skills:

        matched_html = '<div class="skill-container">'

        for skill in matched_skills:
            matched_html += (
                f'<span class="skill-tag-green">{skill}</span>'
            )

        matched_html += "</div>"

        st.markdown(
            matched_html,
            unsafe_allow_html=True
        )

    else:

        st.warning(
            "No matched skills."
        )

    st.divider()

    # ----------------------------------
    # MISSING SKILLS
    # ----------------------------------

    st.subheader("❌ Missing Skills")

    if missing_skills:

        missing_html = '<div class="skill-container">'

        for skill in missing_skills:
            missing_html += (
                f'<span class="skill-tag-red">{skill}</span>'
            )

        missing_html += "</div>"

        st.markdown(
            missing_html,
            unsafe_allow_html=True
        )

    else:

        st.success(
            "No missing skills."
        )

    st.divider()
    # ----------------------------------
# PIE CHART
# ----------------------------------

    chart_data = {
        "Category": ["Matched", "Missing"],
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
        use_container_width=True
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

            st.divider()

# ----------------------------------
# INTERVIEW PREPARATION
# ----------------------------------

st.subheader("📝 Interview Preparation")

if st.button("Generate Interview Questions"):

    with st.spinner(
        "Generating Interview Questions..."
    ):

        questions = interview_agent(
            text,
            job_description
        )

        st.success(
            "Questions Generated Successfully"
        )

        st.write(questions)

        st.download_button(
            "📥 Download Questions",
            questions,
            file_name="interview_questions.txt"
        )

            