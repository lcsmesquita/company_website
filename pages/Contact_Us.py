import streamlit as st
from send_email import send_email

st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    topic = st.selectbox(label="What topic do you want to discuss?",
                          options=["Job Inquiries", "Project Proposals", "Other"])
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: {topic} - {user_email}

From: {user_email}
{raw_message}
"""
    submit_button = st.form_submit_button()
    if submit_button:
        send_email(message)
        st.info("Your eamil was sent successfully")