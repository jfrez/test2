import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from datetime import datetime,timedelta


import streamlit as st



model = keras.models.load_model('nn')

st.title("Predictor de clientes")
st.markdown("""
Bienvenido, para continuar indique una fecha, marque si se trata de algun día especial o ambos


""")


cuando = st.date_input("Cuando:")
st.write(cuando)
especial = st.checkbox("Especial", value=False)
feriado = st.checkbox("Feriado", value=False)
fecha_inicio = cuando + timedelta(hours=10)
fecha_fin = cuando + timedelta(hours=22)

# Crear un rango de fechas y horas
rango_horas = [fecha_inicio + timedelta(hours=x) for x in range(12)]
st.write(fecha_inicio)
# Crear un DataFrame
df = pd.DataFrame({'fecha_hora': rango_horas})
if especial:
  df["especial"] =1  #OJO AQUI
else:
  df["especial"] =0
if feriado:
  df["feriado"] =1  #OJO AQUI
else:
  df["feriado"] =0

# Preprocesamiento de datos
df['fecha_hora'] = pd.to_datetime(df['fecha_hora'])
df['year'] = df['fecha_hora'].dt.year
df['month'] = df['fecha_hora'].dt.month
df['hour'] = df['fecha_hora'].dt.hour
df['day_of_week'] = df['fecha_hora'].dt.dayofweek
df['day_of_month'] = df['fecha_hora'].dt.day
df['day_of_year'] = df['fecha_hora'].dt.dayofyear
df['hour'] = range(10,22)

# Agregar columna para la semana del mes
df['week_of_month'] = (df['day_of_month'] - 1) // 7 + 1


df = df.drop(["fecha_hora"],axis=1)  #Eliminar datos no numericos
st.dataframe(df) 

if st.button('Resultados: ' ,type="primary"):

  data = tf.convert_to_tensor(df.to_numpy())
  prediccion = model.predict(data)
  df["prediccion"] = prediccion
  st.dataframe(df) 
