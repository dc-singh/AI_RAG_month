from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("AI_API_KEY")

if not api_key:
    print("ERROR: Gemini API key not found in .env file")
    exit()

client = genai.Client(api_key=api_key)

def token_counter(text:str):
    response = client.models.count_tokens(
        model="gemini-2.5-flash-lite",
        contents=text
    )

    return response.total_tokens

# test_texts = [
#     "Hello",
#     "Hello world",
#     "What is Python?",
#     "Python is a high-level programming language",
#     "The quick brown fox jumps over the lazy dog. This sentence contains every letter of the English alphabet at least once.",
# ]

# test_texts = [
#     "Plain English text here",
#     "{'name': 'John', 'age': 30}",  # JSON
#     "def hello(): return 'world'",  # Code
#     "🚀💻🎉",  # Emojis
#     "あいうえお",  # Japanese
# ]

# for text in test_texts:
#     tokens = token_counter(text)
#     char = len(text)
#     word = len(text.split())

#     print(f"\nText: '{text}'")
#     print(f"  Characters: {char}")
#     print(f"  Words: {word}")
#     print(f"  Tokens: {tokens}")


# ===========================================
# FUNCTION 2 - CALCULATE COST
# ===========================================

# Gemini 2.5 Flash-Lite pricing (per million tokens)
INPUT_COST_PER_MILLION = 0.075   # $0.075 per 1M input tokens
OUTPUT_COST_PER_MILLION = 0.30   # $0.30 per 1M output tokens


def calculate_cost(input_tokens: int, output_tokens: int) -> dict:
    """
    Calculate cost for an API call.
    
    Args:
        input_tokens: Tokens in your prompt
        output_tokens: Tokens in AI response
    
    Returns:
        Dictionary with cost breakdown
    """
    
    # Calculate costs (convert from per-million to per-token)
    input_cost = (input_tokens / 1_000_000) * INPUT_COST_PER_MILLION
    output_cost = (output_tokens / 1_000_000) * OUTPUT_COST_PER_MILLION
    total_cost = input_cost + output_cost
    
    return {
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": input_tokens + output_tokens,
        "input_cost_usd": round(input_cost, 8),
        "output_cost_usd": round(output_cost, 8),
        "total_cost_usd": round(total_cost, 8),
        "cost_in_cents": round(total_cost * 100, 6),
    }


# ===========================================
# TEST THE CALCULATOR
# ===========================================

print("\n" + "="*50)
print("COST CALCULATOR TEST")
print("="*50)

# Test scenarios
scenarios = [
    {"name": "Small chat", "input": 50, "output": 100},
    {"name": "Medium response", "input": 200, "output": 500},
    {"name": "Long article", "input": 500, "output": 2000},
    {"name": "Heavy request", "input": 1000, "output": 5000},
]

for s in scenarios:
    cost = calculate_cost(s["input"], s["output"])
    
    print(f"\n--- {s['name']} ---")
    print(f"Input tokens:  {cost['input_tokens']}")
    print(f"Output tokens: {cost['output_tokens']}")
    print(f"Total tokens:  {cost['total_tokens']}")
    print(f"Cost (USD):    ${cost['total_cost_usd']}")
    print(f"Cost (cents):  {cost['cost_in_cents']}¢")