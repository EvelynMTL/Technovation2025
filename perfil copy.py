import streamlit as st


# Suponiendo que el usuario tiene un ID único (debes adaptar esto a tu sistema de autenticación)
usuario_id = "usuario_123"  # Este valor debe ser dinámico basado en el usuario autenticado

   
st.session_state.puntuacion = 0
st.session_state.objetivos = {}

# Si no existe la puntuación de los juegos, inicialízala
if "puntuacion_juegos" not in st.session_state:
    st.session_state.puntuacion_juegos = 0  # Empezamos con puntuación de 0

# Mostrar la puntuación de los objetivos
puntuacion_total = st.session_state.puntuacion + st.session_state.puntuacion_juegos

# Mostrar la puntuación total combinada en el perfil
st.title("Perfil del Usuario")
st.write(f"**Puntuación Total**: 🌟 {puntuacion_total} puntos")


# Aquí se pueden actualizar los datos del perfil, como nombre o correo.
nombre_usuario = st.text_input("Nombre de Usuario", value="Evelyn")
correo_usuario = st.text_input("Correo Electrónico", value="evelyn .torras")

# Mostrar y actualizar la puntuación de los objetivos
st.write(f"**Puntuación en los objetivos:** {st.session_state.puntuacion}")
st.write(f"**Puntuación en los juegos:** {st.session_state.puntuacion_juegos}")

# Guardar el progreso (si cambia)
if st.button("Guardar progreso"):
    # Guardar la puntuación total combinada (juegos + objetivos) y los datos del perfil en Firebase
    datos_perfil = {
        "nombre": nombre_usuario,
        "correo": correo_usuario,
        "puntuacion": puntuacion_total,
        "objetivos": st.session_state.objetivos
    }
   
    st.success("Progreso guardado correctamente.")

# --- CALCULADORA MEJORADA --- (Si deseas dejar la calculadora aquí)
st.subheader("🧮 Calculadora de consumo de agua")

opciones = {
    "Ducha (10 L/min)": 10,
    "Lavavajillas (12 L/uso)": 12,
    "Lavadora (50 L/uso)": 50,
    "Grifo abierto (9 L/min)": 9,
    "Manguera (15 L/min)": 15
}

fuente = st.selectbox("Selecciona una fuente de consumo de agua:", list(opciones.keys()))
cantidad = st.number_input("¿Cuántos minutos o usos hiciste?", min_value=0)

if st.button("Calcular consumo"):
    litros = opciones[fuente] * cantidad
    cubos = litros / 10
    piscinas = litros / 30000

    st.success(f"""
    💧 **Consumo estimado**:  
    - {litros:.1f} litros  
    - {cubos:.1f} cubos de agua (10 L c/u)  
    - {piscinas:.5f} piscinas olímpicas (30.000 L c/u)
    """)

st.divider()

# --- TEMPORIZADOR EN SEGUNDO PLANO --- (Si lo deseas dejar aquí también)
from datetime import datetime, timedelta

# Inicializar estado si no existe
if "temporizador_activo" not in st.session_state:
    st.session_state.temporizador_activo = False
if "fin_temporizador" not in st.session_state:
    st.session_state.fin_temporizador = None

# Iniciar temporizador
if not st.session_state.temporizador_activo:
    duracion_min = st.number_input("Duración del temporizador (min):", min_value=1, max_value=30, value=5)
    if st.button("Iniciar temporizador"):
        st.session_state.fin_temporizador = datetime.now() + timedelta(minutes=duracion_min)
        st.session_state.temporizador_activo = True
        st.success("🚿 Temporizador iniciado. Puedes seguir navegando.")

# Mostrar tiempo restante
if st.session_state.temporizador_activo:
    tiempo_restante = st.session_state.fin_temporizador - datetime.now()
    if tiempo_restante.total_seconds() > 0:
        minutos = int(tiempo_restante.total_seconds()) // 60
        segundos = int(tiempo_restante.total_seconds()) % 60
        st.info(f"⏳ Tiempo restante: {minutos:02d}:{segundos:02d}")
        st.button("🔁 Actualizar estado")  # para refrescar manualmente
    else:
        st.success("✅ ¡Tiempo terminado! ¡Buen trabajo ahorrando agua!")
        st.session_state.temporizador_activo = False
        st.session_state.fin_temporizador = None
