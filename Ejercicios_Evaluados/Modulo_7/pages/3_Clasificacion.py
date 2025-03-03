# Pages/3_Clasificacion.py
import streamlit as st
st.set_page_config(page_title="Modelo de Clasificación - Diamonds", layout="wide")
import pandas as pd
import joblib

# Carga del DataSet.
ruta = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/diamonds.csv'

# Se carga el modelo y el label_encoder en la caché, para minimizar tiempos de espera en consultas posteriores.
@st.cache_resource(show_spinner='Cargando el modelo de clasificación...')
def load_data_clasificacion():
    model = joblib.load("Models/pipeline_clasificacion.joblib")
    label_encoder = joblib.load("Models/label_encoder_clasificacion.joblib")
    df = pd.read_csv(ruta)
    return model, label_encoder, df

modelo_clasificacion, label_encoder, df = load_data_clasificacion()

if st.button('Volver a inicio'): # opcional poder volver a inicio
    st.switch_page('Inicio.py')

st.title("Predicción de Cut - Clasificación")
st.markdown("Ingresa los datos para predecir la calidad de corte (cut) del diamante.")

with st.container(border=True):
    st.write ("Variables numéricas de forma.")
    col1, col2, col3 = st.columns(3)
    # Se definen el rango de valores de entrada para las variables numéricas.
    with col1:
        carat = st.number_input("Carat", min_value=0.0, value=df['carat'].mean(), step=0.01) # Se muestra, por defecto, el valor medio de la columna.
    with col2: 
        depth = st.number_input("Depth", min_value=0.0, value=df['depth'].mean(), step=0.1) # Se muestra, por defecto, el valor medio de la columna.
    with col3:
        table = st.number_input("Table", min_value=0.0, value=df['table'].mean(), step=0.1) # Se muestra, por defecto, el valor medio de la columna.

with st.container(border=True):
    st.write ("Variables numéricas de tamaño.")
    col1, col2, col3 = st.columns(3)
    # Se genera el box de selección para las variables numéricas.
    with col1:
        x = st.number_input("x", min_value=0.0, value=df['x'].mean(), step=0.1)
    with col2:
        y = st.number_input("y", min_value=0.0, value=df['y'].mean(), step=0.1)
    with col3:
        z = st.number_input("z", min_value=0.0, value=df['z'].mean(), step=0.1)

# Valores posibles de las variables categóricas ordinales.
color_options = ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
clarity_options = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF', 'FL']

with st.container(border=True):
    st.write("Variables categóricas ordinales.")
    col1, col2 = st.columns(2)
    # Se genera el box de selección para las variables categóricas ordinales.
    with col1:
        color = st.selectbox("Color", color_options)
    with col2:
        clarity = st.selectbox("Clarity", clarity_options)

if st.button("Predecir corte"):
    # Se genera el DataFrame con los datos de entrada.
    input_data = pd.DataFrame({
        'carat': [carat],
        'color': [color],
        'clarity': [clarity],
        'depth': [depth],
        'table': [table],
        'x': [x],
        'y': [y],
        'z': [z],   
    })
    # Se genera la predicción.
    prediccion = modelo_clasificacion.predict(input_data)
    # Se decodifica el valor numérico de la prediccióm para mostrar el valor asociado de los posibles valores de la variable.
    etiqueta_predicha = label_encoder.inverse_transform(prediccion)
    # Mostrar el resultado.
    st.metric("El corte predicho es:", etiqueta_predicha[0])