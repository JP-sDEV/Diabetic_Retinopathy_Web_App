import streamlit as st
from multiapp import MultiApp
# import your app modules here
from apps import about, classification, data

app = MultiApp()
st.set_page_config(page_title="DR Classifier", page_icon=":eyes:")

st.markdown("""
# Diabetic Retinopathy Classifier
""")

# Add all your application here
app.add_app("Classification", classification.app)
app.add_app("Dataset", data.app)
app.add_app("About", about.app)
# The main app
app.run()
