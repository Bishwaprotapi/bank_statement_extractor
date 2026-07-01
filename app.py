import os
import uuid
import shutil

from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File

from fastapi.responses import JSONResponse

from extractor import extract_bank_statement

# FastAPI App
app = FastAPI(
    title="Gemini Bank Statement Extractor",
    version="1 .0.0"
)

# Upload folder
UPLOAD_FOLDER = "uploads"

# Create upload folder
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():

    return {
        "success": True,
        "message": "Gemini PDF Extractor Running"
    }

@app.post("/extract")
async def extract_pdf(
    file: UploadFile = File(...)
):

    try:

        # Validate PDF
        if not file.filename.lower().endswith(".pdf"):

            return JSONResponse(
                status_code=400,
                content={
                    "success": False,
                    "message": "Only PDF files allowed"
                }
            )

        # Unique filename
        filename = f"{uuid.uuid4()}.pdf"

        # Full path
        file_path = os.path.join(
            UPLOAD_FOLDER,
            filename
        )

        # Save uploaded PDF
        with open(file_path, "wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        # Extract data
        result = extract_bank_statement(
            file_path
        )

        return JSONResponse(
            content=result
        )

    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": str(e)
            }
        )