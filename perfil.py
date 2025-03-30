import streamlit as st


st.title("Perfil de usaurio")
st.title("you are :blue[cool] :sunglasses:")


on = st.toggle("Soy ahorrador")

#if on:
#   st.write("Feature activated!")


options = ["Medio ambiente", "Animales", "Agua", "OTROS"]
if 'key' not in st.session_state:
     st.session_state['perfil_color'] =  "1 al dia",
selection = st.pills("Mis intereses", options, selection_mode="multi", args=st.session_state['perfil_color'] )
#st.markdown(f"Tus intereses: {selection}.")

perfil_color = st.select_slider(
    "Objetivos a  cumplir  ",
    options=[
        "1 al dia",
        "2 dia",
        "3 a la semana",
        "5 al mes",
        "TODOS",
    ],
)
st.session_state['perfil_color'] = perfil_color