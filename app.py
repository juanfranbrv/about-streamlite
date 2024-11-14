import streamlit as st






# Definir las páginas de la aplicación
pagina_inicio = st.Page("inicio.py", title="Inicio", url_path="inicio")

pagina_textos = st.Page("textos.py", title="Texto", url_path="textos")

pagina_botones = st.Page("botones.py", title="Botones", url_path="botones")

pagina_links = st.Page("links.py", title="Links", url_path="links")

pagina_imagenes = st.Page("imagenes.py", title="Imagenes", url_path="imagenes")

# Crear la navegación
navegacion = st.navigation([
    pagina_inicio,
    pagina_textos,
    pagina_botones,
    pagina_links,
    pagina_imagenes,

    
    
    st.Page("widgets_de_entrada.py", title="Widgets de entrada", url_path="widgets_de_entrada"),

     st.Page("widgets_de_salida.py", title="Widgets de salida", url_path="widgets_de_salida"),

     st.Page("ejercicios.py"),

     st.Page("visualización_de_datos.py"),

     st.Page("diseño_interfaz.py",),

     st.Page("tips.py", title="Tips", url_path="tips"),


    
    
    ] 
    
)



# Ejecutar la navegación
navegacion.run()

# Cambiar el tipo de letra y tamaño globalmente con CSS
st.markdown(
    """
    <style>
    /* Cambiar el tipo de letra y tamaño para todo el cuerpo */
    html, body, [class*="css"] {
        font-family: 'Montserrat';
        font-size: 20px; 
    }
    /* Ajustar encabezados si es necesario */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Montserrat'
    }

     /* Personalizar tamaño de encabezados */
    h1 {
        font-size: 28px; /* Ajusta el tamaño del encabezado h1 */
    }
    h2 {
        font-size: 24px; /* Ajusta el tamaño del encabezado h2 */
    }
    h3 {
        font-size: 20px; /* Ajusta el tamaño del encabezado h3 */
    }
    </style>
    """,
    unsafe_allow_html=True
)
