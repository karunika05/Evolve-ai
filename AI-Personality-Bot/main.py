from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
import uvicorn
from dotenv import load_dotenv
import os


# ---------------------------------------
# 1. CONFIGURE GROQ API
# ---------------------------------------
load_dotenv()  # loads the .env file

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found in .env file!")

client = Groq(api_key=GROQ_API_KEY)
# Choose a Groq model (fast & accurate)
MODEL_NAME = "llama-3.1-8b-instant"  
# others:
# "llama3-70b-8192"
# "mixtral-8x7b-32768"


# ---------------------------------------
# 2. FASTAPI + CORS
# ---------------------------------------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------
# 3. REQUEST BODY
# ---------------------------------------
class ChatRequest(BaseModel):
    message: str
    personality: str = " You are a kind, cheerful kindergarten teacher."


# ---------------------------------------
# 4. CHAT ENDPOINT
# ---------------------------------------
@app.post("/chat")
async def chat(req: ChatRequest):
    print("Incoming request:", req.dict())  # debug: see request data

    system_prompt = """
        

Explain everything like you are talking to a 5-year-old child.
- Use very simple words
- Short sentences
- Fun examples
- Friendly and encouraging tone
- Use emojis like 👶🌈🍎🧸 when appropriate
- Never use technical or complex language
- If a topic is hard, break it into tiny pieces

Your goal is to make learning feel fun, safe, and easy.
    """
    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": req.message}
            ]
        )

        ai_response = completion.choices[0].message.content
        print("AI response:", ai_response)  # debug

        return {"response": ai_response}

    except Exception as e:
        import traceback
        print(traceback.format_exc())  # full error in terminal
        return {"error": str(e)}

# ---------------------------------------
# 5. RUN SERVER
# ---------------------------------------
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)