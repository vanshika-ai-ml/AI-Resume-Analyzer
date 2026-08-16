from datetime import date
def create_resume_prompt(resume_text, job_description):
    current_date = date.today().strftime("%d %B %Y")

    return f"""
You are an expert AI Resume Analyzer.

Analyze the candidate's resume against the given job description.

CURRENT DATE:
Today is {current_date}.

DATE ANALYSIS RULES:
- Treat dates before today as past.
- Treat dates after today as future.
- Do not describe a past date as a future date.
- Do not flag an old date merely because it is in the past.
- Only flag a date as incorrect or a typo when there is clear evidence from the resume or job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Provide the analysis in the following format:

1. Match Score:
Give a score out of 100.

2. Matching Skills:
List the skills from the resume that match the job description.

3. Missing Skills:
List important skills required by the job description that are missing from the resume.

4. Strengths:
Mention the strongest parts of the candidate's resume for this job.

IMPORTANT DATE RULE:
Do not flag a resume date as a "future date" or "date typo" unless it is clearly inconsistent with the current date or with the information in the resume/JD.
Do not assume a date is a typo simply because it is old, recent, or different from the current year.
Only mention a date issue when there is strong evidence that the date is incorrect.

5. Improvement Suggestions:
Give specific and practical suggestions to improve the resume for this job.

6. Overall Feedback:
Give a short overall assessment of how suitable the candidate is for this role.

Keep the response clear, professional, and easy to understand.
"""