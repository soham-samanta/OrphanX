from tensorflow import keras
from tensorflow.keras.models import load_model
import numpy as np
import cv2
from keras_vggface.utils import preprocess_input


model = load_model('vgg_face.h5')
#model.summary()
test_path = "input/test/"

def read_img(path):
    img = cv2.imread(path)
    img = np.array(img).astype(np.float64)
    return preprocess_input(img, version=2)


"""
face00443 child chinese
face00426 parent chinese
face00438 parent black
"""
X1 = test_path + "face00443.jpg"
X1 = np.array([read_img(X1)])

X2 = test_path + "face00315.jpg"
X2 = np.array([read_img(X2)])

pred = model.predict([X1, X2])
print(pred)