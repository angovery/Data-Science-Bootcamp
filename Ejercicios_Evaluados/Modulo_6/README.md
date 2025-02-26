## EJERCICIO M6

OBJETIVOS: 
- Regresión de la columna 'price'.
- Clasificación de la columna 'cat'.

Dataset: diamonds

* PARTE 1 (10 %) Carga de datos de diamonds desde CSV con schema: https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/diamonds.csv

* PARTE 2 (40 %) Pipeline regresión price con preprocesados
  * Imputer, StringIndexer, OneHotEncoder, MinMaxScaler o StandardScaler, VectorAssembler

* PARTE 3 (40 %) Pipeline clasificación multiclase sobre variable cut con preprocesados
  * Imputer, StringIndexer, OneHotEncoder, MinMaxScaler o StandardScaler, VectorAssembler

* PARTE 4 (10 %) Gridsearch con CrossValidation sobre cualquiera de los pipelines

Los modelos, se puede utilizar RandomForest para los dos por ejemplo o el que se quiera. Ejemplo RandomForestRegressor para regresión y MultilayerPerceptronClassifier para clasificación.

m6_nombre_apellido.ipynb

Entrega: 02/03/2025

Usar pyspark MLlib y dataframes de pyspark. Seguir el notebook 08.pipelines.ipynb
