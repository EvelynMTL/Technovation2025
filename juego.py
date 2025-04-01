import streamlit as st

# Definir preguntas y respuestas
questions = [
    "¿Cuántos litros usas en una ducha?",
    "¿Cuál es la capital de Francia?",
    "¿Cuántos continentes hay?",
    "¿Cuál es el punto de ebullición del agua?",
    "¿Cuántos días tiene una semana?"
]

answers = [
    "10 litros",
    "París",
    "7",
    "100 grados Celsius",
    "7 días"
]

# Inicializar variables de estado de sesión
if 'selected_question' not in st.session_state:
    st.session_state.selected_question = None
if 'selected_answer' not in st.session_state:
    st.session_state.selected_answer = None
if 'score' not in st.session_state:
    st.session_state.score = 0



# Diseño de la aplicación en Streamlit
st.title("Demuestra cuanto sabes")

# Mostrar la puntuación

panel_verifica=st.container(border=True)
panel_verifica.write(f"Puntuación: {st.session_state.score}")

col1, col2 = st.columns(2,vertical_alignment="center")
# Mostrar preguntas y respuestas como botones
with col1:
    st.write("Preguntas:")
    for question in questions:
        if st.button(question):
            st.session_state.selected_question = question
with col2:
    st.write("Respuestas:")
    for answer in answers:
        if st.button(answer):
            st.session_state.selected_answer = answer

# Función para verificar si la pregunta y la respuesta seleccionadas coinciden
def check_match():
    if st.session_state.selected_question is not None and st.session_state.selected_answer is not None:
        question_index = questions.index(st.session_state.selected_question)
        answer_index = answers.index(st.session_state.selected_answer)
        if question_index == answer_index:
            st.session_state.score += 1
            with panel_verifica:
                st.success("¡Emparejamiento correcto!")
        else:
            with panel_verifica:
                st.error("¡Emparejamiento incorrecto!")
        st.session_state.selected_question = None
        st.session_state.selected_answer = None


# Verificar si la pregunta y la respuesta seleccionadas coinciden
check_match()