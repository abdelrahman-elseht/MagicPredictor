import os

# Base directory of the app module
APP_DIR = os.path.dirname(os.path.abspath(__file__))
# Project root directory (one level up from app/)
PROJECT_ROOT = os.path.dirname(APP_DIR)

# Model paths

AGE_MODEL_PATH = os.path.join(PROJECT_ROOT, 'models', 'kaggle_age_model.h5')
GENDER_MODEL_PATH = os.path.join(PROJECT_ROOT, 'models', 'kaggle_gender_model.h5')
EXPRESSION_MODEL_PATH = os.path.join(PROJECT_ROOT, 'models', 'expressions.h5')

# Asset paths
HEADER_IMAGE_PATH = os.path.join(PROJECT_ROOT, 'assets', 'magic_header-1680x462.jpg')



# These paths will be used by the application *inside* the Docker container.
DOCKER_AGE_MODEL_PATH = '/app/models/kaggle_age_model.h5'
DOCKER_GENDER_MODEL_PATH = '/app/models/kaggle_gender_model.h5'
DOCKER_EXPRESSION_MODEL_PATH = '/app/models/expressions.h5'
DOCKER_HEADER_IMAGE_PATH = '/app/assets/magic_header-1680x462.jpg'


# Class names 
GENDER_CLASSES = ['Man', 'Woman']
EMOTIONS_CLASSES = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprised']
AGE_CLASSES = [
    '(0-3)', '(4-7)', '(8-14)', '(15-21)', '(22-29)',
    '(30-37)', '(38-43)', '(44-47)', '(48-53)', '(54-65)', '(66-100)'
]