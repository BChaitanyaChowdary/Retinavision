# Eye Disease Classification System - Full Stack Application

## 🏥 Professional Medical AI System

Complete React + Flask application for eye disease classification with medical-grade visualizations.

---

## 📁 Project Structure

```
project/
├── backend/              # Flask API
│   ├── app.py           # Main Flask application
│   └── requirements.txt
├── frontend/            # React application
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── App.js
│   │   ├── index.js
│   │   └── App.css
│   └── package.json
└── my_model.h5         # Your trained model (place in root)
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

---

## 🔧 Backend Setup (Flask)

### 1. Navigate to backend folder
```bash
cd backend
```

### 2. Create virtual environment
```bash
python -m venv venv
```

### 3. Activate virtual environment
**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Place your model
Copy `my_model.h5` to the root directory (one level above backend)

### 6. Run Flask server
```bash
python app.py
```

**Backend will run on:** `http://localhost:5000`

---

## 💻 Frontend Setup (React)

### 1. Navigate to frontend folder (new terminal)
```bash
cd frontend
```

### 2. Install dependencies
```bash
npm install
```

### 3. Start React app
```bash
npm start
```

**Frontend will run on:** `http://localhost:3000`

---

## 🎯 Usage

1. **Open browser** → `http://localhost:3000`
2. **Upload eye image** (drag & drop or click)
3. **Click "Analyze Image"**
4. **View results:**
   - AI Diagnosis with confidence
   - Heatmap visualization
   - Affected areas
   - Medical recommendations

---

## 🔌 API Endpoints

### Health Check
```
GET /api/health
```

### Predict
```
POST /api/predict
Content-Type: multipart/form-data
Body: image file

Response:
{
  "success": true,
  "prediction": {
    "class": "Glaucoma",
    "confidence": 89.53,
    "class_index": 5
  },
  "all_predictions": {...},
  "images": {
    "original": "base64...",
    "heatmap": "base64...",
    "affected_areas": "base64..."
  }
}
```

### Get Classes
```
GET /api/classes
```

---

## 🎨 Features

✅ **Professional Medical UI** - Material-UI design
✅ **Real-time Analysis** - Instant predictions
✅ **GradCAM Visualization** - AI attention heatmaps
✅ **Disease Detection** - Affected area highlighting
✅ **Medical Recommendations** - Treatment & lifestyle advice
✅ **Confidence Levels** - Color-coded confidence indicators
✅ **Drag & Drop Upload** - Easy image selection
✅ **Responsive Design** - Works on all devices

---

## 🧪 Disease Classes

1. Cataract
2. Choroidal Neovascularization (CNV)
3. Diabetic Macular Edema (DME)
4. Diabetic Retinopathy
5. Drusen
6. Glaucoma
7. Normal
8. Normal-1

---

## 🛠️ Troubleshooting

### Backend Issues

**Port 5000 already in use:**
```python
# In backend/app.py, change:
app.run(host='0.0.0.0', port=5001, debug=True)
```

**Model not found:**
- Ensure `my_model.h5` is in the root directory
- Check `MODEL_PATH` in `backend/app.py`

**CORS errors:**
- Flask-CORS is installed and configured
- Check frontend API URL in `App.js`

### Frontend Issues

**npm install fails:**
```bash
npm install --legacy-peer-deps
```

**API connection refused:**
- Ensure backend is running on port 5000
- Check `API_BASE_URL` in `App.js`

---

## 📦 Production Deployment

### Backend (Flask)
```bash
# Using gunicorn
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Frontend (React)
```bash
npm run build
# Serve the 'build' folder with nginx or serve
```

---

## 🔒 Security Notes

- Add authentication for production
- Implement rate limiting
- Validate file uploads
- Use HTTPS in production
- Add input sanitization

---

## 📝 License

Professional Medical AI System - All Rights Reserved

---

## 🆘 Support

For issues or questions:
1. Check troubleshooting section
2. Review console logs (F12 in browser)
3. Check both backend and frontend terminals

---

## ✨ Next Steps

1. Add user authentication
2. Implement PDF report generation
3. Add patient management system
4. Create history/archive feature
5. Add multi-language support

---

**Developed with ❤️ for Professional Medical AI**
