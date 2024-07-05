import streamlit as st

# Título de la aplicación
st.title('Aplicación de Ejemplo en Streamlit')

# Entrada de texto para el nombre
name = st.text_input('Ingrese su nombre:')

# Entrada de número para la edad
age = st.number_input('Ingrese su edad:', min_value=0, max_value=120, step=1)

# Botón para mostrar el saludo
if st.button('Saludar'):
    st.write(f'Hola, {name}!')
    st.write(f'Tienes {age} años.')

    # Calcular y mostrar la edad en años perro
    dog_age = age * 7
    st.write(f'Tu edad en años perro es: {dog_age} años.')
