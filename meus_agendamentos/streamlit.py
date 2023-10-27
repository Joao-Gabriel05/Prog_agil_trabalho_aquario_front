import streamlit as st
import streamlit.components.v1 as components
style=('agendamento/strimlit.css')
st.markdown("<h1 style='text-align: center;margin-top:-50px;margin-bottom: 80px; color: white;'>App Name</h1>", unsafe_allow_html=True)
st.markdown("<h8 style='color: white;'>Meus Agendamentos:</h8>", unsafe_allow_html=True)
with st.container(): 
    st.markdown(
        """
        <div style='background-color: white; padding:5px; border: 1px solid #ccc; border-radius: 15px; display: flex; justify-content: space-between;'>
            <p style='font-size: 16px; color: #333;'><strong>Nome Período</strong></p>
            <button class="hover-button-remarcar";>Remarcar</button>
            <button class="hover-button-deletar">Deletar</button>
            <style>
                .hover-button-remarcar {
                    display: inline-block;
                    border-radius: 15px;
                    padding: 2px 2px; /* Adicione padding para tornar o botão mais visível */
                    background-color: white; /* Cor azul */
                    color: balck; /* Cor do texto */
                    border: none;
                    cursor: pointer;
                }
                .hover-button-deletar {
                    display: inline-block;
                    border-radius: 15px;
                    padding: 2px 2px; /* Adicione padding para tornar o botão mais visível */
                    background-color:red; /* Cor azul */
                    color: white; /* Cor do texto */
                    border: none;
                    cursor: pointer;
                }

                .hover-button-remarcar:hover {
                    background-color: #0071C5; /* Cor azul mais escura no hover */
                }
                .hover-button-deletar:hover {
                    background-color:rgb(201, 0, 0); /* Cor azul mais escura no hover */
                }
            </style>
        </div>
        """,
        unsafe_allow_html=True
    )