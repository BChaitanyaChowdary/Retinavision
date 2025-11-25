"""
Fix model compatibility for TensorFlow 2.15
This script loads the old model and saves it in a compatible format
"""

import tensorflow as tf
from tensorflow import keras
import sys

def fix_model():
    """Load and resave model in compatible format"""
    
    model_path = 'my_modeltrained3.h5'
    output_path = 'my_modeltrained3_fixed.h5'
    
    print(f"TensorFlow version: {tf.__version__}")
    print(f"Loading model from: {model_path}")
    
    try:
        # Method 1: Try standard load
        print("\n[1/4] Trying standard load...")
        model = keras.models.load_model(model_path, compile=False)
        print("✅ Standard load successful!")
        
    except Exception as e1:
        print(f"❌ Standard load failed: {str(e1)[:100]}")
        
        try:
            # Method 2: Load with custom objects
            print("\n[2/4] Trying with custom objects...")
            from tensorflow.keras.layers import InputLayer
            
            model = keras.models.load_model(
                model_path,
                compile=False,
                custom_objects={'InputLayer': InputLayer}
            )
            print("✅ Custom objects load successful!")
            
        except Exception as e2:
            print(f"❌ Custom objects failed: {str(e2)[:100]}")
            
            try:
                # Method 3: Load weights only and rebuild
                print("\n[3/4] Trying to load weights only...")
                
                # Create a new model with same architecture
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
                    keras.layers.Dense(8, activation='softmax')
                ])
                
                # Try to load weights
                model.load_weights(model_path)
                print("✅ Weights loaded successfully!")
                
            except Exception as e3:
                print(f"❌ All methods failed!")
                print(f"\nError details: {e3}")
                print("\n" + "="*60)
                print("SOLUTION: The model needs to be retrained with TensorFlow 2.15")
                print("="*60)
                return False
    
    # Model loaded successfully, now save in compatible format
    print("\n[4/4] Saving model in compatible format...")
    
    # Print model info
    print("\nModel Summary:")
    model.summary()
    
    print(f"\nInput shape: {model.input_shape}")
    print(f"Output shape: {model.output_shape}")
    print(f"Number of layers: {len(model.layers)}")
    
    # Save in new format
    print(f"\nSaving to: {output_path}")
    model.save(output_path, save_format='h5')
    
    print("\n" + "="*60)
    print("✅ SUCCESS! Model converted successfully!")
    print("="*60)
    print(f"\nNew model saved as: {output_path}")
    print(f"\nNext steps:")
    print(f"1. Delete old model: del {model_path}")
    print(f"2. Rename new model: ren {output_path} {model_path}")
    print(f"3. Push to GitHub: git add {model_path} && git commit -m 'Fix model' && git push")
    print("="*60)
    
    return True

if __name__ == '__main__':
    success = fix_model()
    sys.exit(0 if success else 1)
