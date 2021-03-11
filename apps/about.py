import streamlit as st


def app():

    st.markdown("""
                ## **About**

                ## What is Diabetic Retinopathy?

                Diabetic Retinopathy(DR) is an eye disease caused by diabetes effecting 21 % of patients with type 2 diabetes. The blood vessels in the eye become damaged affecting the retina. As DR progresses into it's final stages, the chances of vision loss increase, therefore early detection of the disease is important to prevent/treat the progression of DR. ![Key Indicators of Diabetic Retinopathy](https://www.retinamd.com/Customer-Content/www/CMS/files/diabetic-retinopathy.jpg)

                ### Physical Indicators of DR

                Some clear indicators of DR are the patches seen around the blood vessels, as well as the bright outlines of the blood vessels.

                **Disclaimer**: I am not a professional nor licensed to diagnose/treat diabetic retinopathy. I am simply using machine learning to detect diabetic retinopathy based on it's physical features.

                ## Classifying Diabetic Retinopathy with Machine Learning

                ### What Model is Used?

                MobileNetV2 will be used to classify the differing stages/levels of diabetic retinopathy via [transfer learning](https://en.wikipedia.org/wiki/Transfer_learning).

                ### Why MobileNetV2?
                MobileNetV2 is used because it's light weight(faster training, and loading), while still being accurate relative to deeper models.
                
                ### MobileNetV2 Architecture
                ![MobileNetV2 Architecture](https://miro.medium.com/max/499/1*f29Ku3IxE5POo6zq0KG88w.png)
                
                More on [MobileNetV2](https://arxiv.org/abs/1801.04381)

                ### Model Parameters

                |Training Parameter  | Value |
                |--|--|
                | Number of Epochs | 50 |
                | Learning Rate| 0.001 |
                | Loss Function | Categorical Crossentropy |
                | Optimizer | Adam |

                ## Training Process

                Each image went through a preprocessing function that did the following:

                1. convert into a grayscale image(1 channel image)
                2. resize into 224x224
                3. adjust contrast via histogram equalization
                4. normalize pixel intensity values(from 0 to 1)

                The full model and training parameters can be found in the "Model Parameters" section above.

                ### Training Results

                | Set| Metric | Result | 
                |--|--|--|
                | Training | Accuracy | 0.9286 |
                | | Loss | 0.4294 |
                | Validation| Accuracy | 0.6017 |
                | | Loss | 6.6678 |
                | Testing | Accuracy | 0.6086 |
                | | Loss | 3.9230 |

                - Accuracy — higher is better
                - Loss — lower is better

                ## Technologies Used
                - [Keras](https://keras.io/)
                - [TensorFlow](https://www.tensorflow.org/)
                - [Scikit-learn](https://scikit-learn.org/stable/)
                - [Numpy](https://numpy.org/)

                ## [Full Notebook](https://github.com/JP-sDEV/Diabetic-Retinopathy-Classification)
                """)
