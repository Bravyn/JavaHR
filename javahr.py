import streamlit as st
st.logo("logo.jpg")

st.title(":red[Java **House**] :coffee: Recruitment Portal")
st.caption("www.javahouseafrica.com")

st.header("Hi, Welcome to Join the Team:heart: .")
st.text("Let us get to know you ")


with st.form("hr_form", border=False):

    first_name = st.text_input("What is your **first name**")
    second_name = st.text_input("What is your **second name**")
    other_names = st.text_input("Other names (if any)")

    age = st.number_input("How old are you?", min_value=16, max_value=65,
                          placeholder="Make sure the age is within the acceptable range") 
    gender = st.radio("**Gender**", ["Male", "Female", "Rather Not Say"])

    st.divider()
    role = st.radio("**What role are you applying for?**",
                    ["ICT Intern", "Digital Brand Ambassador",
                     "Steward", "Brand Intern","Role not listed above"])
    
    if role == "Role not listed above":
        role2 = st.text_input("Type the role you are applying for here")

  
    outreach = st.radio("**How did you hear about this role**",
                        ["LinkedIn", "Social Media Platforms",
                         "A friend"])
    st.divider()
    cv = st.file_uploader("**Please share  your CV with us**")
    email = st.text_input("What is your **email address**")
    about_self = st.text_area("Tell us something about yourself in less than 200 words")

    salary_expecation = st.number_input("What is your **expected salary**")
    submitted =  st.form_submit_button()

    if submitted:
        st.info("Applied Successfully")




