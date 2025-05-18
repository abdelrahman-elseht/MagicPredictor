import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from . import config 

class Predictor:
    def __init__(self, age_model_path, gender_model_path, expression_model_path):
        try:
            self.age_model = load_model(age_model_path, compile=False)
            self.gender_model = load_model(gender_model_path, compile=False)
            self.expression_model = load_model(expression_model_path, compile=False)
            print("Models loaded successfully.")
        except Exception as e:
            print(f"Error loading models from paths: {age_model_path}, {gender_model_path}, {expression_model_path}. Error: {e}")
            raise

        self.gender_classes = config.GENDER_CLASSES
        self.emotions_classes = config.EMOTIONS_CLASSES
        self.age_classes = config.AGE_CLASSES

    def _preprocess_for_age_gender(self, image_path_or_buffer):
        image = load_img(image_path_or_buffer, target_size=(96, 96))
        image_array = img_to_array(image)
        return image_array.reshape(1, 96, 96, 3) / 255.0

    def _preprocess_for_expression(self, image_path_or_buffer):
        img_orig = load_img(image_path_or_buffer, color_mode="grayscale", target_size=(48,48)) # Load directly as grayscale and resize
        img_array = img_to_array(img_orig) # Shape (48, 48, 1)
        return np.expand_dims(img_array / 255.0, axis=0) # Shape (1, 48, 48, 1)


    def _map_age_to_class(self, raw_age_prediction):
        age_val = int(raw_age_prediction)
        if 0 <= age_val <= 3: return self.age_classes[0]
        elif 4 <= age_val <= 7: return self.age_classes[1]
        elif 8 <= age_val <= 14: return self.age_classes[2]
        elif 15 <= age_val <= 21: return self.age_classes[3]
        elif 22 <= age_val <= 29: return self.age_classes[4]
        elif 30 <= age_val <= 37: return self.age_classes[5]
        elif 38 <= age_val <= 43: return self.age_classes[6]
        elif 44 <= age_val <= 47: return self.age_classes[7]
        elif 48 <= age_val <= 53: return self.age_classes[8]
        elif 54 <= age_val <= 65: return self.age_classes[9]
        elif age_val >= 66: return self.age_classes[10]
        else: return "Unknown Age"

    def predict(self, image_path_or_buffer):
        processed_img_age_gender = self._preprocess_for_age_gender(image_path_or_buffer)
        age_prediction_raw = self.age_model.predict(processed_img_age_gender)[0][0]
        age_prediction_class = self._map_age_to_class(age_prediction_raw)

        gender_prediction_raw = self.gender_model.predict(processed_img_age_gender)
        gender_index = int(np.round(gender_prediction_raw[0][0]))
        gender_prediction_class = self.gender_classes[min(gender_index, len(self.gender_classes)-1)] # Ensure index is valid

        processed_img_expression = self._preprocess_for_expression(image_path_or_buffer)
        expression_prediction_raw = self.expression_model.predict(processed_img_expression)
        emotion_index = np.argmax(expression_prediction_raw)
        expression_prediction_class = self.emotions_classes[emotion_index]
        
        return {
            "age": age_prediction_class,
            "gender": gender_prediction_class,
            "emotion": expression_prediction_class
        }