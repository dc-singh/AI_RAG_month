from google import genai
import os
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("AI_API_KEY")

if not api_key:
    print("Error: Gemini api key is not found in .env file")
    exit()

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
        model = "gemini-2.5-flash", 
        contents ="Why should I learn backend development?",  
        config = types.GenerateContentConfig(
            system_instruction = "You are a helpful assistant. Answer in one sentence only maximum 100 words",
            # max_output_tokens = 100,
            temperature = 0.7
        )
)

print("===== Gemini Response =====")
print(response.text)
print("\n=== TOKEN USAGE ===")
print("Input tokens: ", response.usage_metadata.prompt_token_count)
print("Output tokens:", response.usage_metadata.candidates_token_count)
print("Total tokens: ", response.usage_metadata.total_token_count)
