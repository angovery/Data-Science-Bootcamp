# Home.py
import streamlit as st

# Página principal.
st.set_page_config(page_title="Diamonds Analysis", layout="wide")

st.title("Análisis del Dataset 'Diamonds'")
st.markdown("""
Esta aplicación realiza un análisis exploratorio del famoso dataset **diamonds** y permite:
- Visualizar gráficos univariantes, bivariantes y multivariantes.
- Realizar predicciones de precio mediante un modelo de regresión.
- Predecir la categoría del corte de los diamantes mediante un modelo de clasificación.
""")