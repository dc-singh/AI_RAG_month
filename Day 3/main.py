from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
import json


load_dotenv()

api_key = os.getenv("AI_API_KEY")

if not api_key:
    print("ERROR: Gemini API key not found in .env file")
    exit()

client = genai.Client(api_key=api_key)

def resume_parser(resume_text: str) -> dict:
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=f"""
        Return ONLY this JSON format. Nothing else:
        {{
            "name": "full name or null",
            "email": "email or null",
            "phone": "phone or null",
            "experience_years": "number or null",
            "current_company": "company name or null",
            "current_role": "job title or null",
            "skills": ["list", "of", "skills"],
            "education": "education details or null"
        }}
        
        Resume: {resume_text}""",
        config=types.GenerateContentConfig(
            system_instruction="""You are an expert resume parser.
            Extract information accurately.
            Return ONLY valid JSON.
            No explanation. No markdown blocks.
            If information is missing, use null.
            For skills, always return as a list array.""",
            temperature=0
        )
    )

    raw = response.text.strip()

    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]

    raw = raw.strip()

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {
            "error": "Failed to parse resume",
            "raw_response": raw
        }


resume_1 = """
John Doe
Email: john.doe@gmail.com
Phone: +1-555-123-4567

Currently working at Google as Senior Software Engineer.
Total experience: 7 years.

Technical Skills:
Python, JavaScript, React, FastAPI, PostgreSQL, AWS, Docker, Kubernetes

Education:
B.Tech in Computer Science from MIT (2017)
"""

print("\n--- TEST 1: Complete Resume ---")
print("INPUT:")
print(resume_1)
result_1 = resume_parser(resume_1)
print("OUTPUT:")
print(json.dumps(result_1, indent=2))


