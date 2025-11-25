# 🔧 Model Loading Fix Guide

## Issue: Model Compatibility Error

Your model was trained with an older version of Keras that uses `batch_shape` parameter, which is not compatible with TensorFlow 2.15.

**Error**: `Unrecognized keyword arguments: ['batch_shape']`

---

## ✅ Solution Options:

### Option 1: Convert Model Locally (Recommended)

**If you have the original training environment:**

1. **Run the conversion script**:
   ```bash
   cd backend
   python convert_model.py
   ```

2. **Replace the model file**:
   ```bash
   # Backup old model
   mv my_modeltrained3.h5 my_modeltrained3_old.h5
   
   # Use new model
   mv my_modeltrained3_new.h5 my_modeltrained3.h5
   ```

3. **Commit and push**:
   ```bash
   git add backend/my_modeltrained3.h5
   git commit -m "Update model to TensorFlow 2.15 compatible format"
   git push origin main
   ```

### Option 2: Retrain Model (Best Long-term Solution)

**Retrain with current TensorFlow 2.15:**

```python
import tensorflow as tf
from tensorflow import keras

# Your model architecture
model = keras.Sequential([
    keras.layers.InputLayer(input_shape=(128, 128, 3)),  # Use input_shape, not batch_shape
    # ... rest of your layers
])

# Compile and train
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))

# Save in compatible format
model.save('my_modeltrained3.h5', save_format='h5')
```

### Option 3: Use SavedModel Format

**Convert to SavedModel (more compatible):**

```python
# Load old model (if possible)
model = keras.models.load_model('my_modeltrained3.h5', compile=False)

# Save in SavedModel format
model.save('my_modeltrained3_savedmodel')

# Update app.py to load SavedModel
# MODEL_PATH = 'my_modeltrained3_savedmodel'
```

### Option 4: Deploy Without Model (Temporary)

**The app currently works without the model:**
- ✅ Database operations work
- ✅ Patient management works
- ✅ Statistics work
- ❌ Predictions won't work (will return error)

This allows you to:
1. Deploy and test other features
2. Fix the model locally
3. Update and redeploy

---

## 🔍 Detailed Steps for Option 1:

### Step 1: Setup Local Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install tensorflow==2.15.0 keras numpy
```

### Step 2: Run Conversion

```bash
cd backend
python convert_model.py
```

**Expected Output**:
```
Loading old model...
✅ Model loaded successfully

Model Summary:
[model architecture]

Saving in new format...
✅ Model saved as my_modeltrained3_new.h5

Saving in SavedModel format...
✅ Model saved as my_modeltrained3_savedmodel/

✅ Conversion complete!
```

### Step 3: Test New Model

```python
# Test loading
import tensorflow as tf

model = tf.keras.models.load_model('my_modeltrained3_new.h5')
print("✅ Model loads successfully!")

# Test prediction
import numpy as np
test_input = np.random.rand(1, 128, 128, 3)
prediction = model.predict(test_input)
print(f"✅ Prediction works! Shape: {prediction.shape}")
```

### Step 4: Deploy

```bash
# Replace old model
mv my_modeltrained3.h5 my_modeltrained3_old.h5
mv my_modeltrained3_new.h5 my_modeltrained3.h5

# Commit and push
git add my_modeltrained3.h5
git commit -m "Update model to compatible format"
git push origin main
```

Render will automatically redeploy with the new model!

---

## 🚨 If Conversion Fails:

### The model might be too old to convert

**You'll need to retrain:**

1. **Get your training data**
2. **Use the training script with TensorFlow 2.15**
3. **Save in new format**

**Example training script**:

```python
import tensorflow as tf
from tensorflow import keras
import numpy as np

# Load your data
# X_train, y_train, X_val, y_val = load_data()

# Define model (update architecture as needed)
model = keras.Sequential([
    keras.layers.InputLayer(input_shape=(128, 128, 3)),
    keras.layers.Conv2D(32, (3, 3), activation='relu'),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.Flatten(),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(8, activation='softmax')  # 8 classes
])

# Compile
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_data=(X_val, y_val)
)

# Save
model.save('my_modeltrained3.h5', save_format='h5')
print("✅ Model saved in compatible format!")
```

---

## 📊 Check Model Status:

### Via API:

```bash
# Check root endpoint
curl https://retinavision.onrender.com/

# Response will show:
{
  "model_loaded": false,  # or true
  "model_status": "needs_conversion",  # or "ready"
  "note": "Model requires conversion - see convert_model.py"
}
```

### Via Logs:

Look for in Render logs:
```
✅ Model loaded successfully  # Good!
or
❌ MODEL LOADING FAILED  # Needs fix
```

---

## 🎯 Quick Fix Checklist:

- [ ] Download model file locally
- [ ] Install TensorFlow 2.15
- [ ] Run convert_model.py
- [ ] Test new model loads
- [ ] Replace old model file
- [ ] Commit and push to GitHub
- [ ] Verify deployment logs show "Model loaded successfully"
- [ ] Test prediction endpoint

---

## 💡 Prevention for Future:

### Always use compatible model saving:

```python
# Good - Compatible format
model.save('model.h5', save_format='h5')

# Better - SavedModel format
model.save('model_savedmodel')

# Best - Include version info
model.save(f'model_tf{tf.__version__}.h5')
```

### Document your environment:

```bash
# Save exact versions
pip freeze > requirements_training.txt

# Include TensorFlow version in model name
# model_tf2.15.0.h5
```

---

## 🆘 Still Having Issues?

1. **Check TensorFlow version**:
   ```python
   import tensorflow as tf
   print(tf.__version__)  # Should be 2.15.0
   ```

2. **Verify model file**:
   ```bash
   ls -lh backend/my_modeltrained3.h5
   # Should be ~50-200MB
   ```

3. **Check model architecture**:
   ```python
   model = tf.keras.models.load_model('model.h5')
   model.summary()
   ```

4. **Contact for help**:
   - Check GitHub issues
   - Review training code
   - Verify data preprocessing

---

**Note**: The app will continue to work for all features except predictions until the model is fixed. This allows you to test and use other functionality while resolving the model issue.
