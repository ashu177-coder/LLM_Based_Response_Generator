# conda create -p venv python == 3.10 -y
# Create requirements.txt
# pip install -r requirement.txt
# Create the .env file and include the API key.

import google.generativeai as genai
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # Loading all the environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_resposne(question):
    # Function to load gemini-pro model and get responses
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text


# initializing the streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
input = st.text_input("Input: ", key="input")
submit = st.button("Ask the Question")

# When submit is clicked
if submit:
    response = get_gemini_resposne(input)
    st.write(response)
