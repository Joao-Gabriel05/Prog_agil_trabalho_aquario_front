import streamlit as st

# Carregue o estilo a partir de um arquivo CSS externo
st.markdown("<h1 class='app-title'>App Name</h1>", unsafe_allow_html=True)
st.markdown("<h8 class='white-text'>Meus Agendamentos:</h8>", unsafe_allow_html=True)
with st.container():
    st.markdown(
        """
        <div class='appointment-container'>
            <p class='period-text'><strong>Nome Período</strong></p>
            <button class='hover-button-remarcar'>Remarcar</button>
            <button class='hover-button-deletar'>Deletar</button>
        </div>
        """,
        unsafe_allow_html=True
    )