import streamlit as st
#dicionario ficticio
df = {
    "email": "usuario@example.com",
    "senha": "senha123",
    "nome_completo": "Nome Sobrenome"
}

#login caso ja tenha cadastro
def login():
    st.title("Login")

    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if email == df["email"] and senha == df["senha"]:
            st.success("Login bem-sucedido!")
        else:
            st.error("Email ou senha incorretos.")
#não sei se temos essa api
    if st.button("Esqueceu a senha?"):
        st.write("Você receberá um email para redefinir sua senha.")

#caso seja a primeira vez no app
def cadastro():
    st.title("Cadastro")

    nome_completo = st.text_input("Nome Completo")
    novo_email = st.text_input("Email")
    nova_senha = st.text_input("Senha", type="password")

    if st.button("Cadastrar"):
        df["nome_completo"] = nome_completo
        df["email"] = novo_email
        df["senha"] = nova_senha
        st.success("Conta criada com sucesso! Agora você pode fazer login.")

def roda():
    st.sidebar.title("Menu")
    escolha = st.sidebar.radio("Selecione uma opção", ["Login", "Cadastro"])

    if escolha == "Login":
        login()
    elif escolha == "Cadastro":
        cadastro()

if __name__ == "__main__":
    roda()
