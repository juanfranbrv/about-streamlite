import streamlit as st


st.set_page_config(page_title="Ejemplo de Texto en Streamlit", page_icon="🎃")

# Título de la aplicación
st.title("Ejemplo de Textos en Streamlit")

# Explicación general
st.write("A continuación se muestran ejemplos de cómo crear enlaces en texto usando Streamlit.")

# Código y Resultado de enlaces usando st.write() sin Markdown ni HTML
st.subheader("Ejemplo 1: Enlace Directo con `st.write()`")
st.code("""
# Enlace directo usando `st.write()`
st.write("Visita Google en https://www.google.com")
""", language="python")
st.write("Resultado:")
st.write("Visita Google en https://www.google.com")

# Código y Resultado de enlaces usando st.write() con formato Markdown
st.subheader("Ejemplo 2: Enlace en texto con Formato Markdown en `st.write()`")
st.code("""
# Enlace usando `st.write()` con formato Markdown
st.write("Visita [Google](https://www.google.com)")
""", language="python")

st.write("Resultado:")
st.write("Visita [Google](https://www.google.com)")

# Código y Resultado de enlaces usando st.markdown() con HTML
st.subheader("Ejemplo 3: Enlace en texto con HTML en `st.markdown()`")
st.code("""
# Enlace usando `st.markdown()` con HTML
st.markdown("<a href='https://www.google.com' style='color:blue;'>Ir a Google</a>", unsafe_allow_html=True)
""", language="python")

st.write("Resultado:")
st.markdown("<a href='https://www.google.com' style='color:blue;'>Ir a Google</a>", unsafe_allow_html=True)

# Código y Resultado de enlaces en imágenes con Markdown
st.subheader("Ejemplo 4: Enlace en Imagen usando Markdown")
st.code("""
# Enlace en imagen usando Markdown
st.markdown("[![Texto alternativo](enlace.png)](https://www.google.com)")
""", language="python")

st.write("Resultado:")
st.markdown("[![Texto alternativo](enlace.png)](https://www.google.com)")

# Código y Resultado de enlaces en imágenes con HTML
st.subheader("Ejemplo 5: Enlace en Imagen usando HTML en `st.markdown()`")
st.code("""
# Enlace en imagen usando HTML en `st.markdown()`
st.markdown(\"\"\"
    <a href='https://www.google.com' target='_blank'>
        <img src='enlace.png' width='150'>
    </a>
\"\"\", unsafe_allow_html=True)
""", language="python")
st.write("Resultado:")
st.markdown("""
    <a href='https://www.google.com' target='_blank'>
        <img src='enlace.png' alt='Texto alternativo' width='150'>
    </a>
""", unsafe_allow_html=True)


st.text("")

st.error("❌En Streamlit, el HTML embebido no puede acceder directamente a archivos locales debido a restricciones de seguridad en la forma en que Streamlit procesa los archivos y renderiza el HTML. Por esa razon no funcionan los ejemplos 4 y 5")

st.image("enlace.png")


st.success("✅ Pero el HTML embebido SI puede acceder imagenes en linea mediante su URL")


st.code("""
# Enlace en imagen usando Markdown
st.markdown("[![Texto alternativo](https://cdn-icons-png.freepik.com/512/1063/1063309.png)](https://www.google.com)")
""", language="python")
st.write("Resultado:")
st.markdown("[![Texto alternativo](https://cdn-icons-png.freepik.com/512/1063/1063309.png)](https://www.google.com)")

st.code("""
# Enlace en imagen usando HTML en `st.markdown()`
st.markdown(\"\"\"
    <a href='https://www.google.com' target='_blank'>
        <img src='https://cdn-icons-png.freepik.com/512/1063/1063309.png' alt='Texto alternativo' width='32'>
    </a>
\"\"\", unsafe_allow_html=True)
""", language="python")
st.write("Resultado:")
st.markdown("""
    <a href='https://www.google.com' target='_blank'>
        <img src='https://cdn-icons-png.freepik.com/512/1063/1063309.png' alt='Texto alternativo' width='32'>
    </a>
""", unsafe_allow_html=True)
