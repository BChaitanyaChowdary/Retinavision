# 🚂 Deploy RetinaVision to Railway.app

Railway.app offers **1GB RAM free tier** (2x more than Render's 512MB) - perfect for your TensorFlow model!

---

## 📋 Prerequisites

1. GitHub account with your code
2. Railway account (sign up at https://railway.app)
3. Your existing Render PostgreSQL database URL
4. OpenAI API key

---

## 🚀 Step-by-Step Deployment

### Step 1: Sign Up for Railway (2 minutes)

1. Go to https://railway.app
2. Click **"Login"** → **"Login with GitHub"**
3. Authorize Railway to access your GitHub
4. You get **$5 free credit** + **1GB RAM free tier**

### Step 2: Create New Project (1 minute)

1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Choose **"BChaitanyaChowdary/Retinavision"**
4. Railway will detect it's a Python app

### Step 3: Configure Backend Service (3 minutes)

1. Railway will create a service automatically
2. Click on the service
3. Go to **"Settings"** tab

#### Configure Build & Start:

**Root Directory:**
```
backend
```

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
gunicorn app:app --bind 0.0.0.0:$PORT --timeout 120 --workers 1
```

**Watch Paths:**
```
backend/**
```

### Step 4: Add Environment Variables (2 minutes)

Click **"Variables"** tab and add:

```
DATABASE_URL = [Your Render PostgreSQL Internal URL]
OPENAI_API_KEY = [Your OpenAI API key]
FLASK_ENV = production
FLASK_DEBUG = False
PORT = 8080
PYTHON_VERSION = 3.11.0
```

**Important:** Use your **existing Render PostgreSQL URL** - no need to create a new database!

### Step 5: Deploy! (5-7 minutes)

1. Click **"Deploy"**
2. Watch the logs - you'll see:
   ```
   Installing Python 3.11.0
   Installing dependencies...
   ✅ Model loaded successfully
   Starting gunicorn...
   ```

3. Once deployed, click **"Settings"** → **"Generate Domain"**
4. Copy your Railway URL (e.g., `https://retinavision-production.up.railway.app`)

---

## 🎨 Deploy Frontend

### Option 1: Keep Frontend on Render (Recommended)

1. Go to your Render frontend service
2. Update environment variable:
   ```
   REACT_APP_API_URL = [Your Railway backend URL]
   ```
3. Save - it will redeploy automatically

### Option 2: Deploy Frontend on Railway Too

1. In Railway, click **"New Service"**
2. Select same GitHub repo
3. Configure:
   - **Root Directory:** `frontend`
   - **Build Command:** `npm install && npm run build`
   - **Start Command:** `npx serve -s build -p $PORT`
4. Add variable:
   ```
   REACT_APP_API_URL = [Your Railway backend URL]
   ```

---

## ✅ Verify Deployment

### Test Backend:

```
https://your-railway-url.up.railway.app/api/health
```

Should return:
```json
{
  "status": "healthy",
  "model_loaded": true,
  "model_classes": 8
}
```

### Test Frontend:

1. Open your frontend URL
2. Upload an eye image
3. **It should work!** 🎉

---

## 💰 Railway Free Tier Details

**What You Get:**
- ✅ **1GB RAM** (2x more than Render!)
- ✅ **$5 free credit/month**
- ✅ **500 hours execution time**
- ✅ **100GB bandwidth**
- ✅ **No credit card required** for trial

**Limits:**
- After $5 credit, need to add payment
- Services sleep after 30 min inactivity (like Render)
- Can upgrade to Hobby plan ($5/month) for always-on

---

## 🔧 Railway Configuration Files

Railway auto-detects Python, but you can create these files for better control:

### railway.json (Optional)

```json
{
  "build": {
    "builder": "NIXPACKS",
    "buildCommand": "cd backend && pip install -r requirements.txt"
  },
  "deploy": {
    "startCommand": "cd backend && gunicorn app:app --bind 0.0.0.0:$PORT --timeout 120 --workers 1",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

### nixpacks.toml (Optional)

```toml
[phases.setup]
nixPkgs = ["python311", "postgresql"]

[phases.install]
cmds = ["cd backend && pip install -r requirements.txt"]

[start]
cmd = "cd backend && gunicorn app:app --bind 0.0.0.0:$PORT --timeout 120 --workers 1"
```

---

## 🎯 Advantages Over Render Free Tier

| Feature | Railway | Render Free |
|---------|---------|-------------|
| RAM | **1GB** ✅ | 512MB ❌ |
| Model Loading | **Works!** ✅ | Out of Memory ❌ |
| Predictions | **Fast** ✅ | Crashes ❌ |
| Setup | Easy | Easy |
| Database | Use Render's | Built-in |

---

## 🔄 Using Your Existing Render Database

**Good news:** You can keep using your Render PostgreSQL database!

1. Get your Render database **Internal Connection String**:
   - Go to Render Dashboard
   - Click on your PostgreSQL database
   - Copy **Internal Database URL**

2. Add it to Railway as `DATABASE_URL` variable

3. Both Render and Railway can access the same database!

**Why this works:**
- Render PostgreSQL is accessible from anywhere
- No data migration needed
- Keep all your existing data

---

## 🆘 Troubleshooting

### Build Fails

**Check:**
- Root directory is set to `backend`
- Python version is 3.11
- requirements.txt exists

### Model Not Loading

**Check logs:**
```
Railway Dashboard → Your Service → Deployments → View Logs
```

Look for:
```
✅ Model loaded successfully
```

### Database Connection Error

**Check:**
- DATABASE_URL is correct
- Using Internal URL (not External)
- Database is running on Render

### Out of Memory (Unlikely on Railway)

If still happens:
- Reduce image size before upload
- Upgrade to Hobby plan ($5/month) for 2GB RAM

---

## 📊 Cost Comparison

| Platform | Free RAM | Paid RAM | Cost |
|----------|----------|----------|------|
| **Railway** | 1GB | 2GB | $5/mo |
| Render | 512MB | 2GB | $7/mo |
| Fly.io | 256MB | 1GB | $5/mo |

**Railway = Best value for ML models!** 🏆

---

## 🎉 Quick Start Checklist

- [ ] Sign up at railway.app
- [ ] Create new project from GitHub
- [ ] Set root directory to `backend`
- [ ] Add environment variables (DATABASE_URL, OPENAI_API_KEY)
- [ ] Deploy and wait 5-7 minutes
- [ ] Generate domain
- [ ] Update frontend REACT_APP_API_URL
- [ ] Test predictions - should work!

---

## 🚀 Next Steps After Deployment

1. **Test thoroughly** - Upload multiple images
2. **Monitor usage** - Check Railway dashboard for RAM usage
3. **Optimize if needed** - Railway shows real-time metrics
4. **Upgrade if needed** - If you exceed $5 credit, add payment

---

**Your model WILL work on Railway because of the 1GB RAM!** 🎉

No more "Worker killed" errors!
