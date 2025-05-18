import streamlit as st
from . import config 

class AppUI:
    def __init__(self, predictor):
        self.predictor = predictor
        st.set_page_config(page_title="Magic Predictor", layout="wide")

    def _display_home_page(self):
        st.image(config.DOCKER_HEADER_IMAGE_PATH, use_column_width=True)
        st.header('I AM A MAGICIAN! I CAN TELL YOU YOUR AGE, GENDER AND EMOTION ')
        st.subheader('Wanna see my magic...??!')
        
        uploaded_image = st.file_uploader('Drop Image here', type=['jpg', 'jpeg', 'png'])
        
        if uploaded_image is not None:
            st.image(uploaded_image, caption='Uploaded Image.', width=300)
            
            if st.button('Predict'):
                with st.spinner('Making predictions...'):
                    predictions = self.predictor.predict(uploaded_image)

                st.success(
                    f"**Age:** {predictions['age']}\n\n"
                    f"**Gender:** {predictions['gender']}\n\n"
                    f"**Emotion:** {predictions['emotion']}"
                )
    def _display_about_project_page(self):
        st.header('The Concept Behind Our Project')
        st.markdown("""
        In the realm of digitalization and automation, there's a growing need for intelligent systems that can discern and categorize objects accurately. One promising area where such systems can make a significant impact is in image-based analysis for predicting age, gender, and emotions. With advancements in technologies like Convolutional Neural Networks (CNNs) and Artificial Neural Networks (ANNs), we have the tools to develop sophisticated solutions for this purpose.

        Our project aims to utilize CNNs and ANNs to create an advanced Image Analysis System (IAS) capable of predicting age, gender, and emotions from images with precision and speed. By leveraging deep learning techniques, we intend to build a robust system that enhances our understanding of individuals' characteristics through visual data.

        **Key Objectives:**
        1. **Accuracy in Prediction:** Develop CNN-based models trained on diverse image datasets to achieve high accuracy in predicting age, gender, and emotions.
        2. **Real-time Analysis:** Implement algorithms optimized for real-time processing to swiftly analyze images and provide predictions.
        3. **Scalability:** Design the system architecture to accommodate future enhancements and adapt to different contexts.
        4. **User-Friendly Interface:** Create an intuitive interface for seamless interaction, ensuring ease of use for users.

        **Methodology:**
        Our approach involves stages such as data collection, preprocessing, model training, and deployment. We will curate a diverse dataset comprising images with varying characteristics to train our models effectively. Preprocessing techniques like normalization and resizing will enhance dataset quality. We'll then train multiple CNN and ANN models using frameworks like TensorFlow and PyTorch. Rigorous testing and validation will assess model performance metrics such as accuracy and precision.

        **Expected Outcomes:**
        Upon successful completion, we anticipate:
        1. **High Prediction Accuracy:** Achieve over 90% accuracy in predicting age, gender, and emotions from images.
        2. **Real-world Applicability:** Demonstrate the practical utility of our system in various contexts, showcasing its effectiveness in image-based analysis.
        3. **Scalability and Adaptability:** Establish a framework adaptable to different image-based prediction tasks and integration with existing systems.
        4. **User Acceptance:** Receive positive feedback from users, affirming the system's usability and value.

        In essence, our project pioneers the use of CNNs and ANNs for image-based analysis, with a focus on predicting age, gender, and emotions. By marrying advanced technology with practical applications, we aim to enhance understanding and efficiency in this domain.
        """)

    def _display_acknowledgement_page(self):
        st.header("Acknowledgments")
        st.markdown("""
        We would like to express our sincere gratitude to the following individuals and institutions for their invaluable contributions and support throughout the duration of this project:

        **Team Members:**
        - Abdelrahman Yasser Elseht
        - Abdelrahman Samir Elafify
        - Abdelrahman Mohammed Abdelaal
        - Abdelrahman Taher Mahmoud
        - Abdelrahman Attalah Yahia
        - Abdelrahman Mohammed Tolba
        - Abdullah Ebrahim Elseady

        **Supervising Doctor:**
        - Dr. Fatma Alzahraa Ahmed

        **Instructor:**
        - Sara Emara
        """)

    def run(self):
        st.sidebar.title('Hello')
        app_mode = st.sidebar.selectbox(
            'Select page',
            ('Home', 'About Project', 'Acknowledgement')
        )

        if app_mode == 'Home':
            self._display_home_page()
        elif app_mode == 'About Project':
            self._display_about_project_page()
        elif app_mode == 'Acknowledgement':
            self._display_acknowledgement_page()