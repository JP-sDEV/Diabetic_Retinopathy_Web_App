import streamlit as st
import pandas as pd


def format_predictions(prediction_arr):
    """
    Format prediction array into a Pandas Dataframe with proper labels
      - prediction_arr index corresponds to class
    """
    proper_labels = [
        "No DR (0)",
        "Mild (1)",
        "Moderate (2)",
        "Severe (3)",
        "Proliferative DR (4)"
    ]

    formatted = {
        "Condition": proper_labels,
        "Probability": prediction_arr * 100
    }

    df = pd.DataFrame(formatted)
    formatted_df = df.style.highlight_max(axis=0, color='darkorange')
    return formatted_df
