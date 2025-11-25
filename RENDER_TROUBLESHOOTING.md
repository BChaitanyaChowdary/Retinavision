# 🔧 Render Deployment Troubleshooting

## ✅ Issue Fixed: TensorFlow Compatibility

**Problem**: `TypeError: unhashable type: 'list'` when importing TensorFlow

**Solution**: Updated to Python 3.9.18 and pinned TensorFlow to 2.15.0

The deployment should now work correctly!

---

## Common Deployment Issues

### 1. Build Fails - Dependencies

**Error**: `Could not find a version that satisfies the requirement`

**Solutions**:
- Check `requirements.txt` has correct versions
- Use `opencv-python-headless` instead of `opencv-python` (no GUI needed)
- Pin specific versions instead of using `>=`

**Current Working Versions**:
```
Python: 3.9.18
TensorFlow: 2.15.0
OpenCV: 4.8.1.78 (headless)
NumPy: 1.24.3
```

### 2. Model File Too Large

**Error**: `File size exceeds GitHub limit`

**Solutions**:

**Option A: Use Git LFS** (Recommended)
```bash
git lfs install
git lfs track "*.h5"
git add .gitattributes
git add backend/my_modeltrained3.h5
git commit -m "Add model with Git LFS"
git push
```

**Option B: External Storage**
- Upload model to Google Drive, Dropbox, or AWS S3
- Download in startup script:
```python
# In app.py before loading model
import requests
import os

MODEL_URL = "https://your-storage-url/model.h5"
MODEL_PATH = "my_modeltrained3.h5"

if not os.path.exists(MODEL_PATH):
    print("Downloading model...")
    response = requests.get(MODEL_URL)
    with open(MODEL_PATH, 'wb') as f:
        f.write(response.content)
```

### 3. Database Connection Error

**Error**: `could not connect to server`

**Solutions**:
- Verify `DATABASE_URL` environment variable is set
- Use **Internal Database URL** (not External)
- Check database is in same region as backend
- Ensure database is running (not paused)

**Test Connection**:
```python
# In Shell tab
python
>>> import os
>>> print(os.getenv('DATABASE_URL'))
>>> from database import db
>>> db.create_all()
```

### 4. OpenAI API Error

**Error**: `AuthenticationError` or `RateLimitError`

**Solutions**:
- Verify `OPENAI_API_KEY` is set correctly
- Check API key has credits: https://platform.openai.com/usage
- Ensure key has proper permissions
- Check for typos (no spaces, correct prefix `sk-proj-`)

### 5. Cold Start Timeout

**Issue**: First request takes 30-60 seconds

**This is normal on Free Tier**:
- Service spins down after 15 minutes of inactivity
- First request "wakes up" the service
- Subsequent requests are fast

**Solutions**:
- Upgrade to Starter plan ($7/month) - no spin down
- Use a ping service to keep it alive (not recommended for free tier)
- Inform users about initial load time

### 6. Memory Issues

**Error**: `MemoryError` or service crashes

**Solutions**:
- Free tier has 512MB RAM limit
- TensorFlow model loading uses significant memory
- Consider upgrading to Starter plan (2GB RAM)
- Optimize model size if possible

**Check Memory Usage**:
```bash
# In Shell tab
free -h
```

### 7. Static Files Not Found

**Error**: `404` for images, CSS, or visualizations

**Solutions**:
- Ensure `static` folder is in repository
- Check paths are relative, not absolute
- Verify `CORS` is enabled for static files
- Use `send_from_directory` in Flask

### 8. Frontend Can't Connect to Backend

**Error**: `Network Error` or `CORS Error`

**Solutions**:
- Verify `REACT_APP_API_URL` is set correctly
- Must include `https://` prefix
- No trailing slash
- Check backend CORS configuration
- Ensure backend is deployed and running

**Test Backend**:
```bash
curl https://your-backend.onrender.com/api/health
```

### 9. Environment Variables Not Loading

**Error**: `None` values for environment variables

**Solutions**:
- Check variables are set in Render dashboard
- Restart service after adding variables
- Use `python-dotenv` for local development only
- Don't commit `.env` files

**Verify Variables**:
```python
# In Shell tab
python
>>> import os
>>> print(os.getenv('OPENAI_API_KEY'))
>>> print(os.getenv('DATABASE_URL'))
```

### 10. Build Command Fails

**Error**: Build exits with non-zero status

**Solutions**:
- Check build logs for specific error
- Verify `cd backend` path is correct
- Ensure `requirements.txt` exists
- Check for syntax errors in Python files

**Test Build Locally**:
```bash
cd backend
pip install -r requirements.txt
python -c "import app"
```

---

## Debugging Tips

### View Logs
1. Go to service in Render dashboard
2. Click **"Logs"** tab
3. Look for errors during:
   - Build phase
   - Startup phase
   - Runtime

### Use Shell
1. Go to service in Render dashboard
2. Click **"Shell"** tab
3. Run commands to debug:
```bash
cd backend
python
>>> import tensorflow as tf
>>> print(tf.__version__)
>>> from app import app
>>> print(app.config)
```

### Check Service Status
- Green dot = Running
- Yellow dot = Building
- Red dot = Failed

### Monitor Performance
- Click **"Metrics"** tab
- Check CPU, Memory, Response time
- Look for spikes or crashes

---

## Performance Optimization

### 1. Reduce Model Size
- Use model quantization
- Remove unnecessary layers
- Use TensorFlow Lite

### 2. Cache Static Files
- Use CDN for images
- Enable browser caching
- Compress images

### 3. Database Optimization
- Add indexes to frequently queried columns
- Use connection pooling
- Limit query results

### 4. API Optimization
- Implement rate limiting
- Cache API responses
- Use async processing for heavy tasks

---

## Getting Help

### Render Support
- **Docs**: https://render.com/docs
- **Community**: https://community.render.com
- **Status**: https://status.render.com

### Check Service Health
```bash
curl https://your-backend.onrender.com/api/health
```

Expected response:
```json
{
  "status": "healthy",
  "service": "RetinaVision Backend",
  "timestamp": "2025-11-25T10:30:00"
}
```

---

## Quick Fixes Checklist

- [ ] Python version is 3.9.18
- [ ] TensorFlow version is 2.15.0
- [ ] Using `opencv-python-headless`
- [ ] All environment variables are set
- [ ] Database URL is Internal (not External)
- [ ] Model file is in repository or downloadable
- [ ] CORS is enabled in backend
- [ ] Frontend has correct backend URL
- [ ] Build and start commands are correct
- [ ] Service has restarted after changes

---

**Still having issues?** Check the full logs and error messages, then search Render docs or community forum.
