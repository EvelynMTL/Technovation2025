import streamlit as st
import time

def calcular_gasto_agua(tipo_consumo, minutos):
    # Definir el consumo de agua en litros por minuto para diferentes tipos de consumo
    consumo_por_minuto = {
        'ducha': 9,  # Litros por minuto
        'fregar_platos': 12,  # Litros por minuto
        'lavar_manos': 6,  # Litros por minuto
        'lavar_dientes': 2,  # Litros por minuto
        'lavadora': 10,  # Litros por minuto
        'lavavajillas': 15  # Litros por minuto
    }
    
    # Definir equivalencias
    litros_por_cubo = 10
    litros_por_piscina = 25000
    
    # Calcular el gasto de agua en litros
    if tipo_consumo in consumo_por_minuto:
        gasto_agua_litros = consumo_por_minuto[tipo_consumo] * minutos
    else:
        return "Tipo de consumo no válido."
    
    # Calcular equivalencias
    equivalencia_cubos = gasto_agua_litros / litros_por_cubo
    equivalencia_piscinas = gasto_agua_litros / litros_por_piscina
    
    return {
        'gasto_agua_litros': gasto_agua_litros,
        'equivalencia_cubos': equivalencia_cubos,
        'equivalencia_piscinas': equivalencia_piscinas
    }

# Inicializar variables de estado de sesión
if 'running' not in st.session_state:
    st.session_state.running = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = 0
if 'elapsed_time' not in st.session_state:
    st.session_state.elapsed_time = 0

# Función para iniciar el temporizador
def start_timer():
    st.session_state.start_time = 0
    st.session_state.elapsed_time = 0
    if not st.session_state.running:
        st.session_state.running = True
        st.session_state.start_time = time.time() - st.session_state.elapsed_time

# Función para detener y reiniciar el temporizador
def stop_timer():

    st.session_state.running = False
    #st.session_state.start_time = 0
    #st.session_state.elapsed_time = 0
    escribe_resultado()

# Función para actualizar la visualización del temporizador
def update_timer():
    if st.session_state.running:
        st.session_state.elapsed_time = time.time() - st.session_state.start_time
    minutes, seconds = divmod(st.session_state.elapsed_time, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"


st.title("Cronómetro")
st.write(
    "Cuanto gasto  "
)

#options = ["Ducha", "Animales", "Agua", "OTROS"]
#tipo_consumo = st.pills("Evento", options)
tipo_consumo = st.selectbox("Selecciona el tipo de consumo:", ['ducha', 'fregar_platos', 'lavar_manos', 'lavar_dientes', 'lavadora', 'lavavajillas'])




# Mostrar el temporizador en un campo específico
timer_placeholder = st.empty()


# Botones de inicio y stop
col1, col2 = st.columns(2,vertical_alignment="center")
with col1:
    start_button = st.button("Empezar", on_click=start_timer)
with col2:
    stop_button = st.button("Parar", on_click=stop_timer)

respuesta = st.empty()

def escribe_resultado():
    resultado = calcular_gasto_agua("ducha", 7)
    if isinstance(resultado, dict):
        st.write( resultado )
        respuesta.write({resultado['equivalencia_cubos']}, " cubos de agua" )

        print(f"Equivalente a {resultado['equivalencia_cubos']} cubos de agua")
        print(f"Equivalente a {resultado['equivalencia_piscinas']} piscinas")
  



# Actualizar la visualización del temporizador cada segundo usando un bucle y placeholder
while True:
    timer_display = update_timer()
    timer_placeholder.write(timer_display)
    time.sleep(1)


