import streamlit as st
st.title("Cronómetro")
st.write(
    "Mide cuanto tiempo tienes el grifo abierto "
)


tab1, tab2,tab3 = st.tabs(["Ducha", "Cepillado Dientes","Fregar platos"])

with tab1:
    st.header("Ducha")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)


with tab2:
    st.header("Semanales")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("Semanales")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

st.button('Empezar')

