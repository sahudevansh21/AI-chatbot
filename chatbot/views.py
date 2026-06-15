from django.shortcuts import render
from django.http import JsonResponse
from google import genai
from google.genai import types
import os

# Load API key: check environment variable first (Vercel), then .env file (local)
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

# Fallback: read from .env file for local development
if not GEMINI_API_KEY:
    env_path = BASE_DIR / '.env'
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line.startswith('GEMINI_API_KEY='):
                    GEMINI_API_KEY = line.split('=', 1)[1]

if not GEMINI_API_KEY:
    raise Exception("GEMINI_API_KEY not found in environment variables or .env file")

# Configure Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

SYSTEM_INSTRUCTION = (
    "You are a helpful, friendly AI assistant embedded in a web chatbot. "
    "Keep your responses concise (2-4 sentences max unless the user asks for detail). "
    "Be warm, professional, and informative. "
    "Use plain text — no markdown formatting, no bullet points, no headers. "
    "If you don't know something, say so honestly."
)

# Store chat sessions per Django session
chat_sessions = {}


def get_chat(session_key):
    """Get or create a Gemini chat session for the given Django session."""
    if session_key not in chat_sessions:
        chat_sessions[session_key] = client.chats.create(
            model='gemini-2.0-flash',
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
            )
        )
    return chat_sessions[session_key]


def index(request):
    """Render the main chatbot page."""
    # Ensure Django session exists
    if not request.session.session_key:
        request.session.create()
    return render(request, 'webbot/index.html')


def bot_search(request):
    """Handle chat messages via POST."""
    if request.method == 'GET':
        return render(request, 'webbot/index.html')

    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=400)

    sentence = request.POST.get('query', '').strip()

    if not sentence:
        return render(request, 'webbot/index.html', {
            'error': 'Please enter a valid query'
        })

    try:
        # Ensure session exists
        if not request.session.session_key:
            request.session.create()

        chat = get_chat(request.session.session_key)
        gemini_response = chat.send_message(sentence)
        response = gemini_response.text
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"Gemini API error: {type(e).__name__}: {str(e)}", flush=True)
        response = "I'm experiencing technical difficulties. Please try again later."

    return render(request, 'webbot/index.html', {
        'response': response,
        'sentence': sentence
    })