# Clean .env Configuration for Backend - 6 AI Providers!

## Problem Found
Your `.env` has **duplicate entries** and wrong model names causing issues.

## Correct Configuration - 6 Providers (4 FREE!)

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

# =======================================
# AI Providers (Priority: FREE → PAID)
# ========================================

# === FREE PROVIDERS (Use these first!) ===

# 1. Google Gemini (FREE - Primary)
GEMINI_API_KEY=AIzaSyDmgqT4G1LLb8M-tayLp32CYJQfdKoQiDI
GEMINI_MODEL=gemini-1.5-flash

# 2. Groq (FREE - Extremely fast)
GROQ_API_KEY=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
GROQ_MODEL=llama-3.1-8b-instant

# 3. Cohere (FREE - Good for general tasks)
# Get free key: https://dashboard.cohere.com/api-keys
COHERE_API_KEY=your-cohere-key-here
COHERE_MODEL=command-r

# 4. OpenRouter (FREE models available)
OPENROUTER_API_KEY=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
OPENROUTER_MODEL=meta-llama/llama-3.1-8b-instruct:free

# === PAID PROVIDERS (Fallback only) ===

# 5. Anthropic Claude (PAID - Strong reasoning)
# Get key: https://console.anthropic.com/
ANTHROPIC_API_KEY=your-anthropic-key-here
ANTHROPIC_MODEL=claude-3-haiku-20240307

# 6. OpenAI (PAID - Last resort)
OPENAI_API_KEY=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
OPENAI_MODEL=gpt-4o-mini
```

## Provider Priority (Smart Fallback)

Your chatbot will try in this order:

1. **Gemini** (FREE) - Google's fast model
2. **Groq** (FREE) - ⚡ Extremely fast inference  
3. **Cohere** (FREE) - Good for general tasks
4. **OpenRouter** (FREE) - Meta LLaMA model
5. **Anthropic** (Paid) - Strong reasoning if free options fail
6. **OpenAI** (Paid) - Last resort

## Free API Keys

Get these free keys to maximize reliability:

| Provider | URL | Free Tier? |
|----------|-----|-----------|
| **Gemini** | https://aistudio.google.com/app/apikey | ✅ Very generous |
| **Groq** | https://console.groq.com/ | ✅ Free |
| **Cohere** | https://dashboard.cohere.com/api-keys | ✅ Free trial |
| **OpenRouter** | https://openrouter.ai/keys | ✅ Free models |
| **Anthropic** | https://console.anthropic.com/ | ⚠️ Paid |
| **OpenAI** | https://platform.openai.com/api-keys | ⚠️ Paid |

## After Updating

1. Save the new `.env`
2. Get free Cohere key (optional but recommended)
3. Restart backend: `Ctrl+C` then restart server
4. Test chatbot - you now have **6 fallback options**!

## Benefits

✅ **4 completely FREE providers**
✅ **6 providers = maximum uptime**
✅ **Smart ordering** - tries free options first
✅ **Cost efficient** - paid providers only as last resort
