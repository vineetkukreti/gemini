from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure generative AI with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get response
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# Set page configuration and title
st.set_page_config(page_title="vineetai", page_icon="✨")

# Page header and introduction
st.title("Chimti Application")
st.markdown("Welcome to Chimti, an interactive AI-powered Q&A application!")

# Input field and submit button
input_question = st.text_input("Input your question:", key="input_question")
submit_button = st.button("Ask the question")

# When submit button is clicked
if submit_button:
    # Get response from Gemini Pro model
    response = get_gemini_response(input_question)

    # Display the response with a styled subheader
    st.subheader('The response')
    st.success(response)

# Add a footer for attribution or additional information
st.text("Powered by Gemini Pro AI")

# Optional: Add custom styling to the components for a more visually appealing design
st.markdown(
    """
    <style>
        .css-1j4y4ri {
            background-color: #f0f8ff !important;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
    </style>
    """,
    unsafe_allow_html=True
)
