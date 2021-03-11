import streamlit as st


def app():

    st.markdown("""
                ## **Dataset**

                ## **Original Dataset ([link](https://www.kaggle.com/amanneo/diabetic-retinopathy-resized-arranged))**

                The dataset used to train and validate the model can be found on Kaggle. The original images have differing sizes, all have 3 color channels (RGB), and are all formatted as JPEGs.

                ### Selecting an Image to Put into the Classifier

                1. Go to the original dataset link
                2. Find a folder with the desired condition
                3. Find sample within respective folder
                4. Enlarge sample by left clicking it
                5. Right click enlarged image ⇒ "Copy image address"
                6. Paste link into classifier
                7. Hit enter to get prediction

                **Credit to the author of the original dataset**
                """)
