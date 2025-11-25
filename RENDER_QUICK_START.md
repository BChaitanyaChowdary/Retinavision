# 🚀 Quick Start: Deploy to Render in 10 Minutes

## Step 1: Create Database (2 min)
1. Go to https://dashboard.render.com
2. Click **New +** → **PostgreSQL**
3. Name: `retinavision-db`, Region: Singapore, Plan: Free
4. Click **Create Database**
5. **Copy the Internal Database URL**

## Step 2: Deploy Backend (5 min)
1. Click **New +** → **Web Service**
2. Connect GitHub: `BChaitanyaChowdary/Retinavision`
3. Settings:
   - Name: `retinavision-backend`
   - Build: `cd backend && pip install -r requirements.txt`
   - Start: `cd backend && gunicorn app:app`
4. Environment Variables:
   ```
   DATABASE_URL = [paste database URL]
   OPENAI_API_KEY = [your OpenAI key]
   FLASK_ENV = production
   ```
5. Click **Create Web Service**
6. **Copy backend URL** (e.g., `https://retinavision-backend.onrender.com`)

## Step 3: Deploy Frontend (3 min)
1. Click **New +** → **Static Site**
2. Connect GitHub: `BChaitanyaChowdary/Retinavision`
3. Settings:
   - Name: `retinavision-frontend`
   - Build: `cd frontend && npm install && npm run build`
   - Publish: `frontend/build`
4. Environment Variable:
   ```
   REACT_APP_API_URL = [paste backend URL]
   ```
5. Click **Create Static Site**

## Step 4: Initialize Database (1 min)
1. Go to backend service → **Shell** tab
2. Run:
   ```bash
   cd backend
   python init_database.py
   ```

## ✅ Done!
Open your frontend URL and start using RetinaVision!

**Note**: First load may take 30-60 seconds (cold start on free tier).

---

For detailed instructions, see [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md)
