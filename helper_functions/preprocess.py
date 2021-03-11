import tensorflow as tf
import numpy as np
import tensorflow_addons as tfa


def decode_img(res):
    """
    Converts a request response into an image, applying the following modifications
     - load image as a grayscale image (channels=1)
     - resizing to 224x224
     - equalizes image histogram
    """
    image = tf.image.decode_jpeg(res, channels=1)
    image = tf.image.resize(image, [224, 224])

    return image


def preprocesser(image_arr):
    """
    Preprocesses image array from decode_img
      - equalize pixel intensity distribution
      - normalizes pixel intensities (range from 0 to 1)
    """
    image_adj = tfa.image.equalize(image_arr)
    image_adj /= 255

    return image_adj


def format_input(image_arr):
    """
    Format grayscale image for model input layer
      - (224,224,1) -> (1,224,224,3)
    """
    input_arr = np.squeeze(np.stack((image_arr,)*3, axis=-1))
    input_arr = np.array([input_arr])  # Convert single image to a batch.

    return input_arr
