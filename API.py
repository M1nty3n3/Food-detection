from keras import preprocessing, models
import numpy as np
import warnings

warnings.filterwarnings('ignore')
model = models.load_model('Food_detection_model.h5')

def model_predictions(image_path, model):
    img = preprocessing.image.load_img(image_path, target_size=(256, 256))
    img_array = preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array/255.0

    predict = np.argmax(model.predict(img_array))
        
    return str(predict)