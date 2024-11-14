import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Ejemplo de Texto en Streamlit", page_icon="📚")

# Título de la aplicación
st.title("📚 Ejemplo de Textos en Streamlit")
st.write("En esta aplicación, exploraremos todas las formas de mostrar texto en Streamlit.")

# 1. Mostrar texto simple con st.write

st.write("`st.write` es el método más versátil para mostrar texto y otros elementos en Streamlit. Puedes pasarle casi cualquier tipo de dato, y Streamlit intentará mostrarlo de la forma más adecuada. por ejemplo *markdown* o emojis 🎈")

# 2. Título principal con st.title
st.title("Este es un título principal usando st.title")

# 3. Título de sección con st.header
st.header("Este es un título de sección usando st.header")

# 4. Subtítulo con st.subheader
st.subheader("Este es un subtítulo usando st.subheader")

# 5. Texto fijo con st.text
st.text("Este es un texto fijo usando st.text. No permite *formato*.")

# 6. Mostrar código con st.code
codigo = '''
st.title("Mi App")
st.write("¡Bienvenidos a mi app!")
'''
st.code(codigo, language='python')

# 7. Mostrar ecuaciones con st.latex
st.header("7. Ecuaciones con st.latex")
st.write("Puedes mostrar ecuaciones matemáticas usando LaTeX:")
st.latex(r'''
e^{i\pi} + 1 = 0
''')

# 8. Mostrar Markdown con st.markdown
st.header("8. Markdown con st.markdown")
st.markdown("""
Puedes usar `st.markdown` para mostrar texto con formato **Markdown**.
* **Texto en negrita**
* *Texto en cursiva*
* ~~Texto tachado~~
* Citas: 
    > Esta es una cita en Markdown
* Enlaces: [Streamlit](https://streamlit.io)
""")

# Usando HTML en Markdown para cambiar el color a rojo
st.write("Atencion con markdown podemos incluir HTML y algo de CSS")

st.code("""
# Usando HTML en Markdown para cambiar el color a rojo
st.markdown("<h1 style='color: red;'>Este es un título en rojo</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: blue;'>Este es un párrafo en azul.</p>", unsafe_allow_html=True)
""", language="python")

st.markdown("<h1 style='color: red;'>Este es un título en rojo</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: blue;'>Este es un párrafo en azul.</p>", unsafe_allow_html=True)

st.write("Incluso podemos crear estilos en una linea, para poder usarlos posteriormete en esa pagina")

st.code("""
st.markdown(\"\"\"
    <style>
    .big-font {
        font-size:24px !important;
        color: purple;
    }
    </style>
    \"\"\", unsafe_allow_html=True)

st.markdown('<p class="big-font">Este es un texto en púrpura con un tamaño más grande.</p>', unsafe_allow_html=True)
""", language="python")

st.markdown("""
    <style>
    .big-font {
        display: inline-block;
        font-weight: bold;
        font-size:28px !important;
        color: purple;
        background: yellow;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="big-font">Este es un texto en púrpura con un tamaño más grande.</p>', unsafe_allow_html=True)




# 9. Mostrar íconos y emojis en texto
st.header("9. Íconos y emojis en texto")
st.write("Puedes agregar íconos y emojis para hacer que la app sea más visual y divertida.")
st.write("Aquí algunos ejemplos: 🌍 📈 🐍 🎉 ✅")

# 10. Notificaciones de estado con st.success, st.info, st.warning, y st.error
st.header("10. Notificaciones de estado")
st.success("✅ Esta es una notificación de éxito.")
st.info("ℹ️ Esta es una notificación de información.")
st.warning("⚠️ Esta es una notificación de advertencia.")
st.error("❌ Esta es una notificación de error.")

# 11. Mostrar un mensaje personalizado con st.toast
st.header("11. Mensaje personalizado con st.toast")
st.toast("Este es un toast, un mensaje temporal que aparece en la esquina")

# 12. Texto personalizado en el sidebar
st.sidebar.header("Texto en la barra lateral")
st.sidebar.text("Este es un texto en la barra lateral.")
st.sidebar.markdown("### Sección en la barra lateral")

# Resumen
st.header("Resumen")
st.write("Este ejemplo incluye todas las formas principales de mostrar texto en Streamlit. Puedes experimentar con ellas para hacer tus aplicaciones más interactivas y atractivas visualmente.")


