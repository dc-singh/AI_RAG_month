from google import genai
from dotenv import load_dotenv
import os
from google.genai import types

load_dotenv()

api_key = os.getenv("AI_API_KEY")

if not api_key:
    print("ERROR: Gemini API key not found in .env file")
    exit()

client = genai.Client(api_key=api_key)


def ask(question:str, temperature:float=0.5, max_tokens:int=300, system="You are a helpful assistant."):
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=question,
        config=types.GenerateContentConfig(
            temperature=temperature,
            system_instruction=system,
            max_output_tokens=max_tokens
        )
    )
    return response.text

# print("Setup complete. Ready to test prompts.")

# ==========================================
# PATTERN 1 - ROLE ASSIGNMENT
# ==========================================

# print("\n" + "="*50)
# print("PATTERN 1: ROLE ASSIGNMENT")
# print("="*50)

# # Same question. 3 different roles.
# question = "What is a decorator in Python?"


# # Role 1 - Expert Developer
# print("\n--- ROLE: Expert Developer ---")
# answer1 = ask(
#     question=question,
#     system="""You are a senior Python developer with 10 years experience.
#     Explain concepts clearly with short code examples.
#     Always show a practical example after explaining."""
# )
# print(answer1)


# # Role 2 - Teacher for Beginners
# print("\n--- ROLE: Teacher for Beginners ---")
# answer2 = ask(
#     question=question,
#     system="""You are a Python teacher for absolute beginners.
#     Use very simple words. No technical jargon.
#     Use real-world analogies."""
# )
# print(answer2)


# # Role 3 - Interview Coach
# print("\n--- ROLE: Interview Coach ---")
# answer3 = ask(
#     question=question,
#     system="""You are a technical interview coach.
#     Give answers that would impress an interviewer.
#     Keep it concise and professional.
#     Maximum 3 sentences."""
# )
# print(answer3)


# ==========================================
# PATTERN 2 - OUTPUT FORMAT CONTROL
# ==========================================

# print("\n" + "="*50)
# print("PATTERN 2: OUTPUT FORMAT CONTROL")
# print("="*50)

# # Same topic. 4 different formats.
# topic = "benefits of using FastAPI"


# # Format 1 - Bullet points
# print("\n--- FORMAT: Bullet Points ---")
# print(ask(
#     question=f"Tell me about {topic}",
#     system="""Answer ONLY in bullet points.
#     Use • symbol for each point.
#     Maximum 5 points.
#     Each point maximum 10 words."""
# ))


# # Format 2 - Numbered list
# print("\n--- FORMAT: Numbered List ---")
# print(ask(
#     question=f"Tell me about {topic}",
#     system="""Answer in a numbered list only.
#     Format: 1. point one  2. point two  etc.
#     Maximum 4 points."""
# ))


# # Format 3 - One sentence only
# print("\n--- FORMAT: One Sentence ---")
# print(ask(
#     question=f"Tell me about {topic}",
#     system="""Answer in exactly ONE sentence only.
#     Maximum 20 words.
#     No bullet points. No lists."""
# ))


# # Format 4 - Beginner and Advanced sections
# print("\n--- FORMAT: Beginner + Advanced ---")
# print(ask(
#     question=f"Tell me about {topic}",
#     system="""Structure your answer like this:
    
#     BEGINNER VERSION:
#     (explain in simple words, 2 sentences)
    
#     ADVANCED VERSION:
#     (explain technically, 2 sentences)"""
# ))

# ==========================================
# PATTERN 3 - FEW-SHOT PROMPTING
# ==========================================

# print("\n" + "="*50)
# print("PATTERN 3: FEW-SHOT PROMPTING")
# print("="*50)


# # Example 1 - Informal to Formal Converter
# print("\n--- FEW-SHOT: Informal to Formal ---")
# print(ask(
#     question="""Convert this informal phrase to formal English.

# Here are examples to learn from:

# Informal: gonna
# Formal: going to

# Informal: wanna
# Formal: want to

# Informal: kinda
# Formal: kind of

# Now convert this:
# Informal: gotta finish my work
# Formal:""",
#     system="You are a formal English writing assistant. Reply with only the formal version.",
#     temperature=0.1
# ))


# # Example 2 - Sentiment Detection
# print("\n--- FEW-SHOT: Sentiment Detection ---")
# print(ask(
#     question="""Detect the sentiment of the text.

# Learn from these examples:

# Text: "I love this product! Best purchase ever!"
# Sentiment: POSITIVE

# Text: "This is terrible quality. Total waste."
# Sentiment: NEGATIVE

# Text: "The package arrived on time."
# Sentiment: NEUTRAL

# Now detect this:
# Text: "The food was okay but the service was rude"
# Sentiment:""",
#     system="You are a sentiment analyzer. Reply with ONLY the sentiment word: POSITIVE, NEGATIVE, or NEUTRAL.",
#     temperature=0
# ))


# # Example 3 - Variable Naming Converter
# print("\n--- FEW-SHOT: camelCase to snake_case ---")
# print(ask(
#     question="""Convert camelCase to Python snake_case.

# Examples:

# firstName → first_name
# getUserData → get_user_data
# totalPrice → total_price

# Now convert these (one per line):
# customerEmail
# sendEmailNotification
# maxRetryCount""",
#     system="You are a Python naming expert. Show only the converted names.",
#     temperature=0
# ))

# ==========================================
# PATTERN 4 - CHAIN OF THOUGHT
# ==========================================

# print("\n" + "="*50)
# print("PATTERN 4: CHAIN OF THOUGHT")
# print("="*50)


# # Example 1 - Debug a buggy code
# print("\n--- CHAIN OF THOUGHT: Debug Code ---")
# print(ask(
#     question="""This Python code has a bug. Find and fix it.

# Code:
# def calculate_average(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total / len(numbers)

# numbers = []
# print(calculate_average(numbers))

# Error received: ZeroDivisionError: division by zero
# """,
#     system="""You are a Python debugging expert.
#     Think through this step by step:
    
#     Step 1: What does the code do?
#     Step 2: Where does the error happen?
#     Step 3: Why does the error happen?
#     Step 4: Show the fixed code.
    
#     Use clear step-by-step format.""",
#     temperature=0.1,
#     max_tokens=600
# ))


# # Example 2 - Tech decision making
# print("\n--- CHAIN OF THOUGHT: Tech Decision ---")
# print(ask(
#     question="""I want to build a simple todo list app for personal use.
#     Should I use SQLite or PostgreSQL?""",
#     system="""You are a software architect.
#     Think through this decision step by step:
    
#     Step 1: Understand the use case
#     Step 2: List pros of SQLite for this case
#     Step 3: List pros of PostgreSQL for this case
#     Step 4: Give final recommendation with one sentence reason
    
#     Be concise. No long explanations.""",
#     temperature=0.3,
#     max_tokens=500
# ))


# ==========================================
# JSON OUTPUT - MOST IMPORTANT SKILL
# ==========================================

import json

print("\n" + "="*50)
print("JSON OUTPUT - Contact Extractor")
print("="*50)


def extract_contact(text: str) -> dict:
    """Extract contact info from text. Returns Python dict."""
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        Extract contact information from this text.
        
        Return ONLY this JSON format. Nothing else:
        {{
            "name": "full name or null",
            "email": "email or null",
            "phone": "phone number or null",
            "company": "company name or null"
        }}
        
        Text: {text}
        """,
        config=types.GenerateContentConfig(
            system_instruction="""You are a data extractor.
            Return ONLY valid JSON.
            No explanation. No markdown. No code blocks.
            Just the raw JSON object.""",
            temperature=0
        )
    )
    
    # Get raw response
    raw = response.text.strip()
    
    # Clean markdown code blocks if AI adds them
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    raw = raw.strip()
    
    # Parse JSON safely
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"error": "Could not parse JSON", "raw": raw}


# Test with 4 different samples
test_samples = [
    "Hi I am John Smith, reach me at john@gmail.com",
    "Call Sara Khan at 9876543210 from TechCorp",
    "No contact info in this message at all",
    "CEO Mike (mike@startup.com, +1-800-123-4567) from StartupX"
]

for i, sample in enumerate(test_samples, 1):
    print(f"\n--- Test {i} ---")
    print(f"INPUT:  {sample}")
    result = extract_contact(sample)
    print(f"OUTPUT: {json.dumps(result, indent=2)}")