from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import google.generativeai as genai
import os

from PIL import Image


genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro-vision')
def call_the_model(input,image):
    if input !="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text



st.header("Gemini Application")
input = st.text_input("Input : ",key = "inputs")
upload_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
image  = ""





if upload_image is not None:
    image = Image.open(upload_image)
    st.image(image, caption='Uploaded image..', use_column_width=True)


submit = st.button("tell me about the uploaded image")

if submit:
    response = call_the_model(input,image)
    st.subheader('The response')
    st.write(response)