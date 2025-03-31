import streamlit as st
import pandas as pd
import numpy as np

# Datos de ejemplo: consumo diario de agua en litros durante los últimos 30 días
data = {
    "day": list(range(1, 31)),
    "consumption": [10, 12, 11, 13, 15, 14, 16, 18, 17, 19, 20, 22, 21, 23, 25, 24, 26, 28, 27, 29, 30, 32, 31, 33, 35, 34, 36, 38, 37, 39]
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
    return predictions

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
    predictions = predict_consumption(future_days)
    prediction_df = pd.DataFrame({"day": future_days, "predicted_consumption": predictions})
    st.write("Predicción del Consumo de Agua para los Próximos {} Días".format(days_to_predict))
    st.write(prediction_df)