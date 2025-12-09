# Clean .env Configuration for Backend

## Problem Found
Your `.env` has **duplicate entries** and wrong model names causing issues:
- `MODEL_NAME=gemini-2.5-flash` (doesn't exist!)
- Duplicate `GEMINI_API_KEY`
- Duplicate `MODEL_NAME`

This made Gemini try to use `gpt-4o-mini` instead of its own model!

## Correct Configuration

Replace your `.env` content with this:

```bash
# ========================================
# Backend Environment Variables
# ========================================

# JWT Authentication
SECRET_KEY=VIT8dt_iKFtp3fcmcXPjCPTFS3uTqHntxuUus9DDK18
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_DAYS=7

# Database
DATABASE_URL=postgresql://hackathon_hlyh_user:agYME7qnOSkXQYqtkZl2NTWjDQW8GyzD@dpg-d4m1ctruibrs738a9tm0-a.oregon-postgres.render.com/hackathon_hlyh

# ========================================
# AI Providers (Gemini → OpenAI → OpenRouter → Groq)
# ========================================

# Google Gemini (Primary - FREE)
GEMINI_API_KEY=AIzaSyDmgqT4G1LLb8M-tayLp32CYJQfdKoQiDI
GEMINI_MODEL=gemini-1.5-flash

# OpenAI (Fallback - PAID)
OPENAI_API_KEY=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
OPENAI_MODEL=gpt-4o-mini

# OpenRouter (Fallback - FREE)
OPENROUTER_API_KEY=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
OPENROUTER_MODEL=meta-llama/llama-3.1-8b-instruct:free

# Groq (Fallback - FREE, very fast)
GROQ_API_KEY=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  
GROQ_MODEL=llama-3.1-8b-instant
```

## Key Changes

1. ❌ **Removed** duplicate `GEMINI_API_KEY` entries
2. ❌ **Removed** duplicate and incorrect `MODEL_NAME` entries  
3. ✅ **Added** `GEMINI_MODEL=gemini-1.5-flash` (correct model)
4. ✅ **Fixed** Groq configuration (was GROK, now GROQ)
5. ✅ **Clean** - no duplicates, proper model names

## After Updating

1. Save the new `.env`
2. Restart backend: `Ctrl+C` then `python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`
3. Test chatbot - it should work!
