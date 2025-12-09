# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

# ===== FASTAPI APPLICATION =====
app = FastAPI(
    title="FastAPI Backend with AI Support",
    description="Backend for authentication, user management, and AI chatbot",
    version="1.0.0"
)

# CORS configuration - Allow all for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:8000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# ===== STARTUP EVENT =====
@app.on_event("startup")
async def startup_event():
    from app.database.db import init_db
    try:
        init_db()
        print("✅ Database initialized successfully!")
    except Exception as e:
        print(f"⚠️ Database initialization failed: {e}")
        print("ℹ️ Chatbot will work, but authentication requires a valid database connection.")
        print("ℹ️ Update DATABASE_URL in backend/.env to enable authentication.")

# ===== ROUTES =====
@app.get("/")
def read_root():
    return {
        "message": "FastAPI backend is running!",
        "features": ["Authentication", "User Management", "AI Chatbot via /api/query"]
    }

# ===== INCLUDE API ROUTERS =====
from app.api import auth
from app.api import chat

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(chat.router, prefix="/api", tags=["chat"])