# Pages/3_Clasificacion.py
import streamlit as st
st.set_page_config(page_title="Modelo de Clasificación - Diamonds", layout="wide")
import pandas as pd
import os

if 'prediccion_cla_generada' not in st.session_state:
    st.session_state['prediccion_cla_generada'] = False      # Se inicializa la variable que controla si se ha realizado alguna predicción en la sesión actual.
    
if 'df' not in st.session_state:
    st.error('El DataFrame no se encuentra disponible. por favor, vuelve a cargar la página de Inicio.')
else:
    df = st.session_state['df'] # Carga del DataSet.

    if ('model_cla' not in st.session_state) or ('label_encoder' not in st.session_state):
        st.error('El modelo de clasificación y/o el label_encoder no se encuentran disponibles. por favor, vuelve a cargar la página de Inicio.')
    else:   
        # Se carga el modelo y el label_encoder de la caché, para minimizar tiempos de espera en consultas posteriores.
        modelo_clasificacion = st.session_state['model_cla']
        label_encoder = st.session_state['label_encoder']

        if st.button('Volver a inicio'): # Botón para poder volver a inicio.
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
            datos_entrada = pd.DataFrame({
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
            prediccion_cla = modelo_clasificacion.predict(datos_entrada)
            # Se decodifica el valor numérico de la prediccióm para mostrar el valor asociado de los posibles valores de la variable.
            etiqueta_predicha = label_encoder.inverse_transform(prediccion_cla)
            # Se muestra el resultado.
            st.metric("El corte predicho es:", etiqueta_predicha[0])
            
            posicion_cut = datos_entrada.columns.get_loc('carat') + 1       # Se busca la posición seguida a la columna 'carat'.
            datos_entrada.insert(loc = posicion_cut, column = 'cut', value = etiqueta_predicha) # Se añaden los datos de la predicción al DataFrame de entrada.
            
            # Para guardar los datos de las predicciones, se predice la variable 'price' con los datos de entrada y la predicción de 'cut'.
            if 'model_reg' not in st.session_state:
                st.write("No se ha cargado el modelo de regresión. Por favor, vuelva a cargar la página de Inicio")
            else:
                modelo_regresion = st.session_state['model_reg']
                prediccion_reg = modelo_regresion.predict(datos_entrada)
                posicion_price = datos_entrada.columns.get_loc('table') + 1
                datos_entrada.insert(loc = posicion_price, column = 'price', value = prediccion_reg)
            
            if 'df_predicciones' not in st.session_state:                       # Si no se ha realizado ninguna predicción anterior, se añade la predicción al session_state.
                st.session_state['df_predicciones'] = datos_entrada.copy()
            else:
                st.session_state['df_predicciones'] = pd.concat([st.session_state['df_predicciones'], datos_entrada], ignore_index=True)    # Se añade la predicción al session_state.
            
            st.session_state['prediccion_cla_generada'] = True      # Se cambia el flag, dado que ya se ha generado una predicción.
        
        # Se decide que la aparición del botón "Guardar..." esté condicionada a que, previamente, se haya generado una predicción durante la sesión.
        # Se podría haber sustituido el botón "Predecir..." por el botón "Guardar...", pero esto habría implicado la imposibilidad de guardar varias predicciones generadas durante la sesión de una sola vez.
        # Si se sustituyera un botón por otro, se tendría que guardar, de forma individual, cada predicición generada durante la sesión.
        if st.session_state['prediccion_cla_generada']:                                                 # Si se ha generado alguna predicción durante la sesión actual, se muestra el botón de "Guardar..."
            if st.button("Guardar predicciones en archivo"):
                if 'df_predicciones' in st.session_state:
                    os.makedirs('data', exist_ok=True)
                    st.session_state['df_predicciones'].drop_duplicates(inplace = True)                 # Se eliminan duplicados de las predicciones antes de guardar los datos en el archivo.
                    st.session_state['df_predicciones'].to_csv('data/predicciones.csv', index=False)
                    st.session_state['prediccion_cla_generada'] = False                                 # Se cambia el flag para ocultar el botón "Guardar..." hasta que se genere una nueva predicción. 
                    st.rerun()                                                                          # Se recarga la página para que los cambios surtan efecto.
            
        if 'df_predicciones' not in st.session_state:
            st.write("No hay predicciones que mostrar.")
        else:
            st.header("Predicciones efectuadas.")
            df_predicciones = st.data_editor(st.session_state['df_predicciones'], use_container_width=True)