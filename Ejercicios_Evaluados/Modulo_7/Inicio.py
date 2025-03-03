# Home.py
import streamlit as st
# Página principal.
st.set_page_config(page_title="Analisis DataFrame 'Diamonds'", layout="wide")
import pandas as pd
import joblib

# Carga del DataSet.
ruta = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/diamonds.csv'
@st.cache_resource(show_spinner='Cargando el DataFrame...')
def load_data():
    df = pd.read_csv(ruta)
    model_reg = joblib.load("Models/pipeline_regresion.joblib")
    model_cla = joblib.load("Models/pipeline_clasificacion.joblib")
    label_encoder = joblib.load("Models/label_encoder_clasificacion.joblib")
    return df, model_reg, model_cla, label_encoder

df, model_reg, model_cla, label_encoder = load_data()

# Se almacenan los datos cargados en session_state, para poder compartirlo entre las diferentes páginas de la aplicación.
st.session_state['df'] = df
st.session_state['model_reg'] = model_reg
st.session_state['model_cla'] = model_cla
st.session_state['label_encoder'] = label_encoder

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