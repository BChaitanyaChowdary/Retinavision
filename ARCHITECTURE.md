# 🏗️ ARCHITECTURE OVERVIEW

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                          USER BROWSER                           │
│                     http://localhost:3000                       │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    REACT FRONTEND (PORT 3000)                   │
├─────────────────────────────────────────────────────────────────┤
│  Components:                                                    │
│  ├── App.js                    Main application                │
│  ├── ImageUploader.js          Drag & drop upload              │
│  ├── ImageViewer.js            3-tab image viewer              │
│  ├── PredictionResult.js       Results display                 │
│  └── MedicalRecommendations.js Medical information             │
│                                                                 │
│  Features:                                                      │
│  ✅ Material-UI components                                      │
│  ✅ Professional medical design                                 │
│  ✅ Real-time predictions                                       │
│  ✅ Responsive layout                                           │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ HTTP POST /api/predict
                             │ (multipart/form-data)
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                     FLASK BACKEND (PORT 5000)                   │
├─────────────────────────────────────────────────────────────────┤
│  Endpoints:                                                     │
│  ├── GET  /api/health        Health check                      │
│  ├── POST /api/predict       Image analysis                    │
│  └── GET  /api/classes       Available diseases                │
│                                                                 │
│  Processing Pipeline:                                          │
│  1. Receive image                                              │
│  2. Preprocess (resize, normalize)                             │
│  3. Run TensorFlow prediction                                  │
│  4. Generate GradCAM heatmap                                   │
│  5. Detect affected areas                                      │
│  6. Convert to base64                                          │
│  7. Return JSON response                                       │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      AI MODEL (my_model.h5)                     │
├─────────────────────────────────────────────────────────────────┤
│  Architecture: CNN (MobileNet/EfficientNet)                     │
│  Input: 224x224x3 RGB images                                   │
│  Output: 8 classes (disease predictions)                       │
│                                                                 │
│  Classes:                                                       │
│  1. Cataract                                                   │
│  2. Choroidal Neovascularization (CNV)                         │
│  3. Diabetic Macular Edema (DME)                               │
│  4. Diabetic Retinopathy                                       │
│  5. Drusen                                                     │
│  6. Glaucoma                                                   │
│  7. Normal                                                     │
│  8. Normal-1                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Data Flow

```
User Upload Image
       │
       ▼
┌──────────────┐
│   Frontend   │ ─────► Preview Image
│  (React UI)  │
└──────┬───────┘
       │ Click "Analyze"
       ▼
  POST /api/predict
       │
       ▼
┌──────────────┐
│   Backend    │ ─────► Load Image
│   (Flask)    │
└──────┬───────┘
       │
       ▼
  Preprocess Image
  (224x224, normalize)
       │
       ▼
┌──────────────┐
│  AI Model    │ ─────► Get Predictions
│ (TensorFlow) │        [Class, Confidence]
└──────┬───────┘
       │
       ▼
  Generate GradCAM
  (Attention Heatmap)
       │
       ▼
  Detect Affected Areas
  (Yellow Contours)
       │
       ▼
  Convert to Base64
       │
       ▼
  JSON Response {
    prediction: {...},
    images: {...}
  }
       │
       ▼
┌──────────────┐
│   Frontend   │ ─────► Display Results
│              │        ├── Diagnosis
│              │        ├── Heatmap
│              │        ├── Affected Areas
│              │        └── Recommendations
└──────────────┘
```

---

## Technology Stack

### Frontend (React)
```
React 18.2
├── @mui/material          # UI components
├── @mui/icons-material    # Icons
├── axios                  # HTTP client
├── react-dropzone         # File upload
└── recharts              # Charts (optional)
```

### Backend (Flask)
```
Python 3.8+
├── Flask 3.0             # Web framework
├── flask-cors            # CORS support
├── TensorFlow 2.14+      # AI/ML
├── OpenCV 4.8+           # Image processing
├── NumPy                 # Numerical operations
└── Pillow                # Image handling
```

---

## File Structure

```
project/
│
├── backend/
│   ├── app.py                    # Flask API (322 lines)
│   ├── requirements.txt          # Python dependencies
│   └── venv/                     # Python virtual env (created on setup)
│
├── frontend/
│   ├── public/
│   │   └── index.html           # HTML template
│   ├── src/
│   │   ├── components/
│   │   │   ├── ImageUploader.js        # Upload component
│   │   │   ├── ImageViewer.js          # Image viewer
│   │   │   ├── PredictionResult.js     # Results display
│   │   │   └── MedicalRecommendations.js # Medical info
│   │   ├── App.js               # Main React app
│   │   ├── App.css              # Styles
│   │   └── index.js             # Entry point
│   ├── package.json             # Node dependencies
│   ├── .env                     # Environment config
│   └── node_modules/            # Node packages (created on npm install)
│
├── my_model.h5                  # Trained TensorFlow model
├── start_app.bat                # Windows startup script
├── QUICK_START.md               # Quick start guide
├── SETUP_INSTRUCTIONS.md        # Detailed setup
└── .gitignore                   # Git ignore rules
```

---

## API Contract

### Request
```http
POST /api/predict HTTP/1.1
Host: localhost:5000
Content-Type: multipart/form-data

image: [binary file data]
```

### Response
```json
{
  "success": true,
  "prediction": {
    "class": "Glaucoma",
    "confidence": 89.53,
    "class_index": 5
  },
  "all_predictions": {
    "Cataract": 6.00,
    "Choroidal Neovascularization": 0.48,
    "Diabetic Macular Edema": 0.76,
    "Diabetic Retinopathy": 0.54,
    "Drusen": 0.74,
    "Glaucoma": 89.53,
    "Normal": 0.00,
    "Normal-1": 1.94
  },
  "images": {
    "original": "iVBORw0KGgoAAAANS...",
    "heatmap": "iVBORw0KGgoAAAANS...",
    "affected_areas": "iVBORw0KGgoAAAANS..."
  },
  "timestamp": "2025-11-10T12:30:45.123456"
}
```

---

## Performance Optimization

### Backend
- ✅ Model loaded once at startup (not per request)
- ✅ NumPy vectorized operations
- ✅ OpenCV GPU acceleration (if available)
- ✅ Efficient base64 encoding
- ✅ CORS configured for specific origin

### Frontend
- ✅ React virtual DOM
- ✅ Component lazy loading possible
- ✅ Image preview before upload
- ✅ Optimized Material-UI components
- ✅ Production build minification

---

## Security Considerations

### Current (Development)
- ⚠️ No authentication
- ⚠️ Open CORS (any origin)
- ⚠️ No rate limiting
- ⚠️ No file size validation

### Production TODO
- 🔐 Add JWT authentication
- 🔐 Restrict CORS to specific domain
- 🔐 Implement rate limiting
- 🔐 Add file size/type validation
- 🔐 Use HTTPS
- 🔐 Sanitize inputs
- 🔐 Add logging/monitoring

---

## Deployment Architecture

```
Production Environment
│
├── Frontend (Static Files)
│   ├── Netlify / Vercel / AWS S3 + CloudFront
│   └── Build: npm run build → Deploy 'build' folder
│
├── Backend (API Server)
│   ├── Heroku / AWS EC2 / Google Cloud Run / Azure
│   ├── Run: gunicorn -w 4 app:app
│   └── Environment: Production Python virtual env
│
└── Database (Future)
    └── PostgreSQL / MongoDB for patient records
```

---

## Next Development Phase

1. **Phase 1: Core Enhancements**
   - [ ] Add PDF report generation
   - [ ] Implement patient data storage
   - [ ] Add prediction history

2. **Phase 2: User Management**
   - [ ] User registration/login
   - [ ] Role-based access (Doctor/Admin)
   - [ ] Session management

3. **Phase 3: Advanced Features**
   - [ ] Batch image processing
   - [ ] Comparison view (before/after)
   - [ ] Export to DICOM format
   - [ ] Email notifications

4. **Phase 4: Analytics**
   - [ ] Dashboard with statistics
   - [ ] Disease prevalence charts
   - [ ] Model performance tracking
   - [ ] Audit logs

---

**Architecture designed for scalability and maintainability** ✨
