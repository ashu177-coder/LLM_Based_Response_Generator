from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load gemini pro model and get response


def get_gemini_resposne(question):
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    response = chat.send_message(question)
    return response.text


st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input:", key='input')
submit = st.button("Ask your question")

if submit and input:
    response = get_gemini_resposne(input)

    # Add user query and response to session chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is ->")
    # for chunk in response:
    #     st.write(chunk.text)
    #     st.session_state['chat_history'].append(("Bot", chunk.text))
    st.write(response)
    st.session_state['chat_history'].append(("Bot", response))

st.subheader("The Chat history is")

for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")

# conda create -p venv python==3.10 -y
# conda activate /venv
# pip install -r requirements.txt
