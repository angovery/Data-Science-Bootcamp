import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Se carga el modelo y el label_encoder en la caché, para minimizar tiempos de espera en consultas posteriores.
@st.cache_resource(show_spinner='Cargando el modelo de regresión...')
def load_regression_model():
    model = joblib.load("Models/pipeline_regresion.joblib")
    return model

modelo_regresion = load_regression_model()

st.title("Predicción de Precio - Regresión")
st.markdown("Ingresa los datos para predecir el precio del diamante.")

# Se definen el rango de valores de entrada para las variables numéricas.
carat = st.number_input("Carat", min_value=0.0, value=0.5, step=0.01)
depth = st.number_input("Depth", min_value=0.0, value=60.0, step=0.1)
table = st.number_input("Table", min_value=0.0, value=55.0, step=0.1)
x = st.number_input("x", min_value=0.0, value=5.0, step=0.1)
y = st.number_input("y", min_value=0.0, value=5.0, step=0.1)
z = st.number_input("z", min_value=0.0, value=3.0, step=0.1)

# Valores posibles de las variables categóricas ordinales.
cut_options = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
color_options = ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
clarity_options = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF', 'FL']

# Se genera el box de selección para las variables categóricas ordinales.
cut = st.selectbox("Cut", cut_options)
color = st.selectbox("Color", color_options)
clarity = st.selectbox("Clarity", clarity_options)

if st.button("Predecir Precio"):
    # Se genera el DataFrame con los datos de entrada.
    input_data = pd.DataFrame({
        'carat': [carat],
        'depth': [depth],
        'table': [table],
        'x': [x],
        'y': [y],
        'z': [z],
        'cut': [cut],
        'color': [color],
        'clarity': [clarity]
    })
    # Se genera la predicción.
    prediccion = modelo_regresion.predict(input_data)
    st.metric(label="Predicción del precio", value=np.round(prediccion[0], 2))