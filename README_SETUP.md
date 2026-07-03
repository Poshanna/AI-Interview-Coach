# AI Interview Coach - Setup Guide

## What's been done:
✅ Removed friend's name from the codebase
✅ Installed Python dependencies (in ./lib folder)
✅ Installed frontend dependencies
✅ Created a startup script (run.py)
✅ Updated database configuration to use SQLite by default
✅ Created .env.example file

## Next Steps:

1. **Get a Gemini API Key**:
   - Go to https://aistudio.google.com/app/apikey
   - Create a new API key
   - Copy it

2. **Update your .env file**:
   Open the `.env` file in the project root and add your API key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   DATABASE_URL=sqlite:///./ai_interview_coach.db
   ```

3. **Run the backend**:
   ```bash
   python run.py
   ```

4. **Run the frontend** (in a new terminal):
   ```bash
   cd frontend
   npm run dev
   ```

5. **Open the app**:
   Go to http://localhost:5173 in your browser

---

## Important Note:
**Please tell me where you were seeing "service unavailable"!** Was it in Google AI Studio when trying to create an API key, or somewhere else?
