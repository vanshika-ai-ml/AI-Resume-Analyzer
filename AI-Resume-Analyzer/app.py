import streamlit as st
from parser import extract_text_from_pdf
from prompts import create_resume_prompt
from utils import analyze_resume


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: #f8fafc;
    }

    /* Header */
    .hero {
        background: linear-gradient(135deg, #1e3a8a, #2563eb);
        padding: 35px 40px;
        border-radius: 18px;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 8px 25px rgba(37, 99, 235, 0.18);
    }

    .hero h1 {
        font-size: 38px;
        margin-bottom: 8px;
        font-weight: 700;
    }

    .hero p {
        font-size: 17px;
        opacity: 0.92;
        margin: 0;
    }

    /* Section cards */
    .section-card {
        background: white;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 15px rgba(15, 23, 42, 0.05);
        height: 100%;
    }

    .section-title {
        font-size: 21px;
        font-weight: 650;
        color: #1e293b;
        margin-bottom: 6px;
    }

    .section-subtitle {
        color: #64748b;
        font-size: 14px;
        margin-bottom: 18px;
    }

    /* Button */
    div.stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #2563eb, #1d4ed8);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 13px 20px;
        font-size: 16px;
        font-weight: 600;
        transition: 0.2s;
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #1d4ed8, #1e40af);
        transform: translateY(-1px);
    }

    /* Result area */
    .result-header {
        background: white;
        padding: 20px 24px;
        border-radius: 14px;
        border: 1px solid #e2e8f0;
        margin-top: 30px;
        margin-bottom: 15px;
    }

    /* Hide Streamlit branding */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

</style>
""", unsafe_allow_html=True)


# ---------------- HERO ----------------
st.markdown("""
<div class="hero">
    <h1>📄 AI Resume Analyzer</h1>
    <p>
        Analyze your resume against a job description and get
        AI-powered insights, skill gaps, and improvement suggestions.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------- INPUT SECTION ----------------
col1, col2 = st.columns(2, gap="large")


# Resume upload
with col1:
    st.markdown("""
    <div class="section-card">
        <div class="section-title">📄 Upload Resume</div>
        <div class="section-subtitle">
            Upload your resume in PDF format.
        </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Choose your Resume",
        type=["pdf"],
        label_visibility="collapsed"
    )

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- EXTRACTED RESUME TEXT ----------------
if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)

    st.markdown("### 📄 Extracted Resume Text")
    st.text_area(
        "Resume Text",
        resume_text,
        height=250,
        label_visibility="collapsed"
    )



# Job description
with col2:
    st.markdown("""
    <div class="section-card">
        <div class="section-title">💼 Job Description</div>
        <div class="section-subtitle">
            Paste the job description you want to match against.
        </div>
    """, unsafe_allow_html=True)

    job_description = st.text_area(
        "Job Description",
        placeholder="Paste the Job Description here...",
        height=180,
        label_visibility="collapsed"
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ---------------- ANALYZE BUTTON ----------------
st.write("")

if st.button("✨ Analyze My Resume"):

    if uploaded_file is None:
        st.warning("Please upload your resume first.")

    elif job_description.strip() == "":
        st.warning("Please enter the Job Description.")

    else:

        st.success("Everything looks good! Starting AI analysis...")

        # AI analysis
        with st.spinner("Analyzing your resume..."):

            prompt = create_resume_prompt(
                resume_text,
                job_description
            )

            result = analyze_resume(prompt)

        # Result header
        st.markdown("""
        <div class="result-header">
            <div class="section-title">🤖 AI Resume Analysis</div>
            <div class="section-subtitle">
                Here's how your resume matches the selected job description.
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Display result
        st.markdown(result)
