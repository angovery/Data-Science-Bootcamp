# Pages/3_Clasificacion.py
import streamlit as st
import pandas as pd
import joblib

# Se carga el modelo y el label_encoder en la caché, para minimizar tiempos de espera en consultas posteriores.
@st.cache_resource(show_spinner='Cargando el modelo de clasificación...')
def load_classification_label_model():
    model = joblib.load("Models/pipeline_clasificacion.joblib")
    label_encoder = joblib.load("Models/label_encoder_clasificacion.joblib")
    return model, label_encoder

modelo_clasificacion, label_encoder = load_classification_label_model()

st.title("Predicción de Cut - Clasificación")
st.markdown("Ingresa los datos para predecir la calidad de corte (cut) del diamante.")

# Se definen el rango de valores de entrada para las variables numéricas.
carat = st.number_input("Carat", min_value=0.0, value=0.5, step=0.01)
depth = st.number_input("Depth", min_value=0.0, value=60.0, step=0.1)
table = st.number_input("Table", min_value=0.0, value=55.0, step=0.1)
x = st.number_input("x", min_value=0.0, value=5.0, step=0.1)
y = st.number_input("y", min_value=0.0, value=5.0, step=0.1)
z = st.number_input("z", min_value=0.0, value=3.0, step=0.1)

# Valores posibles de las variables categóricas ordinales.
color_options = ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
clarity_options = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF', 'FL']

# Se genera el box de selección para las variables categóricas ordinales.
color = st.selectbox("Color", color_options)
clarity = st.selectbox("Clarity", clarity_options)

if st.button("Predecir corte"):
    # Se genera el DataFrame con los datos de entrada.
    input_data = pd.DataFrame({
        'carat': [carat],
        'depth': [depth],
        'table': [table],
        'x': [x],
        'y': [y],
        'z': [z],
        'color': [color],
        'clarity': [clarity]
    })
    # Se genera la predicción.
    prediccion = modelo_clasificacion.predict(input_data)
    # Se decodifica el valor numérico de la prediccióm para mostrar el valor asociado de los posibles valores de la variable.
    etiqueta_predicha = label_encoder.inverse_transform(prediccion)
    # Mostrar el resultado.
    st.metric("El corte predicho es:", etiqueta_predicha[0])