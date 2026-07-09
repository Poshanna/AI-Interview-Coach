# AI Smart Interview Coach

Practice AI-powered interviews tailored to your skills, resume, and career goals. Get evaluated in real-time by advanced LLMs.

## 🌐 Live Demo

- **Frontend**: https://ai-interview-coach-olive.vercel.app
- **Backend**: https://ai-interview-coach-backend-n4mz.onrender.com

## ✨ Features

- 📄 **Resume Analysis**: Upload your PDF resume - Aura extracts your skills, projects, certifications, and experience
- 🎯 **Adaptive Questions**: Generative question pipelines that scale difficulty dynamically based on prior responses
- 🎤 **Speech-to-Text**: State-of-the-art Web Speech API integration translating voice answers into text editor streams
- 📊 **Real-Time Feedback**: Instant evaluation showing score, explanation, and sample ideal answers for every query
- 📜 **Interview History**: Secure session logging enabling you to review previous logs and trace progress
- 📈 **Performance Dashboard**: Comprehensive visual diagnostics featuring core competencies, study grids, and weakness charts

## 🛠️ Tech Stack

### Frontend
- React 19
- Vite
- Tailwind CSS
- Axios
- React Router DOM

### Backend
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- Google Gemini API
- Python-JOSE (JWT authentication)

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js 18+
- npm or yarn
- Gemini API Key (from https://aistudio.google.com/app/apikey)

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Poshanna/AI-Interview-Coach.git
   cd AI-Interview-Coach
   ```

2. **Backend Setup**
   ```bash
   # Create virtual environment
   python -m venv .venv
   
   # Activate virtual environment
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Create .env file
   cp .env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   cp .env.example .env
   ```

4. **Run the App**
   - **Backend**: In project root: `python run.py`
   - **Frontend**: In frontend directory: `npm run dev`

5. **Open in browser**: http://localhost:5173

## 📝 Environment Variables

### Backend (.env)
```
GEMINI_API_KEY=your_gemini_api_key_here
DATABASE_URL=sqlite:///./ai_interview_coach.db
```

### Frontend (frontend/.env)
```
VITE_API_URL=http://127.0.0.1:8003
```

## 🚀 Deployment

- **Frontend**: Deployed on Vercel
- **Backend**: Deployed on Render

## 📄 License

MIT

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
