import streamlit as st


st.title("Perfil de usaurio")
st.title("you are :blue[cool] :sunglasses:")


on = st.toggle("Soy ahorrador")

#if on:
#   st.write("Feature activated!")


options = ["Medio ambiente", "Animales", "Agua", "OTROS"]

selection = st.pills("Mis intereses", options, selection_mode="multi")

if 'perfil_color' not in st.session_state:
     st.session_state['perfil_color'] =  "1 al dia"
perfil_color = st.select_slider(
    "Objetivos a  cumplir  ",
    options=[
        "1 al dia",
        "2 dia",
        "3",
        "5 al mes",
        "TODOS",
    ],value=st.session_state.perfil_color
)
st.session_state['perfil_color'] = perfil_color