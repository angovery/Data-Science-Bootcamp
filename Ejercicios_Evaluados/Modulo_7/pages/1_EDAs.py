# Página para EDA's.
import streamlit as st
st.set_page_config(page_title="EDA - Diamonds", layout="wide")
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

# Carga del DataSet.
ruta = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/diamonds.csv'
@st.cache_resource(show_spinner='Cargando el DataFrame...')
def load_data():
    df = pd.read_csv(ruta)
    return df

df = load_data()

if st.button('Volver a inicio'): # opcional poder volver a inicio
    st.switch_page('Inicio.py')

st.title("EDA - Análisis Exploratorio de Datos")
st.markdown("Explora el dataset de diamonds aplicando filtros individuales y ajusta el tamaño de los gráficos.")

st.header("1.-DataFrame editable.")
df_editable = st.data_editor(df, use_container_width=True)

# Listas de variables.
num_cols = ['carat', 'depth', 'table', 'x', 'y', 'z']
cat_cols = ['cut', 'color', 'clarity']

# Valores posibles para las variables ordinales (definidos de menor a mayor).
cut_order = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
color_order = ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
clarity_order = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF', 'FL']

# Se configuran los filtros en la barra lateral.
st.sidebar.header("Filtros Globales")

# --- Filtro para variable numérica seleccionada ---
st.sidebar.subheader("Filtro Variables Numéricas")
num_seleccionado = st.sidebar.selectbox("Selecciona una variable numérica", num_cols)
valor_min = float(df[num_seleccionado].min())
valor_max = float(df[num_seleccionado].max())
rango_filtro_num = st.sidebar.slider(
    f"Rango para {num_seleccionado}",
    min_value=valor_min,
    max_value=valor_max,
    value=(valor_min, valor_max)
)

# --- Filtros para variables categóricas (ordinales) ---
st.sidebar.subheader("Filtro Variables Categóricas (Ordinales)")
filtros_cat = {}
filtros_cat['cut'] = st.sidebar.multiselect("Cut", options=cut_order, default=cut_order)
filtros_cat['color'] = st.sidebar.multiselect("Color", options=color_order, default=color_order)
filtros_cat['clarity'] = st.sidebar.multiselect("Clarity", options=clarity_order, default=clarity_order)

# --- Ajustes de tamaño de gráficos ---
st.sidebar.header("Ajustes de Tamaño de Gráficos")
# Para gráficos Plotly (en píxeles).
plotly_width = st.sidebar.number_input("Ancho Plotly (px)", min_value=300, max_value=2000, value=800)
plotly_height = st.sidebar.number_input("Alto Plotly (px)", min_value=300, max_value=2000, value=500)
# Para gráficos Matplotlib.
mpl_width = plotly_width / 100
mpl_height = plotly_height / 100

# Se aplican los filtros al DataFrame.
df_filtrado = df.copy()
df_filtrado = df_filtrado[df_filtrado[num_seleccionado].between(rango_filtro_num[0], rango_filtro_num[1])]
for col, seleccion in filtros_cat.items():
    if seleccion:
        df_filtrado = df_filtrado[df_filtrado[col].isin(seleccion)]

st.header("2.-DataFrame filtrado.")
st.write(df_filtrado.head())

# --- Visualización de Gráficos ---

st.header("3.-Gráficos Univariantes.")
# Histograma de Price con Plotly
fig_hist = px.histogram(
    df_filtrado, 
    x='price', 
    title='Histograma de Price',
    width=plotly_width,
    height=plotly_height
)
st.plotly_chart(fig_hist, use_container_width=True)

# KDE plot con Seaborn y Matplotlib
fig, ax = plt.subplots(figsize=(mpl_width, mpl_height))
sns.kdeplot(df_filtrado['price'], ax=ax)
ax.set_title("KDE Plot de Price")
st.pyplot(fig)

# Boxplot con Seaborn y Matplotlib
fig, ax = plt.subplots(figsize=(mpl_width, mpl_height))
sns.boxplot(x=df_filtrado['price'], ax=ax)
ax.set_title("Boxplot de Price")
st.pyplot(fig)

st.header("4.-Gráficos Bivariantes.")
# Scatter plot: Carat vs Price con Plotly
fig_scatter = px.scatter(
    df_filtrado, 
    x='carat', 
    y='price', 
    title='Scatter: Carat vs Price',
    width=plotly_width,
    height=plotly_height
)
st.plotly_chart(fig_scatter, use_container_width=True)

st.header("5.-Gráficos Multivariantes.")
# Heatmap de correlaciones con Seaborn y Matplotlib
fig, ax = plt.subplots(figsize=(mpl_width, mpl_height))
corr = df_filtrado.select_dtypes(include=['float64', 'int64']).corr()
sns.heatmap(corr, annot=True, ax=ax)
ax.set_title("Heatmap de correlaciones")
st.pyplot(fig)

# Pairplot (muestra de 500 datos) usando Seaborn
st.markdown("Pairplot (muestra de 500 datos)")
sample_data = df_filtrado.sample(500) if len(df_filtrado) > 500 else df_filtrado
pairplot_fig = sns.pairplot(sample_data.select_dtypes(include=['float64', 'int64']))
# El objeto pairplot no permite definir figsize de forma directa, por lo que se muestra sin ajuste de tamaño.
st.pyplot(pairplot_fig.fig)

# Scatter con hue: diferenciando por 'cut' con Plotly
fig = px.scatter(
    df_filtrado, 
    x='carat', 
    y='price', 
    color='cut', 
    title='Scatter: Carat vs Price con Hue en cut',
    width=plotly_width,
    height=plotly_height
)
st.plotly_chart(fig, use_container_width=True)

