import streamlit as st

    # Si no existe, inicializamos los datos del perfil
st.session_state.puntuacion = 0
st.session_state.objetivos = {}
st.session_state.nombre = ""
st.session_state.correo = ""

# Mostrar el formulario para que el usuario ingrese su nombre y correo
st.title("OBJETIVOS")
st.write("Poque cada pequeña gota cuenta")

# Campos de entrada para el nombre y correo
st.session_state.nombre = st.text_input("Nombre de usuario", value=st.session_state.nombre)
st.session_state.correo = st.text_input("Correo electrónico", value=st.session_state.correo)

# Mostrar la puntuación y los objetivos
st.write(f"Puntuación: {st.session_state.puntuacion}")

# Mostrar objetivos y permitir marcar progreso
st.subheader("Objetivos")

# Ejemplo de objetivos
objetivos = {
    "diarios": {
        "Ahorrar 10L de agua hoy": False,
        "No usar el lavavajillas más de 3 veces al día": False,
    },
    "semanales": {
        "Ahorrar 50L de agua esta semana": False,
        "No dejar el grifo abierto más de 15 minutos al día": False,
    },
    "mensuales": {
        "Ahorrar 200L de agua este mes": False,
        "Reducir el consumo de manguera en un 50%": False,
    }
}

# Mostrar los objetivos y permitir marcar los completados
for tipo, objetivos_lista in objetivos.items():
    st.subheader(tipo.capitalize())
    for objetivo, completado in objetivos_lista.items():
        objetivo_completado = st.checkbox(objetivo, value=completado, key=f"{tipo}_{objetivo}")
        if objetivo_completado:
            st.session_state.objetivos[objetivo] = True
            st.session_state.puntuacion += 10  # Incrementar la puntuación al completar el objetivo

# Botón para guardar la puntuación (si cambia algo)
if st.button("Guardar Progreso"):
    datos_perfil = {
        "nombre": st.session_state.nombre,
        "correo": st.session_state.correo,
        "puntuacion": st.session_state.puntuacion,
        "objetivos": st.session_state.objetivos
    }
    guardar_perfil(usuario_id, datos_perfil)
    st.success("Progreso guardado correctamente.")

# Mostrar la puntuación del usuario
st.write(f"**Puntuación total:** 🌟 {st.session_state.puntuacion} puntos")

# Opcional: Mostrar un mensaje de bienvenida y progreso
st.write("Tu progreso se guarda automáticamente.")
