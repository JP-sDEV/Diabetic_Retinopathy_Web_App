import streamlit as st
import tensorflow as tf
import requests
import numpy
from PIL import Image
from io import BytesIO
from helper_functions.preprocess import decode_img, preprocesser, format_input
from helper_functions.format_results import format_predictions


def app():

    st.markdown("""
                ## **Classification**
                
                ### Link to labelled instances ([link](https://www.kaggle.com/amanneo/diabetic-retinopathy-resized-arranged))
                """)

    path = st.text_input("Provide URL of DR Image for Classification",
                         "https://www.reviewofoptometry.com/CMSImagesContent/2019/05/DR1.jpg")

    with st.spinner("Loading Model..."):
        model = tf.keras.models.load_model("model")

    if path is not None:
        content = requests.get(path).content
        image = Image.open(BytesIO(content))

        # VISUALS
        col1, col2 = st.beta_columns(2)

        col1.subheader("Original Image")
        col1.image(image, use_column_width=True)

        raw_img_arr = decode_img(content)
        preprocessed_img = preprocesser(raw_img_arr)
        show_grayscale = preprocessed_img.numpy()

        col2.subheader("Preprocessed Image")
        col2.image(show_grayscale,
                   use_column_width=True)

        # CLASSIFICATION
        input_batch = format_input(preprocessed_img)
        with st.spinner('Predicting.....'):
            predictions = model.predict(
                input_batch)

            predictions_table = format_predictions(predictions[0])
            st.table(predictions_table)
