from dotenv import load_dotenv
# dotenv is for loading all the environment

load_dotenv() ## loading all the environment variable

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


## fuction to load gemini pro model and get response

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Application")
input = st.text_input("Input : ",key = "inputs")
submit = st.button("Ask the question")

## when submit is clicked 
if submit:
    response = get_gemini_response(input)
    st.subheader('The response')
    st.write(response)