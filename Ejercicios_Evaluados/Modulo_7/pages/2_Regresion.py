import streamlit as st
st.set_page_config(page_title="Modelo de Regresión - Diamonds", layout="wide")
import pandas as pd
import numpy as np
import os

if 'prediccion_reg_generada' not in st.session_state:
    st.session_state['prediccion_reg_generada'] = False         # Se inicializa la variable que controla si se ha realizado alguna predicción en la sesión actual.
  
if 'df' not in st.session_state:
    st.error('El DataFrame no se encuentra disponible. por favor, vuelve a cargar la página de Inicio.')
else:
    df = st.session_state['df'] # Carga del DataSet.
    
    if 'model_reg' not in st.session_state:
        st.error('El modelo de regresión no se encuentra disponible. por favor, vuelve a cargar la página de Inicio.')
    else:    
        # Se carga el modelo de la caché, para minimizar tiempos de espera en consultas posteriores.
        modelo_regresion = st.session_state['model_reg']
    
        if st.button('Volver a inicio'): # Botón para poder volver a inicio.
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
        df_auxiliar = pd.DataFrame()
            
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
            # Se muestra el resultado.
            st.metric(label="Predicción del precio", value=str(np.round(prediccion[0], 2)) + '$', delta=str(np.round(((prediccion[0] - df['price'].mean()) / df['price'].mean()) * 100, 2)) + "%",delta_color='normal')
            st.write('(Se muestra el porcentaje relativo con respecto al precio medio. Precio medio: ', np.round(df['price'].mean(), 2), '$)')
            
            posicion = datos_entrada.columns.get_loc('table') + 1 # Se busca la posición seguida a la columna 'table'.
            datos_entrada.insert(loc = posicion, column = 'price', value = prediccion) # Se añaden los datos de la predicción al DataFrame de entrada.
            
            if 'df_predicciones' not in st.session_state:
                st.session_state['df_predicciones'] = datos_entrada.copy() # Si no se ha realizado ninguna predicción anterior, se añade la predicción al session_state.
            else:
                st.session_state['df_predicciones'] = pd.concat([st.session_state['df_predicciones'], datos_entrada], ignore_index = True)  # Se añade la predicción al session_state.
            
            st.session_state['prediccion_reg_generada'] = True # Se cambia el flag, dado que ya se ha generado una predicción.
            
        if st.session_state['prediccion_reg_generada']: # Si se ha generado alguna predicción durante la sesión actual, se muestra el botón de "Guardar..."
            if st.button("Guardar predicciones en archivo"):
                if 'df_predicciones' in st.session_state:
                    os.makedirs('data', exist_ok=True)
                    st.session_state['df_predicciones'].drop_duplicates(inplace = True)                 # Se eliminan duplicados de las predicciones antes de guardar los datos en el archivo.
                    st.session_state['df_predicciones'].to_csv('data/predicciones.csv', index=False)
                    st.session_state['prediccion_reg_generada'] = False
                    st.rerun()
                
        if 'df_predicciones' not in st.session_state:
            st.write("No hay predicciones que mostrar.")
        else:
            st.header("Predicciones efectuadas.")
            df_predicciones = st.data_editor(st.session_state['df_predicciones'], use_container_width=True)