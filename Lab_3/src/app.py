import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json
import os


# Функция для загрузки модели

def load_model():
    with open('src/iris_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model


model = load_model()


st.title('Iris Species Prediction')
st.write('Please upload a JSON file containing Iris features for prediction')


# Загрузка файла пользователем
uploaded_file = st.file_uploader('Choose a JSON file', type=['json'])
if uploaded_file is not None:

    data = json.load(uploaded_file)

    df = pd.DataFrame

    try:
        prediction = model.predict(df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])
        st.write('Pedicted Iris species', prediction[0])
    except Exception as e:
        st.error(f'Error in Prediction: {e}')
    finally:
        uploaded_file.seek(0)

