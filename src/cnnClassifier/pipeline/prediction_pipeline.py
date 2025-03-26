import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        
        
    def prediction(self):
        model=  load_model(r"C:\Users\VAIBHAVRAI\OneDrive\Desktop\kidney_project\kd_pr\artifacts\training\model.h5")
        imagename = self.filename
        test_image =  image.load_img(imagename, target_size= (224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result  = np.argmax(model.predict(test_image), axis =1 )    
        print(result)
        
        if result[0] ==1:
            prediction = 'Tumor'
            return [{"Given image has": prediction}]
        
        else:
            prediction = 'Normal'
            return [{"Given image is ": prediction}]