import streamlit as st

def main():
    st.markdown("""<h1 style='text-align: center;margin-top:-50px;margin-bottom: 80px; color: white;'>App Name</h1>
        <style>
        body {
            background-color: red;
        }
        </style>
    """, unsafe_allow_html=True)
    st.title("Editar Perfil")
    nome = st.text_input("Nome:")
    email = st.text_input("Email:")
    senha = st.text_input("Senha:",type="password")
    senha_denovo=st.text_input("Digite a senha de novo:",type="password")
    if st.button("Salvar Alterações") and senha_denovo==senha:
        # Exiba os detalhes do perfil após salvar
        st.success(f"Perfil Atualizado:\n\nNome: {nome} \n\nEmail: {email} \n\n Senha: {senha}")

if __name__ == "__main__":
    main()


