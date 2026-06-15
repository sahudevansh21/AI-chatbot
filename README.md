# 🤖 AI Chatbot — Powered by Gemini

A Django-powered AI chatbot integrated with Google's **Gemini 2.0 Flash** API, delivering intelligent, context-aware responses with a sleek, modern dark-themed UI.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Django](https://img.shields.io/badge/Django-4.2-green?logo=django)
![Gemini](https://img.shields.io/badge/Gemini-2.0_Flash-purple?logo=google)

## ✨ Features

- 🧠 **Gemini AI Integration** — Powered by Google's Gemini 2.0 Flash for intelligent responses
- 💬 **Session-based Chat Memory** — Maintains conversation context per user session
- 🎨 **Premium Dark UI** — Glassmorphism, purple accents, smooth animations
- 🔒 **Secure** — CSRF protection, API key stored in environment variables
- ⚡ **Fast & Lightweight** — No heavy ML dependencies, just Django + Gemini SDK
- 📱 **Fully Responsive** — Works beautifully on desktop and mobile

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Django 4.2, Python 3.9+ |
| **AI Engine** | Google Gemini 2.0 Flash (via `google-genai`) |
| **Frontend** | HTML5, CSS3, Font Awesome |
| **Design** | Dark theme, Glassmorphism, Inter font |

## 🚀 Setup Guide

### 1. Clone the repository
```bash
git clone https://github.com/sahudevansh21/AI-chatbot.git
cd AI-chatbot
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your Gemini API Key
Create a `.env` file in the project root:
```bash
echo "GEMINI_API_KEY=your_api_key_here" > .env
```
Get your free API key at [aistudio.google.com](https://aistudio.google.com/apikey)

### 5. Run migrations
```bash
python manage.py migrate
```

### 6. Start the server
```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser 🎉

## 📁 Project Structure

```
AI-chatbot/
├── chat/                  # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── chatbot/               # Main chatbot app
│   ├── views.py           # Gemini API integration
│   ├── urls.py
│   └── templates/
│       └── webbot/
│           └── index.html # Chat UI
├── .env                   # API key (not in repo)
├── .gitignore
├── manage.py
└── requirements.txt
```

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

Made with ❤️ by [Devansh Sahu](https://github.com/sahudevansh21)
