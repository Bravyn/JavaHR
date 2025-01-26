import os
import streamlit as st
import openai
from dotenv import load_dotenv
from PyPDF2 import PdfReader

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OpenAI API key not found. Ensure it's set in the .env file.")


st.logo("logo.jpg")

st.title(":red[Java **House**] :coffee: Recruitment Portal")
st.caption("www.javahouseafrica.com")

st.header("Hi, Welcome to Join the Team:heart: .")
st.text("Let us get to know you ")

# Form for user input
with st.form("hr_form", clear_on_submit=False):
    first_name = st.text_input("What is your **first name**")
    second_name = st.text_input("What is your **second name**")
    other_names = st.text_input("Other names (if any)")

    age = st.number_input("How old are you?", min_value=16, max_value=65,
                          placeholder="Make sure the age is within the acceptable range") 
    gender = st.radio("**Gender**", ["Male", "Female", "Rather Not Say"])

    st.divider()
    role = st.radio("**What role are you applying for?**",
                    ["ICT Intern", "Digital Brand Ambassador",
                     "Steward", "Brand Intern", "Role not listed above"])
    
    if role == "Role not listed above":
        role = st.text_input("Type the role you are applying for here")

    outreach = st.radio("**How did you hear about this role**",
                        ["LinkedIn", "Social Media Platforms",
                         "A friend"])
    st.divider()
    cv = st.file_uploader("**Please share your CV with us (PDF only)**", type=["pdf"])
    email = st.text_input("What is your **email address**")
    about_self = st.text_area("Tell us something about yourself in less than 200 words")

    salary_expectation = st.number_input("What is your **expected salary**")
    submitted = st.form_submit_button("Submit Application")

    if submitted:
        if cv is not None:
            try:
                # Extract and summarize CV content
                reader = PdfReader(cv)
                cv_text = ""
                for page in reader.pages[:5]:  # Limit to first 5 pages
                    cv_text += page.extract_text()

                # Summarize CV content to reduce size
                summary_prompt = f"Summarize the following CV text to reduce length for compatibility analysis:\n{cv_text}"
                cv_summary_response = openai.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant summarizing CVs."},
                        {"role": "user", "content": summary_prompt}
                    ],
                    temperature=0.5,
                    max_tokens=500  # Limit tokens for the summary
                )
                cv_summary = cv_summary_response.choices[0].message.content

                # Prepare user data for compatibility analysis
                user_data = {
                    "first_name": first_name,
                    "second_name": second_name,
                    "other_names": other_names,
                    "age": age,
                    "gender": gender,
                    "role": role,
                    "outreach": outreach,
                    "email": email,
                    "about_self": about_self,
                    "salary_expectation": salary_expectation,
                }

                # Combine user data and summarized CV
                messages = [
                    {"role": "system", "content": "You are a recruitment assistant helping to analyze job applicants."},
                    {"role": "user", "content": f"""
Analyze the following job applicant data and their summarized CV. Provide a compatibility summary highlighting
strengths, weaknesses, and suitability for the applied role.

Applicant Data:
{user_data}

Summarized CV Content:
{cv_summary}

Provide a summarized compatibility report.
"""}
                ]

                # Generate compatibility report
                response = openai.chat.completions.create(
                    model="gpt-4",
                    messages=messages,
                    temperature=0.7
                )
                report = response.choices[0].message.content

                # Display the compatibility report
                st.subheader("Compatibility Summary Report")
                st.write(report)

            except Exception as e:
                st.error(f"Error generating compatibility report: {e}")
        else:
            st.warning("Please upload your CV to proceed.")

            st.warning("Please upload your CV to proceed.")
