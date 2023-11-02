import streamlit as st

st.markdown("<h1 style='text-align: center;margin-top:-50px;margin-bottom: 80px; color: white;'>App Name</h1>", unsafe_allow_html=True)

with st.container():
    st.markdown(
        """
        <style>
            body {
                background-color: red;
            }
            h2 {
                text-align: center;
                margin-top: -50px;
                margin-bottom: 80px;
                color: white;
            }
        </style>
        <form action="/editar_perfil" method="post">
            <h2>Editar Perfil</h2>
            <label for="nome">Nome:</label>
            <input type="text" id="nome" name="nome"><br>
            
            <label for="email">Email:</label>
            <input type="text" id="email" name="email"><br>
            
            <label for="senha">Senha:</label>
            <input type="password" id="senha" name="senha"><br>

            <input type="submit" value="Salvar Alterações">
        </form>
        """
        , unsafe_allow_html=True
    )

