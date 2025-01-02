# Job Search Platform

## Overview
The Job Search Platform is a lightweight, AI-powered application built using **Streamlit** that simplifies job hunting by analyzing uploaded resumes and displaying relevant job postings from multiple sources. This project fetches job data directly using web scraping and text processing scripts.

## Features
- **Resume Upload**: Users can upload their resumes in PDF format.
- **Resume Parsing**: Extracts key information such as skills, education, and experience using NLP techniques.
- **Job Matching**: Fetches job postings from popular platforms (e.g., Indeed, Naukri) based on the user's profile.
- **Job Listings Display**: Displays relevant job postings in a user-friendly Streamlit interface.

## Tech Stack
- **Frontend**: Streamlit
- **Job Data Scraping**: Python scripts (e.g., `scrap.py`)
- **File Processing**: Python script for PDF parsing (e.g., `pdf.py`)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/snehaapratap/Job-Search.git
   cd Job-Search
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
4. Ensure any necessary API keys or credentials are configured in a `.env` file or directly in the scripts.

## Usage
1. Open the Streamlit app in your browser.
2. Upload your resume in PDF format.
3. Wait for the system to analyze your resume.
4. View tailored job postings scraped from various job boards.

## Project Structure
```
job-search-platform/
│
├── .venv/                     # Virtual environment files
├── .gitattributes             # Git attributes
├── .gitignore                 # Ignored files
├── app.py                     # Main Streamlit application
├── pdf.py                     # Script for processing PDF resumes
├── scrap.py                   # Script for scraping job postings
├── foundit_job_cards.txt      # Sample job data from Foundit
├── indeed_job_cards.txt       # Sample job data from Indeed
├── naukri_job_cards.txt       # Sample job data from Naukri
├── jooble_job_cards.txt       # Sample job data from Jooble
├── job_analysis_results.txt   # Processed analysis results
```
## Screenshots
![image](https://github.com/user-attachments/assets/03f3663e-c234-432e-99d4-2a2f68dba966)

![image](https://github.com/user-attachments/assets/03ba08db-240f-4357-a2e2-20fe30dc8226)

![image](https://github.com/user-attachments/assets/f72be01a-3eef-4d4e-8403-f381bb97cf7a)

![image](https://github.com/user-attachments/assets/1b188887-8c41-4065-b707-9b81ca79c931)

![image](https://github.com/user-attachments/assets/f57c3b4c-0213-4f56-823f-da7d0bbb66dd)



## Future Enhancements
- Add user authentication and session management.
- Integrate more job boards for a wider range of postings.
- Enhance the NLP model for better resume parsing and job matching.
- Add a database to store user preferences and session data.
