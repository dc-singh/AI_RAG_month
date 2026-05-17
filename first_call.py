from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# if not api_key:
#     raise ValueError("ERROR: GEMINI_API_KEY not found in .env file")
# exit()



client = genai.Client(api_key=api_key) # connect you to google ai

response = client.models.generate_content( # send your question 
    model="gemini-3-flash-preview", #which model to use
    contents="Waht is python in programming language", # your question
    config = types.GenerateContentConfig(
        system_instruction = "Answer me in 1 lines.", # tells AI how to behave
        # max_output_tokens = 500, # Limit response length
        temperature = 0.7 # it tell's the level of AI thinking
    )
)

print("=== Gemini Response ===")
print(response.text) # The AI reply text

print("Input Tokens: ", response.usage_metadata.prompt_token_count)
print("Output Tokens: ", response.usage_metadata.candidates_token_count)
print("Total Tokens: ", response.usage_metadata.total_token_count)




