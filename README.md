# Gemini PDF Bank Statement Extractor

## Author

**Bishwaprotap Ray**

- **Role:** Software Developer Intern | AI & Machine Learning Engineer
- **Education:** B.Sc. in Computer Science & Engineering (International University of Business Agriculture and Technology)
- **Specialization:** AI, Machine Learning, LLM, FastAPI, Voice Assistant Development
- **Location:** Dhaka, Bangladesh
- **Email:** baburay214@gmail.com
- **LinkedIn:** [https://www.linkedin.com/in/bishwaprotap-ray/](https://www.linkedin.com/in/bishwaprotap-ray/)
- **GitHub:** [https://github.com/Bishwaprotapi](https://github.com/Bishwaprotapi)

---

## Python Version

Python 3.11

---

# Install

```bash
pip install -r requirements.txt
```

---

# Add Gemini API Key

Create `.env`

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

# Run Project

```bash
uvicorn app:app --reload
```

---

# Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoint

POST

```text
/extract
```

Form Data:

```text
file = statement.pdf
```

---

# Example Response

```json
{
  "success": true,
  "data": {
    "Account_Number": "1820901036156",
    "Account_Name": "MAGNUM STEEL INDUSTRIES LIMITED",
    "Opening_Balance": -192097192.00,
    "Closing_Balance": 0.00,
    "Bank_Name": "PUBALI BANK PLC.",
    "Bank_Branch": "FARMGATE BRANCH",
    "Statement_Genaration_Date": "2026-05-03",
    "Client_Address": "AKIJ HOUSE-198 BIR UTTOM MIR SHOWKATSARAK, GULSHAN LINK ROAD, TEJGAON DHAKA"
  }
}
```