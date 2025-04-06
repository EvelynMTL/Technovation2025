import streamlit as st
import time

def calcular_gasto_agua(tipo_consumo, tiempo_consumo):
  
    # Definir el consumo de agua en litros por minuto para diferentes tipos de consumo
    consumo_por_minuto = {
        'Ducha': 9,  # Litros por minuto
        'Fregar platos': 12,  # Litros por minuto
        'Lavar las manos': 6,  # Litros por minuto
        'Lavar los dientes': 2,  # Litros por minuto
        'Lavadora': 10,  # Litros por minuto
        'Lavavajillas': 15  # Litros por minuto
    }

    
    # Definir equivalencias
    litros_por_cubo = 10
    litros_por_bañera = 150
    
    # Calcular el gasto de agua en litros
    if tipo_consumo in consumo_por_minuto:
        gasto_agua_litros = consumo_por_minuto[tipo_consumo] * tiempo_consumo
    else:
        return "Tipo de consumo no válido."
    
    # Calcular equivalencias
    equivalencia_cubos =int( gasto_agua_litros / litros_por_cubo)
    equivalencia_bañera =gasto_agua_litros / litros_por_bañera
    
    return {
        'gasto_agua_litros': gasto_agua_litros,
        'equivalencia_cubos': equivalencia_cubos,
        'equivalencia_piscinas': round (equivalencia_bañera,2)
    }


# Titulo pagina
st.title("Calculadora")
st.write("Te ayudamos a saber cuanto agua usas en algunas de las acciones más cotidianas")
tipo_consumo = st.selectbox("Selecciona el tipo de consumo:", ['Ducha', 'Fregar platos', 'Lavar las manos', 'Lavar los dientes', 'Lavadora', 'Lavavajillas'],index=None,placeholder="Elige un consumo...")
tiempo_consumo = st.number_input("Selecciona el tiempo (minutos)", value=1, step=1)

if st.button("Calcular"):
    resultado = calcular_gasto_agua(tipo_consumo, tiempo_consumo)
    pintar= st.container(border=True)
    pintar.write(f" :material/water_drop: Gasto de agua: {resultado['gasto_agua_litros']} litros ")
    pintar.write(f":material/colors:  Equivalente a {resultado['equivalencia_cubos']} cubos de agua")
    pintar.write(f":material/bathtub: Equivalente a {resultado['equivalencia_piscinas']} bañeras llenas")






