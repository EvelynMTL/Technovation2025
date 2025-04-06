import streamlit as st
#definimos nuestro logo


sidebar_logo =  "imagenes/gota.jpeg"
main_body_logo =  "imagenes/gota.jpeg"

st.logo(sidebar_logo, icon_image=main_body_logo)

home  =st.Page("home.py", title="Inicio", icon=":material/home:")
perfil = st.Page("perfil.py", title="Perfil", icon=":material/face:")
objetivos = st.Page("objetivos.py", title="Objetivos", icon=":material/new_releases:")
iniciativas = st.Page("iniciativas.py", title="Iniciativas", icon=":material/arrow_split:")
chat =st.Page("chat.py", title="Chat", icon=":material/chat:")
tiempo = st.Page("calculadora.py", title="Calculadora", icon=":material/calculate:")
juego =st.Page("juego.py", title="Quiz", icon=":material/quiz:")
prediccion =st.Page("predictor.py", title="Predictor de consumo", icon=":material/quiz:")
pg = st.navigation([home,perfil,objetivos,iniciativas,chat,juego,tiempo])
pg.run()
