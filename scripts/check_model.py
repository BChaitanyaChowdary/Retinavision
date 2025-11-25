import os
import sys
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

BASE = os.path.dirname(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE, 'my_modeltrained3.h5')
TEST_DIR = os.path.join(BASE, 'test_images')

print('Python', sys.version)
print('TF', tf.__version__)
print('Model path', MODEL_PATH)

if not os.path.exists(MODEL_PATH):
    print('Model file not found:', MODEL_PATH)
    sys.exit(1)

try:
    model = tf.keras.models.load_model(MODEL_PATH, compile=False)
    print('Loaded model')
    model.summary()
    try:
        print('model.input_shape =', model.input_shape)
    except Exception:
        pass
except Exception as e:
    print('Failed to load model:', e)
    sys.exit(1)

# Determine target size from model if available
try:
    target_h, target_w = int(model.input_shape[1]), int(model.input_shape[2])
    print('Using model input size for loading images:', (target_h, target_w))
except Exception:
    target_h, target_w = 128, 128
    print('Falling back to default target size:', (target_h, target_w))

# Load up to 5 images
imgs = []
if os.path.isdir(TEST_DIR):
    for f in os.listdir(TEST_DIR)[:5]:
        p = os.path.join(TEST_DIR, f)
        try:
            img = image.load_img(p, target_size=(target_h, target_w))
            x = image.img_to_array(img)
            imgs.append((f, x))
            print('Loaded', f)
        except Exception as e:
            print('Could not load', f, e)

if not imgs:
    print('No test images found; using random images')
    for i in range(3):
        imgs.append((f'random_{i}.png', np.random.randint(0,256,(224,224,3), dtype=np.uint8)))

X = np.stack([x for _, x in imgs]).astype('float32')

def run_with_preprocessing(X, kind='mobilenetv2'):
    Xf = X.copy().astype('float32')
    try:
        if kind == 'mobilenetv2':
            from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
            Xp = preprocess_input(Xf)
        elif kind == 'efficientnet':
            from tensorflow.keras.applications.efficientnet import preprocess_input
            Xp = preprocess_input(Xf)
        else:
            Xp = Xf / 255.0
        print(f'Used preprocess: {kind}')
    except Exception as e:
        Xp = Xf / 255.0
        print(f'Preprocess {kind} failed, falling back to /255: {e}')

    preds = model.predict(Xp)
    print('preds shape', preds.shape)
    for (name, _), p in zip(imgs, preds):
        print(f'[{kind}]', name, '-> argmax', int(np.argmax(p)), 'vals (first 8):', np.round(p[:8],4))
    print(f'[{kind}] Row sums (softmax?)', np.round(preds.sum(axis=1),4))
    return preds

# Test multiple preprocessing options
preds_mn = run_with_preprocessing(X, 'mobilenetv2')
preds_en = run_with_preprocessing(X, 'efficientnet')
preds_simple = run_with_preprocessing(X, 'simple')

# Also try raw inputs (no preprocessing) as a quick check
try:
    preds_raw = model.predict(X / 255.0)
    print('Preds on X/255 shape', preds_raw.shape)
    for (name, _), p in zip(imgs, preds_raw):
        print(name, 'RAW -> argmax', int(np.argmax(p)), 'vals (first 8):', np.round(p[:8],4))
    print('Preds on X/255 sums', np.round(preds_raw.sum(axis=1),4))
except Exception as e:
    print('Could not run raw predict:', e)

# Additional quick checks: random noise and constant images to detect collapse
print('\n--- Additional checks: random and constant inputs ---')
rand_imgs = np.random.randint(0,256,(10, target_h, target_w, 3), dtype=np.uint8).astype('float32') / 255.0
preds_rand = model.predict(rand_imgs)
print('Random inputs argmax counts:', np.bincount(np.argmax(preds_rand, axis=1), minlength=preds_rand.shape[1]))

zeros = np.zeros((3, target_h, target_w, 3), dtype=np.float32)
preds_zeros = model.predict(zeros)
print('Zeros inputs argmax:', np.argmax(preds_zeros, axis=1), 'vals (first):', np.round(preds_zeros[0][:8],4))

ones = np.ones((3, target_h, target_w, 3), dtype=np.float32)
preds_ones = model.predict(ones)
print('Ones inputs argmax:', np.argmax(preds_ones, axis=1), 'vals (first):', np.round(preds_ones[0][:8],4))
