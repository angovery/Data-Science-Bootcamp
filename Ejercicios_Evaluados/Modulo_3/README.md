## EJERCICIO MÓDULO 3:

Uso de Pandas y Seaborn + algún gráfico de Plotly.

Dataset: diamonds.

IMPORTANTE: cargar el dataset desde CSV desde la carpeta Data porque tendrá nulos introducidos manualmente.

* Carga con Pandas: pd.read_csv

* Limpieza de nulos (limpiar valores NaN):
    * Nulos en columnas continuas: mediana, media
    * Nulos en columnas categóricas: moda, un valor fijo

* Cambio de tipo de dato: .astype() por ejemplo a categorical

* Limpieza de valores error: 
    * hay columnas que tienen un valor '?', por tanto se deben reemplazar por una mediana o moda o valor fijo.

* Encoding: texto a numérico
    * Uso de la función get_dummies() para encoding one_hot
    * Uso de map para encoding ordinal para la columna cut: 1, 2, 3, 4

* Uso de función apply:
    * crear una columna price_iva a partir de la columna price que muestre el precio + IVA (21%)

* Crear una nueva columna volumen combinando: x, y, z

* Ordenar por dos columnas con sort_values():
    * tipo de corte (cut) y precio (price)

* Agrupaciones con groupby y visualizarla
    * Agrupar por las 3 que hay de tipo categórico calculando la media, max, min por ejemplo de alguna de las numéricas: price, carat, depth

* Seaborn EDAS:
    * univariantes:
        * histogramas y curvas de densidad
        * boxplot
        * countplot
    * bivariantes y multivariantes
        * scatterplot con hue, con size, con style
        * Calcular correlación con Pandas y mostrarla con seaborn
        * Hacer la correlación en un gráfico de barras para la columna 'price'
    * Combinarlas con:
        * hue, style
        * filtro

* Outliers: Visualización Q1 y Q3 y calcular límites tukey y filtrar. Sobre la columna precio.

* asimetría, curtosis y transformar datos con logaritmo o raíz cuadrada

* Discretizar la columna precio por barato, medio, caro usando la función pd.cut