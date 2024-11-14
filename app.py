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
    pagina_imagenes] 
    
)

# Ejecutar la navegación
navegacion.run()
