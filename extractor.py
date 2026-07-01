import pathlib
import json

import google.generativeai as genai

from config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Working Model
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config={
        "temperature": 0,
        "response_mime_type": "application/json"
    }
)

PROMPT = """
Extract bank statement information from this PDF.

Return ONLY valid JSON.

JSON Structure:

{
  "Account_Number": "",
  "Account_Name": "",
  "Opening_Balance": 0.00,
  "Closing_Balance": 0.00,
  "Bank_Name": "",
  "Bank_Branch": "",
  "Statement_Genaration_Date": "",
  "Client_Address": ""
}

Rules:
- Return only JSON
- No markdown
- No explanation
- Date format YYYY-MM-DD
- Numeric amounts must be float
- Missing values = null
"""

def extract_bank_statement(pdf_path: str):

    try:

        pdf_file = pathlib.Path(pdf_path)

        # Upload PDF
        uploaded_file = genai.upload_file(pdf_file)

        # Generate response
        response = model.generate_content([
            PROMPT,
            uploaded_file
        ])

        text = response.text.strip()

        data = json.loads(text)

        return {
            "success": True,
            "data": data
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }