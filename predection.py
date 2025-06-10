import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
    
    def predict(self):
        # load model
        model = load_model(os.path.join("model", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        # Map the class indices to their names
        class_names = {
            0: 'Cyst',  # Replace with your actual class names
            1: 'Normal',
            2: 'Stone',
            3: 'Tumor'
        }
        
        prediction = class_names.get(result[0], 'Unknown')
        return [{"image": prediction}]