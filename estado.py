import streamlit as st

st.title("Estado de una aplicación")

st.write("""

¿Qué es el Estado de una Aplicación?
En el contexto de la programación de aplicaciones web o interactivas, el estado se refiere a la información que la aplicación necesita recordar para mantenerse consistente durante su uso. En otras palabras, es como una memoria temporal que permite a la aplicación recordar lo que ha pasado hasta ahora, incluso cuando el usuario interactúa con la interfaz.

Por ejemplo, en un juego, el estado podría ser la puntuación del jugador; en un formulario largo, podría ser la información introducida hasta el momento, en una app de compras el estado del carrito El estado permite que la aplicación no "olvide" lo que el usuario ha hecho, evitando que se reinicie con cada interacción.


""")

st.subheader("Estado en Streamlit")
st.write(""" Estado en Streamlit
Streamlit, por su diseño, re-ejecuta el script completo cada vez que el usuario realiza alguna acción, como presionar un botón o mover un control deslizante. Sin un mecanismo para mantener el estado, cada interacción haría que la aplicación volviera a su punto inicial, como si se reiniciara desde cero.

Para resolver esto, Streamlit introduce **st.session_state**, una especie de contenedor donde puedes almacenar variables que necesitas recordar entre interacciones del usuario. Esto permite que la aplicación tenga persistencia de datos durante una sesión, y no se pierdan las acciones que ya se realizaron.""")

st.subheader("¿Cómo Implementa Streamlit el Estado con st.session_state?")

st.markdown("""
- **st.session_state** es un Diccionario:

**st.session_state** es similar a un diccionario de Python, donde puedes almacenar valores clave. Esto te permite definir variables persistentes.
""")
st.code("""

if 'contador' not in st.session_state:
    st.session_state.contador = 0


""")

st.markdown(""" 
- **Persistencia entre Interacciones:**

Cuando un usuario interactúa (por ejemplo, hace clic en un botón), Streamlit re-ejecuta el script completo. Pero, las variables almacenadas en st.session_state mantienen su valor, ya que no se reinician.

""")

st.markdown(""" 

Piensa en st.session_state como un diccionario global que vive durante la sesión del usuario. A diferencia de las variables locales, los valores almacenados en st.session_state no se pierden entre las ejecuciones sucesivas del script, lo que permite mantener datos relevantes y hacer la aplicación interactiva de manera más intuitiva.


""")

st.markdown("""- **st.session_state es global**

Funciona como una variable global que está disponible en todas las páginas de la aplicación. Esto significa que cualquier valor almacenado en st.session_state es accesible y compartido entre las diferentes páginas.
""")

