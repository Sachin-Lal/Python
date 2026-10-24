# FastOne Chatbot

A simple full-stack chatbot with:
- Python FastAPI backend
- React frontend with an F1-inspired UI
- Gemini API using the key from the .env file as GEMINI_KEY

## Run

Backend:
```bash
python -m uvicorn backend.main:app --reload --port 8000
```

Frontend:
Open the generated index.html directly in a browser, or serve the folder with a simple static server.
