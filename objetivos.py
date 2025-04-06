import streamlit as st
st.title("MIS OBJETIVOS")

if 'score' not in st.session_state:
    st.session_state.score = 0


if st.session_state.score < 2 :
    st.write("Supera nuestro QUIZ y demuestra que eres un experto ")
    st.write("Tienes ", st.session_state.score, " puntos ")
else: 
    st.write("Lo conseguiste :material/star:!  tienes ", st.session_state.score, " puntos ")
    st.write("Sigue asi")


tab1, tab2, tab3 = st.tabs(["Diarios", "Semanales", "Mensuales"])

with tab1:
    st.header("Diarios")
    with st.container():

        col1, col2 = st.columns(2,vertical_alignment="center")
        with col1:

            st.image("https://static.streamlit.io/examples/cat.jpg", width=100)
        with col2:
            st.checkbox("COMPLETADO",key=3)
    with st.container():
        col1, col2 = st.columns(2,vertical_alignment="center")
        with col1:

            st.image("https://static.streamlit.io/examples/cat.jpg", width=100)
        with col2:
            st.checkbox("COMPLETADO",key=1)

with tab2:
    st.header("Semanales")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
