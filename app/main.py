import streamlit as st
from .predictor import Predictor
from .app_ui import AppUI
from . import config 

def main():
    @st.cache_resource
    def load_predictor_instance():
        try:
            predictor_instance = Predictor(
                age_model_path=config.DOCKER_AGE_MODEL_PATH,
                gender_model_path=config.DOCKER_GENDER_MODEL_PATH,
                expression_model_path=config.DOCKER_EXPRESSION_MODEL_PATH
            )
            return predictor_instance
        except Exception as e:
            st.error(f"CRITICAL: Failed to load models. Check paths and model integrity. Error: {e}")
            st.error(f"Age Model Path: {config.DOCKER_AGE_MODEL_PATH}")
            st.error(f"Gender Model Path: {config.DOCKER_GENDER_MODEL_PATH}")
            st.error(f"Expression Model Path: {config.DOCKER_EXPRESSION_MODEL_PATH}")
            st.stop()

    predictor = load_predictor_instance()
    
    if predictor:
        app = AppUI(predictor)
        app.run()

if __name__ == "__main__":
    main()