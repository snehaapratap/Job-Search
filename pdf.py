import os
import PyPDF2
from groq import Groq
import streamlit as st

# API Key for Groq
GROQ_API_KEY = "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"  

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.
    """
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def analyze_resume_with_llama(text):
    """
    Analyze the extracted text using the Groq API.
    """
    client = Groq(api_key=GROQ_API_KEY)

    prompt = f"""
    Analyze the following resume text and identify key domains related to the skills, projects, internships, and interests mentioned.
    Limit the identified domains to 6 critically most important ones. Provide only the domain names without any numbers, descriptions, or attached explanations.

    Resume Text: {text}
    """
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=512,
        top_p=1,
        stream=True,
        stop=None,
    )

    analysis_result = ""
    for chunk in completion:
        chunk_content = chunk.choices[0].delta.content or ""
        analysis_result += chunk_content

    return analysis_result


#     return domains
def extract_domains_from_pdf(pdf_path):
    """
    Function to analyze PDF and extract important domains.
    """
    if not os.path.exists(pdf_path):
        st.error("The specified PDF file does not exist.")
        return [] 
    
    resume_text = extract_text_from_pdf(pdf_path)
    analysis = analyze_resume_with_llama(resume_text)
    domains = extract_and_limit_domains(analysis, max_domains=15)
    return domains

def extract_and_limit_domains(analysis_result, max_domains=15):
    """
    Extract important domains from the analysis result and limit to a maximum count.
    """
    domains = []
    lines = analysis_result.split("\n")

    for line in lines:
        domain = line.strip()  
        if domain and len(domain.split()) <= 5:  
            domains.append(domain)

    return domains[:max_domains]

def load_job_listings_from_file(file_path="job_listings.txt"):
    """
    Load job listings from a text file.
    """
    with open(file_path, 'r') as file:
        return file.read()

def analyze_resume_with_job_listings(resume_text, job_listings_text):
    """
    Analyze the resume and job listings using the Groq API.
    """
    client = Groq(api_key=GROQ_API_KEY)

    prompt = f"""
    You are an AI job analysis assistant. Below is a resume and a list of job listings.
    Your tasks are:
    1. For each job listing, analyze the skills required based on the job description.
    2. Compare the required skills with the resume.
    3. For each job listing, identify:
        - Strengths: The skills the user possesses that match the job requirements.
        - Areas of Improvement: The skills the user lacks based on the job requirements.
    4. Categorize each job into:
        - Must Apply
        - Good Fit
        - Neutral
        - Doesn't Align
    5. Provide the output in a beautified, structured format, clearly listing:
        - Domain
        - Job Title
        - Company
        - Category
        - Strengths
        - Areas of Improvement
        - Reason for Categorization
    6. Make sure all the job listings are covered.

    Resume:
    {resume_text}

    Job Listings:
    {job_listings_text}
    """
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=2048,
        top_p=1,
        stream=True,
        stop=None,
    )

    analysis_result = ""
    for chunk in completion:
        chunk_content = chunk.choices[0].delta.content or ""
        analysis_result += chunk_content

    # Save the result to a text file
    output_file = "job_analysis_results.txt"
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(analysis_result)


def display_jobs_by_category(content):
    """
    Displays job analysis results in a structured format using Streamlit.
    
    Args:
        content (str): The content of the job analysis results
    """
    try:
        current_category = None
        
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if not line:
                continue

            if line.startswith("**") and line.endswith("**"):
                current_category = line.replace("**", "").strip()
                st.header(current_category)

            elif line[0].isdigit() and line[1] == ".":
                job_title = line.split('. ', 1)[1].strip()
                st.subheader(job_title)

            elif line.startswith('* '):
                parts = line.replace('* ', '').split(': ', 1)
                if len(parts) == 2:
                    key, value = parts
                    st.markdown(f"**{key}:** {value}")

            elif line.startswith('---'):
                st.markdown("---")

    except Exception as e:
        st.error(f"Error parsing job listings: {str(e)}")
        st.text("Content that caused error:")
        st.code(content)