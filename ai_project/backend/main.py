import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

app = FastAPI(title='FastOne Chatbot')
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

class ChatRequest(BaseModel):
    message: str


def build_prompt(user_message: str) -> str:
    return (
        "You are FastOne, a witty F1-inspired AI chatbot. "
        "Answer the user’s question directly and in first person. "
        "Mention Sachin as your creator. "
        "Keep the tone energetic and racing-themed, but stay helpful and factual. "
        f"Question: {user_message}"
    )


def get_model():
    key = os.getenv('GEMINI_KEY') or os.getenv('GEMINI_API_KEY')
    if not key:
        raise RuntimeError('Missing GEMINI_KEY or GEMINI_API_KEY in environment')
    genai.configure(api_key=key)
    return genai.GenerativeModel(os.getenv('GEMINI_MODEL', 'models/gemini-flash-latest'))


def generate_reply(model, user_message: str) -> str:
    generation_config = genai.GenerationConfig(
        temperature=0.7,
        max_output_tokens=1024,
        top_p=0.95,
    )
    response = model.generate_content(
        build_prompt(user_message),
        generation_config=generation_config,
    )
    return getattr(response, 'text', str(response))


@app.post('/chat')
def chat(req: ChatRequest):
    try:
        model = get_model()
        reply = generate_reply(model, req.message)
        return {'reply': reply}
    except Exception as exc:
        return {'reply': f'FastOne hit a pit stop: {exc}'}
