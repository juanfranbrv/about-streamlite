import streamlit as st

st.title("Tips y cositas para Streamlit")

st.subheader("Cambiar el tipo de letra para todas las paginas de la webapp")

st.code("""



st.markdown(
    \"""
    <style>
    /* Cambiar el tipo de letra y tamaño para todo el cuerpo */
    html, body, [class*="css"] {
        font-family: 'Montserrat';
        font-size: 20px; 
    }
    /* Ajustar encabezados si es necesario */
    h1, h2, h3, h4, h5, h6 { font-family: 'Montserrat'  }

    /* Personalizar tamaño de encabezados */
    h1 { font-size: 28px; }
    h2 { font-size: 24px; }
    h3 { font-size: 20px; }

    </style>
    \""",
    unsafe_allow_html=True
)




""", language='python')

st.link_button("Go to gallery", "https://streamlit.io/gallery")