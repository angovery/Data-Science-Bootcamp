# Home.py
import streamlit as st

# Página principal.
st.set_page_config(page_title="Analisis DataFrame 'Diamonds'", layout="wide")

import pandas as pd

# Carga del DataSet.
ruta = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/diamonds.csv'
@st.cache_resource(show_spinner='Cargando el DataFrame...')
def load_data():
    df = pd.read_csv(ruta)
    return df

df = load_data()

# Se almacena el DataFrame en session_state, para poder compartirlo entre las diferentes páginas de la aplicación.
st.session_state['df'] = df

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