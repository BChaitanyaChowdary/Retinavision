"""
Convert old Keras model to new format compatible with TensorFlow 2.15
Run this locally, then upload the new model
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np

def convert_model():
    """Convert old model to new format"""
    print("Loading old model...")
    
    try:
        # Try to load with older method
        model = keras.models.load_model('my_modeltrained3.h5', compile=False)
        print("✅ Model loaded successfully")
        
        # Get model architecture
        print("\nModel Summary:")
        model.summary()
        
        # Save in new format
        print("\nSaving in new format...")
        model.save('my_modeltrained3_new.h5', save_format='h5')
        print("✅ Model saved as my_modeltrained3_new.h5")
        
        # Also save in SavedModel format (more compatible)
        print("\nSaving in SavedModel format...")
        model.save('my_modeltrained3_savedmodel')
        print("✅ Model saved as my_modeltrained3_savedmodel/")
        
        print("\n✅ Conversion complete!")
        print("\nNext steps:")
        print("1. Replace 'my_modeltrained3.h5' with 'my_modeltrained3_new.h5'")
        print("2. Or use the SavedModel format (recommended)")
        print("3. Commit and push to GitHub")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nTrying alternative method...")
        
        # Alternative: Rebuild model from scratch
        print("Model needs to be retrained with current TensorFlow version")
        print("The model architecture uses deprecated parameters")

if __name__ == '__main__':
    convert_model()
