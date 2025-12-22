from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY").strip()

# Initialize client
client = Groq(api_key=api_key)

# Test a simple chat completion
try:
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": "Hello"}]
    )
    print("AI response:", completion.choices[0].message.content)

except Exception as e:
    print("Error:", e)
