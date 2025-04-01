import streamlit as st
import pandas as pd
import numpy as np

# Generar datos de ejemplo: consumo diario de agua en litros durante los últimos 30 días
np.random.seed(42)
days = list(range(1, 31))
consumption = np.random.randint(10, 20, size=30)
data = {
    "day": days,
    "consumption": consumption
}

# Convertir datos a DataFrame
df = pd.DataFrame(data)

# Función para predecir el consumo futuro utilizando una regresión lineal simple
def predict_consumption(days):
    # Calcular los coeficientes de la regresión lineal
    x = np.array(df["day"])
    y = np.array(df["consumption"])
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)
    
    # Predecir el consumo futuro
    future_days = np.array(days)
    predictions = m * future_days + c
    return future_days, predictions

# Diseño de la aplicación en Streamlit
st.title("Predicción del Consumo de Agua")

# Mostrar datos de ejemplo
st.write("Datos de Ejemplo: Consumo Diario de Agua durante los Últimos 30 Días")
st.write(df)

# Entrada para el número de días a predecir
days_to_predict = st.number_input("Introduce el número de días a predecir:", min_value=1, max_value=30)

# Predecir el consumo futuro y mostrar los resultados
if st.button("Predecir"):
    future_days = list(range(31, 31 + days_to_predict))
    future_days, predictions = predict_consumption(future_days)
    prediction_df = pd.DataFrame({"day": future_days, "predicted_consumption": predictions})
    st.write("Predicción del Consumo de Agua para los Próximos {} Días".format(days_to_predict))
    st.write(prediction_df)