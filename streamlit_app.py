import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
home  =st.Page("home.py", title="Inicio", icon=":material/home:")
perfil = st.Page("perfil.py", title="Perfil", icon=":material/face:")
objetivos = st.Page("objetivos.py", title="Objetivos", icon=":material/new_releases:")
iniciativas = st.Page("iniciativas.py", title="Iniciativas", icon=":material/arrow_split:")
chat =st.Page("chat.py", title="Chat", icon=":material/chat:")
tiempo = st.Page("temporizador.py", title="Cronómetro", icon=":material/timer:")

pg = st.navigation([home,perfil,objetivos,iniciativas,chat,tiempo])
pg.run()


#if st.session_state.logged_in:
 #  st.navigation([home,perfil,iniciativas,chat,tiempo])
#else:
 #  pg = st.navigation([login_page])