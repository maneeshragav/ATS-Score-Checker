from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import io
import base64
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def get_gemini_response(input,pdf_content,prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input,pdf_content[0],prompt])
    return response.text
def input_pdf_setup(upload_file):
    if upload_file is not None:
        ## convert the PDF to image
        image = pdf2image.convert_from_bytes(uploaded_file.read())

        first_page = image[0]

        ##convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format = 'JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode() #encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
##Streamlit App

st.set_page_config(page_title = "ATS Resume Expert")
st.header("ATS Tracking System")
input_text = st.text_area("Job Description: ",key = "input")
uploaded_file = st.file_uploader("Upload your resume(PDF)...",type = ["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell me about the resume")

submit3 = st.button("Percentage match")

input_prompt1 = """
You are an experienced technical Human Resource Manager,
your task is to review the provided resume against the Job Description
Please share your professional evaluation on whether the candidate's profile aligns with the role
Highlight the strengths and weaknesses of the applicant in relation to the specified job description"""

input_prompt3 = """
Ypu are an experienced ATS scanner with deep technical understanding of the required skills
your task is to evaluate the resume against the provided job description.
Give me the percentage of the candidates resume matching withe job description.
first the output should be in percentage and then keywords"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Response is: ")
        st.write(response)
    else:
        st.write("Please upload the resume")
elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Response is: ")
        st.write(response)
    else:
        st.write("Please upload the resume")
