from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure generative AI with the Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get response
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# Set Streamlit page configuration
st.set_page_config(
    page_title="VineetAI",
    page_icon="🌌",
    layout="wide",
      bg_color="#FF0000"
)

# Custom styling for background color
background_color = "#FF2400"  # Scarlet Red
text_color = "#FFFFFF"  # White

# Apply custom styling
custom_style = f"""
    <style>
        body {{
            background-color: {background_color};
            color: {text_color};
        }}
    </style>
"""

st.markdown(custom_style, unsafe_allow_html=True)

# Streamlit header and input field
st.header("Chimti Application")
input_text = st.text_input("Input your question:", key="input_question")
submit_button = st.button("Ask the question")

# When submit button is clicked
if submit_button:
    if input_text:
        # Get Gemini Pro model response
        response = get_gemini_response(input_text)

        # Display the response
        st.subheader('The response')
        st.write(response)
    else:
        # Display a warning if the input is empty
        st.warning("Please enter a question before submitting.")
