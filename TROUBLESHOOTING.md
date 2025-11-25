# 🔧 Troubleshooting Guide

## "Failed to Process Image" Error

### Quick Fix:

1. **Check Backend is Running:**
   ```bash
   # Should see: Running on http://127.0.0.1:5000
   ```

2. **Check Backend Console for Errors:**
   - Look for red error messages
   - Check what step failed

3. **Restart Backend:**
   ```bash
   # Stop: Ctrl+C
   cd backend
   python app.py
   ```

4. **Clear Browser Cache:**
   - Press: Ctrl+Shift+Delete
   - Clear cache
   - Refresh: Ctrl+F5

### Common Causes:

#### 1. Database Connection Issue
**Symptoms:**
- "Failed to process image"
- Backend shows database errors

**Solution:**
```bash
cd backend
python test_database.py
```

If test fails:
```bash
python init_database.py
```

#### 2. Model Not Loaded
**Symptoms:**
- "Model not loaded" error
- Backend shows model loading errors

**Solution:**
```bash
cd backend
# Check if model exists
dir my_modeltrained3.h5

# If missing, model file is required
```

#### 3. Missing Dependencies
**Symptoms:**
- "Module not found" errors
- Import errors

**Solution:**
```bash
cd backend
pip install -r requirements.txt
```

#### 4. Port Already in Use
**Symptoms:**
- "Address already in use"
- Backend won't start

**Solution:**
```bash
# Windows
taskkill /F /IM python.exe
taskkill /F /IM node.exe

# Then restart
python app.py
```

#### 5. Image Format Issue
**Symptoms:**
- "Failed to process image"
- Only happens with certain images

**Solution:**
- Use PNG or JPG format
- Image should be < 10MB
- Try a different image

### Debug Steps:

#### Step 1: Check Backend Logs
When you upload an image, backend should show:
```
=== PREDICTION VISUALIZATION REQUEST RECEIVED ===
✅ Image file received: image.jpg
✅ Image loaded successfully
✅ Image preprocessed successfully
✅ Prediction completed
✅ Patient saved to database
✅ Prediction saved to database
```

If you see ❌ or ⚠️, that's where the error is.

#### Step 2: Test Database
```bash
cd backend
python test_database.py
```

Should show:
```
✅ All tests passed!
```

#### Step 3: Check Frontend Console
- Press F12 in browser
- Go to Console tab
- Look for red errors

#### Step 4: Check Network Tab
- Press F12 in browser
- Go to Network tab
- Upload image
- Click on "predict_visualize" request
- Check Response tab for error message

### Specific Error Messages:

#### "No image file provided"
- **Cause:** Image not uploaded correctly
- **Fix:** Make sure to select an image before clicking Analyze

#### "Model not loaded"
- **Cause:** ML model file missing or failed to load
- **Fix:** Check `backend/my_modeltrained3.h5` exists

#### "Database connection failed"
- **Cause:** PostgreSQL connection issue
- **Fix:** Run `python init_database.py`

#### "Patient save failed"
- **Cause:** Database error or missing patient data
- **Fix:** Fill in all required patient fields (Name, Age, Gender, DOB)

### Still Not Working?

#### Complete Reset:

1. **Stop Everything:**
   ```bash
   # Windows
   taskkill /F /IM python.exe
   taskkill /F /IM node.exe
   ```

2. **Clear Everything:**
   ```bash
   # Clear browser cache: Ctrl+Shift+Delete
   # Close all browser tabs
   ```

3. **Restart Backend:**
   ```bash
   cd backend
   python test_database.py  # Should pass
   python app.py            # Should start without errors
   ```

4. **Restart Frontend:**
   ```bash
   cd frontend
   npm start
   ```

5. **Test with Simple Image:**
   - Use a small PNG or JPG
   - Fill in all patient details
   - Click Analyze

### Check Backend Output:

When working correctly, you should see:
```
✅ Database tables created successfully
📊 Tables created:
   - patients
   - predictions
   - statistics

* Running on http://127.0.0.1:5000

[When you upload image]
=== PREDICTION VISUALIZATION REQUEST RECEIVED ===
✅ Image file received: test.jpg
✅ Image loaded successfully. Image size: (512, 512)
✅ Image preprocessed successfully. Shape: (1, 128, 128, 3)
✅ Prediction completed. Predictions shape: (1, 8)
✅ Prediction results - Disease: Cataract, Confidence: 95.23
🤖 Generating AI-powered recommendations...
✅ AI recommendations generated successfully
✅ Patient saved to database
✅ Prediction saved to database
✅ Statistics updated
✅ Prediction visualization completed successfully
```

### Get Help:

If still not working, check:
1. Backend console output (copy the error)
2. Frontend console (F12 → Console tab)
3. Network tab (F12 → Network → predict_visualize → Response)

The error message will tell you exactly what's wrong!
