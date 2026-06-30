# Token Management + Cost Control

## LESSON 1 — What is a Token (Refresher)
```
Token = unit of text AI processes

NOT words. NOT characters. TOKENS.

Examples:
"Hello"            = 1 token
"Hello world"      = 2 tokens
"Python"           = 1 token
"programming"      = 1 token
"ChatGPT"          = 2 tokens (Chat + GPT)
"don't"            = 2 tokens (don + 't)

Rule of thumb:
1 token ≈ 4 characters
1 token ≈ 0.75 words
1,000 tokens ≈ 750 words ≈ 1 page

Common text sizes:
Short message:    50-100 tokens
Email:            200-400 tokens
Long article:     1,000-2,000 tokens
Book chapter:     5,000-10,000 tokens
```

# LESSON 2 — Input vs Output Tokens
```
Every API call has TWO token counts:

INPUT TOKENS:
→ Your system instruction
→ Your prompt/question
→ Conversation history (if chatbot)
→ Charged at LOWER rate

OUTPUT TOKENS:
→ AI's response
→ Charged at HIGHER rate (2-3x more)

Example:
You send:  100 tokens  → costs $0.0001
AI sends:  500 tokens  → costs $0.0015
TOTAL:     600 tokens  → costs $0.0016
```

# LESSON 3 — Gemini Pricing (Free + Paid)

```
GEMINI 2.5 FLASH-LITE (what we use):

FREE TIER:
→ 15 requests per minute
→ 1 million tokens per day
→ FREE for learning
→ Perfect for development

PAID TIER (if you scale):
→ Input:  $0.075 per million tokens
→ Output: $0.30 per million tokens
→ Very cheap compared to OpenAI

Example cost calculation:
1,000 API calls per day
Each call: 200 input + 300 output tokens
= 200,000 input + 300,000 output tokens per day
= $0.015 input + $0.090 output
= $0.105 per day
= $3.15 per month

VERY affordable.
```

# LESSON 4 — Token Control Techniques

```
4 ways to control tokens:

1. max_output_tokens
   → Limits AI response length
   → Already using this in your code

2. Shorter system instructions
   → Don't write essays in system prompt
   → Be concise

3. Trim conversation history
   → For chatbots: only keep last 10 messages
   → Drop older messages

4. Count BEFORE sending
   → Use Gemini's count_tokens method
   → Reject if too expensive
```

# LESSON 5 — Gemini Has Built-In Token Counter

```
Gemini library has a FREE method:
client.models.count_tokens()

It tells you EXACT token count
WITHOUT making the actual API call.

Why this is powerful:
→ Check cost BEFORE you pay for it
→ Block requests that are too big
→ Show users how much their query costs
→ Set hard limits
```

### Pattern 1 — Tokens ≠ Words

```
Words → Tokens ratio:
"Hello"        → 1 word  = 2 tokens (ratio 2.0)
"Hello world"  → 2 words = 3 tokens (ratio 1.5)
"What is..."   → 3 words = 5 tokens (ratio 1.67)
Long sentence  → 21 words = 24 tokens (ratio 1.14)

LESSON:
→ Short text = more tokens per word
→ Long text = less tokens per word
→ Average ratio: ~1.3 tokens per word
```
### Pattern 2 — Tokens ≠ Characters
```
Characters → Tokens ratio:
"Hello"        → 5 chars  / 2 tokens = 2.5 chars per token
"Hello world"  → 11 chars / 3 tokens = 3.7 chars per token
"What is..."   → 15 chars / 5 tokens = 3.0 chars per token
Long sentence  → 119 chars / 24 tokens = 4.95 chars per token

LESSON:
→ Average: 4 characters per token
→ This matches industry standard
→ This is the "magic 4" rule
```
### Pattern 3 — Punctuation Costs Tokens

```
"high-level"       = 3 tokens (because of the dash)
"What is Python?"  = 5 tokens (? adds a token)
"end."             = often 2 tokens

LESSON:
→ Every punctuation mark = potential extra token
→ This is why JSON costs more (lots of {, }, ", :, ,)
```

### How the Tokenizer Actually Works
```
The Gemini Tokenizer:

Step 1: Look at the text
Step 2: Find common words/patterns
Step 3: If word is common → 1 token
        ("the", "is", "a", "Python", "the")
Step 4: If word is rare → split into pieces
        ("decorator" might become "deco" + "rator")
Step 5: Punctuation → separate tokens
Step 6: Add invisible markers (start, end)
Step 7: Return total count

This system is called BPE (Byte Pair Encoding)
Used by OpenAI, Google, Anthropic — all major AIs
```

