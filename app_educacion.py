import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Análisis de Datos de Educación en Colombia")

# Cargar el archivo CSV directamente desde la raíz del repositorio
df = pd.read_csv("educacion.csv")  

# Mostrar el DataFrame en la página principal
st.subheader("Tabla de Datos de Educación")
st.dataframe(df)

# Agregar widgets para filtrar los datos
st.sidebar.header("Filtros")

# Filtrar por nivel educativo
nivel_educativo = st.sidebar.multiselect(
    "Nivel educativo", df["Nivel educativo"].unique()
)

# Filtrar por carrera
carrera = st.sidebar.multiselect("Carrera", df["Carrera"].unique())

# Filtrar por institución
institucion = st.sidebar.multiselect("Institución", df["Institución"].unique())

# Filtrar el DataFrame con base en los filtros seleccionados
df_filtrado = df.copy()
if nivel_educativo:
    df_filtrado = df_filtrado[df_filtrado["Nivel educativo"].isin(nivel_educativo)]
if carrera:
    df_filtrado = df_filtrado[df_filtrado["Carrera"].isin(carrera)]
if institucion:
    df_filtrado = df_filtrado[df_filtrado["Institución"].isin(institucion)]

# Mostrar el DataFrame filtrado
st.subheader("Datos Filtrados")
st.dataframe(df_filtrado)

# Calcular y mostrar estadísticas descriptivas de los datos filtrados
st.subheader("Estadísticas Descriptivas")
st.write(df_filtrado.describe())

# Conteo de estudiantes por nivel educativo
st.subheader("Conteo de Estudiantes por Nivel Educativo")
st.bar_chart(df_filtrado["Nivel educativo"].value_counts())

# Visualizar la distribución de la edad con un histograma
st.subheader("Distribución de la Edad")
st.bar_chart(df_filtrado["Edad"].value_counts())

st.subheader("Estadísticas por Nivel Educativo")
estadisticas_nivel = df_filtrado.groupby("Nivel educativo")["Edad"].agg(['mean', 'min', 'max']).reset_index()
st.dataframe(estadisticas_nivel)
