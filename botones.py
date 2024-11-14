import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Ejemplo de Botones en Streamlit", page_icon="🔘")

# Título de la aplicación
st.title("Ejemplo Básico de Botones en Streamlit")
st.write("Esta página muestra cómo funcionan los botones en Streamlit y cómo pueden ser útiles en una aplicación.")

# 1. Botón básico
st.header("1. Botón Básico")
if st.button("Presiona este botón"):
    st.write("¡El botón fue presionado!")
else:
    st.write("El botón aún no ha sido presionado.")

# 2. Botón para ejecutar una función
st.header("2. Botón para Ejecutar una Función")

def mostrar_mensaje():
    st.write("¡Has ejecutado una función al presionar el botón!")

if st.button("Ejecutar función"):
    mostrar_mensaje()

# 3. Botón con estado usando st.session_state
st.header("3. Botón con Estado usando st.session_state")

# Inicializamos el contador si no existe en session_state
if "contador" not in st.session_state:
    st.session_state.contador = 0

# Incrementamos el contador cada vez que se presiona el botón
if st.button("Incrementar contador"):
    st.session_state.contador += 1

st.write(f"Valor actual del contador: {st.session_state.contador}")

# 4. Botón de descarga con st.download_button
st.header("4. Botón de Descarga")

# Creamos un DataFrame de ejemplo para descargar
df = pd.DataFrame({
    "Nombre": ["Ana", "Beto", "Carla"],
    "Edad":   [23,34,45]
})

# Convertimos el DataFrame a CSV
csv = df.to_csv(index=False)

st.download_button(
    label="Descargar datos como CSV",
    data=csv,
    file_name="datos.csv",
    mime="text/csv"
)

# 5. Botón de reset para reiniciar el contador (opcional)
st.header("5. Botón de Reset del Contador")

if st.button("Resetear contador"):
    st.session_state.contador = 0
    st.write("Contador reiniciado a 0.")