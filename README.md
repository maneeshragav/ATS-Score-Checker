ATS Resume Expert

Overview

The ATS Resume Expert is a Streamlit application designed to help users match their resumes with job descriptions using an AI-based evaluation. It leverages Google's Gemini language model to provide insights on the strengths and weaknesses of a candidate's resume in comparison to a given job description, as well as an ATS (Applicant Tracking System) style percentage match. The application provides three key features:

Resume Evaluation: Evaluates the user's resume and highlights its strengths and weaknesses in relation to the job description.
Skills Improvement Suggestions: Offers suggestions on how to improve the user's skills based on the job description.
Percentage Match: Calculates the percentage match between the user's resume and the job description, highlighting keywords that are important.
Features
Job Description Input:

A text area where users can input the job description they want to match their resume against.
Resume Upload:

Users can upload their resume in PDF format.
Key Buttons:

Tell me about the resume: This button triggers an evaluation of the resume, comparing it to the job description, and returns the strengths and weaknesses.
How can I improvise my skills: This button provides feedback on how the user can improve their skills to match the job description better (future enhancement).
Percentage Match: This button calculates the percentage match between the resume and the job description, highlighting important keywords.

How It Works
PDF Resume Upload: The user uploads a PDF version of their resume, which is converted to an image using the pdf2image library.

Job Description Input: The user inputs the job description for the position they are interested in.

Gemini AI Integration: The uploaded resume and job description are passed to the Google Gemini AI model for content generation.

Evaluation: Based on the model's output, the system evaluates the resume's strengths and weaknesses, suggests improvements, or calculates a percentage match.

Environment Variables
GOOGLE_API_KEY: This is the key required to interact with the Google Gemini AI API. Ensure this is stored securely in your .env file.
Future Enhancements
Skills Improvement Suggestions: Implement functionality to provide concrete feedback on how to improve skills based on the job description.
Expanded Resume Parsing: Enhance the system to parse different formats beyond PDF.
Multi-Page PDF Support: Add support for processing multiple pages from a resume.
