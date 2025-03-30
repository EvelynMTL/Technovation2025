import streamlit as st
import time

# Inicializar variables de estado de sesión
if 'running' not in st.session_state:
    st.session_state.running = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = 0
if 'elapsed_time' not in st.session_state:
    st.session_state.elapsed_time = 0

# Función para iniciar el temporizador
def start_timer():
    if not st.session_state.running:
        st.session_state.running = True
        st.session_state.start_time = time.time() - st.session_state.elapsed_time

# Función para detener y reiniciar el temporizador
def stop_timer():
    st.session_state.running = False
    st.session_state.start_time = 0
    st.session_state.elapsed_time = 0

# Función para actualizar la visualización del temporizador
def update_timer():
    if st.session_state.running:
        st.session_state.elapsed_time = time.time() - st.session_state.start_time
    minutes, seconds = divmod(st.session_state.elapsed_time, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

# Diseño de la aplicación en Streamlit
st.title("Timer App")

# Mostrar el temporizador en un campo específico
timer_placeholder = st.empty()

# Botones de inicio y stop
col1, col2 = st.columns(2,vertical_alignment="center")
with col1:
    start_button = st.button("Start", on_click=start_timer)
with col2:
    stop_button = st.button("Stop", on_click=stop_timer)

# Actualizar la visualización del temporizador cada segundo usando un bucle y placeholder
while True:
    timer_display = update_timer()
    timer_placeholder.write(timer_display)
    time.sleep(1)


