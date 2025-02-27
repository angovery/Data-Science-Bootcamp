## EJERCICIO

Dataset: diamonds.

* PARTE 1 (30 %): Página 1 con EDA con seaborn y plotly con filtros globales
    * Gráficos univariantes: histograma, kdeplot, boxplot
    * Gráficos bivariantes: scatter
    * Gráficos multivariantes: heatmap, pairplot, scatter con hue o color 
    * Filtros globales categóricos y numéricos: un filtro para columna
* PARTE 2 (35 %): Página 2 Regresión con formulario sobre price + Pipeline ipynb
    * Regresión sobre columna price
    * pipeline_regresion.ipynb
    * pipeline_regresion.joblib
    * 2_Regresion.py con formulario de entrada para introducir datos y hacer prediccion y mostrar en st.metric
* PARTE 3 (35 %): Página 3 Clasificación con formulario sobre cut + Pipeline ipynb
    * Clasificación multiclase sobre columna cut (Usar LabelEncoder para cut)
    * pipeline_clasificacion.ipynb
    * pipeline_clasificacion.joblib
    * 3_Clasificacion.py con formulario de entrada para introducir datos y hacer prediccion y mostrar en st.metric
* Usar multipáginas
* Separar apartados con encabezados o container
* Mostrar predicciones usando st.metric
* Opcionalmente se pueden acumular predicciones en un dataframe y mostrar un botón de descargar dataframe en CSV.


Fecha entrega M7: miércoles 05/03/2025 23:59:59 Hora peninsular

Tutoría: martes 04/03/2025 - 16:00 a 18:00 en el mismo enlace zoom

Formato entrega:

* Nueva carpeta modulo_7_nombre_apellido_evaluable en el repositorio github que ya tenéis.
    * app.py (Home)
    * .streamlit/
    * pages/
        * 1_EDA.py
        * 2_Regresion.py
        * 3_Clasificacion.py
    * models/
        * pipeline_regresion.joblib
        * pipeline_clasificacion.joblib
    * notebooks/
        * pipeline_regresion.ipynb
        * pipeline_clasificacion.ipynb