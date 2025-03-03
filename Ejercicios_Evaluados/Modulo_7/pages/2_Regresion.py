import streamlit as st
st.set_page_config(page_title="Modelo de Regresión - Diamonds", layout="wide")
import pandas as pd
import joblib
import numpy as np

if 'df' not in st.session_state:
    st.error('El DataFrame no se encuentra disponible. por favor, vuelve a cargar la página de Inicio.')
else:
    df = st.session_state['df'] # Carga del DataSet.
    
    # Se carga el modelo y el label_encoder en la caché, para minimizar tiempos de espera en consultas posteriores.
    @st.cache_resource(show_spinner='Cargando el modelo de regresión...')
    def load_data_regresion():
        model = joblib.load("Models/pipeline_regresion.joblib")
        return model

    modelo_regresion = load_data_regresion()

    if st.button('Volver a inicio'): # opcional poder volver a inicio
        st.switch_page('Inicio.py')

    st.title("Predicción de Precio - Regresión")
    st.markdown("Ingresa los datos para predecir el precio del diamante.")

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
    cut_options = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
    color_options = ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    clarity_options = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF', 'FL']

    with st.container(border=True):
        st.write("Variables categóricas ordinales.")
        col1, col2, col3 = st.columns(3)
        # Se genera el box de selección para las variables categóricas ordinales.
        with col1:
            cut = st.selectbox("Cut", cut_options)
        with col2:
            color = st.selectbox("Color", color_options)
        with col3:
            clarity = st.selectbox("Clarity", clarity_options)
        
    if st.button("Predecir Precio"):
        # Se genera el DataFrame con los datos de entrada.
        datos_entrada = pd.DataFrame({
            'carat': [carat],
            'cut': [cut],
            'color': [color],
            'clarity': [clarity],
            'depth': [depth],
            'table': [table],
            'x': [x],
            'y': [y],
            'z': [z]
        })
        # Se genera la predicción.
        prediccion = modelo_regresion.predict(datos_entrada)
        st.metric(label="Predicción del precio", value=str(np.round(prediccion[0], 2)) + '$', delta=str(np.round(((prediccion[0] - df['price'].mean()) / df['price'].mean()) * 100, 2)) + "%",delta_color='normal')
        st.write('(Se muestra el porcentaje relativo con respecto al precio medio. Precio medio: ', np.round(df['price'].mean(), 2), '$)')