# Home.py
import streamlit as st
# Página principal.
st.set_page_config(page_title="Analisis DataFrame 'Diamonds'", layout="wide")
import pandas as pd
import joblib
import os

# Se cargan en la caché todos los datos que serán utilizados entre las diferentes páginas de la aplicación.
# Los datos cargados, se almacenan en el diccionario 'session_state'.
@st.cache_resource(show_spinner='Cargando datos...')
def cargar_datos():
    ruta_dataframe = 'data/diamonds.csv'                        # DataFrame principal.
    ruta_df_predicciones = 'data/predicciones.csv'              # DataFrame con las predicciones generadas.
    ruta_model_reg = 'models/pipeline_regresion.joblib'         # Modelo de regresión para predecir la columna 'price'.
    ruta_model_cla = 'models/pipeline_clasificacion.joblib'     # Modelo de clasificación para predecir la columna 'cut'.
    ruta_label_encoder = 'models/label_encoder_clasificacion.joblib'    # Mapeado de la columna 'cut'.
    lista_rutas ={'df': ruta_dataframe, 'df_predicciones': ruta_df_predicciones,'model_reg': ruta_model_reg, 'model_cla': ruta_model_cla, 'label_encoder': ruta_label_encoder}
    for archivo, ruta in lista_rutas.items():                   # Se recorre la lista, se van cargando los datos y almacenandol en session_state.
        if os.path.exists(ruta):
            try:
                if ruta.endswith('.csv'):           # Los archivos .csv se cargan de forma diferente.
                    st.session_state[archivo] = pd.read_csv(ruta)
                    st.session_state[archivo].drop_duplicates(inplace = True) # Tras la carga, se eliminan las posibles filas duplicadas.
                else:
                    st.session_state[archivo] = joblib.load(ruta)   # Se cargan los archivos .joblib.
            except Exception as e:
                st.error(f"Error al cargar el archivo '{ruta}': {e}.")
        else:
            st.error(f"El archivo {archivo} no se encuentra en la ruta '{ruta}'.")
    return

cargar_datos()

st.title("Análisis del Dataset 'Diamonds'")
st.markdown("""
Esta aplicación realiza un análisis exploratorio del famoso dataset **diamonds** y permite:
- Visualizar gráficos univariantes, bivariantes y multivariantes.
- Realizar predicciones de precio mediante un modelo de regresión.
- Predecir la categoría del corte de los diamantes mediante un modelo de clasificación.
""")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("EDA's"):
        st.switch_page('pages/1_EDAs.py')

with col2:
    if st.button("Regresión"):
        st.switch_page('pages/2_Regresion.py')
        
with col3:
    if st.button("Clasificación"):
        st.switch_page('pages/3_Clasificacion.py')