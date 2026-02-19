import google.generativeai as genai
import PyPDF2 as pdf
import json
import re

# CONFIGURE GEMINI

def configure_genai(api_key):
    """Configure the Generative AI API with proper error handling."""
    try:
        genai.configure(api_key=api_key)
    except Exception as e:
        raise Exception(f"Failed to configure Generative AI: {str(e)}")



# CALL GEMINI MODEL

def get_gemini_response(prompt):
    """
    Generate content using the NEW correct Gemini model:
    - gemini-1.5-flash (FREE + supported)
    Handles:
        • Empty responses
        • JSON extraction
        • Invalid model errors
        • 404 model errors
    """
    try:
      
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Make request
        response = model.generate_content(prompt)

        # Validate response
        if not response or not hasattr(response, "text") or not response.text:
            raise Exception("Empty response received from Gemini")

        raw_text = response.text.strip()

        

      
        try:
            parsed = json.loads(raw_text)

            # Validate required fields
            for field in ["JD Match", "MissingKeywords", "Profile Summary"]:
                if field not in parsed:
                    raise Exception(f"Missing required field: {field}")

            return raw_text

        except json.JSONDecodeError:
            # Try extracting JSON block manually
            match = re.search(r"\{.*\}", raw_text, re.DOTALL)
            if match:
                return match.group()

            raise Exception("Gemini responded but JSON could not be extracted")

    except Exception as e:
        # Clean error for Flask frontend
        raise Exception(f"Error generating response: {str(e)}")



# PDF TEXT EXTRACTOR

def extract_pdf_text(uploaded_file):
    """Extract text safely from PDF using PyPDF2."""
    try:
        reader = pdf.PdfReader(uploaded_file)

        if len(reader.pages) == 0:
            raise Exception("PDF file is empty")

        text_content = []

        for page in reader.pages:
            text = page.extract_text()
            if text:
                text_content.append(text)

        if not text_content:
            raise Exception("No readable text found in the PDF")

        return " ".join(text_content)

    except Exception as e:
        raise Exception(f"Error extracting PDF text: {str(e)}")



# PROMPT BUILDER

def prepare_prompt(resume_text, job_description):
    """Prepare a structured ATS evaluation prompt."""
    if not resume_text or not job_description:
        raise ValueError("Resume text and job description cannot be empty")

    prompt_template = """
    You are an expert ATS (Applicant Tracking System) evaluator.

    Compare the following resume with the job description and return ONLY JSON output.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Respond strictly in this JSON structure:
    {{
        "JD Match": "percentage between 0-100",
        "MissingKeywords": ["keyword1", "keyword2"],
        "Profile Summary": "A detailed ATS-friendly summary"
    }}
    """

    return prompt_template.format(
        resume_text=resume_text.strip(),
        job_description=job_description.strip()
    )
