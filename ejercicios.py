import streamlit as st

st.title("Ejercicios")

st.subheader("Ejercicio 1: Página de Bienvenida Interactiva")
st.markdown("<hr style='border: 0.1px solid #000; margin: 0px 0px'>", unsafe_allow_html=True)
st.markdown("""Crea una página de bienvenida interactiva que

- Muestre un titulo.

- Un parrafo de texto extenso con trozo  subrayado en amarillo

- Incluye botones para activar efectos visuales (globos y nieve).

- Muestra una imagen cuadrada con un enlace.

- Muestra una imagen tipo banner que ocupe el ancho de la web sin enlace (local)

- Incluye un enlace adicional al repositorio de la aplicación""")

if st.button("Ver solución"):
    pass