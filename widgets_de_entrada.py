import streamlit as st

# Título de la aplicación
st.title("Widgets Interactivos en Streamlit")

# Introducción
txt_intro = """
En esta página, exploraremos los widgets interactivos disponibles en Streamlit que permiten a los usuarios ingresar información, seleccionar valores, y realizar interacciones que afectan el comportamiento de la aplicación. A continuación, se presenta una lista de widgets comunes con ejemplos de cómo utilizarlos.
"""
st.write(txt_intro)

# 1. Entrada de Texto
st.subheader("1. Entrada de Texto")
st.write("`st.text_input()`: Permite a los usuarios escribir texto. Por ejemplo, para pedir datos como nombres o direcciones.")
st.code("""
nombre = st.text_input("Ingresa tu nombre:")
""", language="python")

# 2. Área de Texto
st.subheader("2. Área de Texto")
st.write("`st.text_area()`: Similar a `st.text_input()`, pero para escribir texto más largo, como comentarios o descripciones.")
st.code("""
comentario = st.text_area("Deja un comentario:")
""", language="python")

# 3. Entrada de Números
st.subheader("3. Entrada de Números")
st.write("`st.number_input()`: Permite al usuario ingresar un número, con valores mínimos, máximos y un paso definido.")
st.code("""
edad = st.number_input("Ingresa tu edad:", min_value=0, max_value=120, step=1)
""", language="python")

# 4. Control Deslizante (Slider)
st.subheader("4. Control Deslizante (Slider)")
st.write("`st.slider()`: Permite seleccionar un valor dentro de un rango, útil para ajustar valores numéricos de manera visual.")
st.code("""
valor = st.slider("Selecciona un valor:", min_value=0, max_value=100)
""", language="python")

# 5. Selección Única (Selectbox)
st.subheader("5. Selección Única (Selectbox)")
st.write("`st.selectbox()`: Permite seleccionar una sola opción de una lista desplegable.")
st.code("""
fruta = st.selectbox("Selecciona tu fruta favorita:", ["Manzana", "Banana", "Naranja"])
""", language="python")

# 6. Selección Múltiple (Multiselect)
st.subheader("6. Selección Múltiple (Multiselect)")
st.write("`st.multiselect()`: Permite seleccionar múltiples opciones de una lista.")
st.code("""
hobbies = st.multiselect("Selecciona tus hobbies:", ["Leer", "Viajar", "Correr", "Nadar"])
""", language="python")

# 7. Botones de Opción (Radio)
st.subheader("7. Botones de Opción (Radio)")
st.write("`st.radio()`: Permite seleccionar una sola opción de varias, mostrando todas las opciones visibles como botones.")
st.code("""
genero = st.radio("Selecciona tu género:", ["Masculino", "Femenino", "Otro"])
""", language="python")

# 8. Casilla de Verificación (Checkbox)
st.subheader("8. Casilla de Verificación (Checkbox)")
st.write("`st.checkbox()`: Permite al usuario seleccionar una opción con una casilla de verificación.")
st.code("""
aceptar = st.checkbox("Acepto los términos y condiciones")
""", language="python")

# 9. Entrada de Fecha
st.subheader("9. Entrada de Fecha")
st.write("`st.date_input()`: Permite al usuario seleccionar una fecha del calendario.")
st.code("""
fecha = st.date_input("Selecciona una fecha:")
""", language="python")

# 10. Entrada de Hora
st.subheader("10. Entrada de Hora")
st.write("`st.time_input()`: Permite seleccionar una hora específica.")
st.code("""
hora = st.time_input("Selecciona una hora:")
""", language="python")

# 11. Carga de Archivos
st.subheader("11. Carga de Archivos")
st.write("`st.file_uploader()`: Permite al usuario cargar un archivo desde su dispositivo.")
st.code("""
archivo = st.file_uploader("Sube un archivo:", type=["csv", "txt", "jpg", "png"])
""", language="python")

# 12. Selector de Color
st.subheader("12. Selector de Color")
st.write("`st.color_picker()`: Permite seleccionar un color de una paleta.")
st.code("""
color = st.color_picker("Elige un color:", "#00f900")
""", language="python")

# Resumen
txt_resumen = """
Estos widgets interactivos son fundamentales para crear aplicaciones dinámicas e interactivas en Streamlit. Puedes combinarlos de diferentes maneras para recopilar información de los usuarios y proporcionar una experiencia enriquecedora.


Pero esta lista NO es completa. Puedes revisarlos todos en la documentación oficial https://docs.streamlit.io/develop/api-reference/widgets
"""
st.write(txt_resumen)
