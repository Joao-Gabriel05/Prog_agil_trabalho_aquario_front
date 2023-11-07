
import streamlit as st

# Dados de exemplo para simular um usuário logado
user_data = {
    "nome": "Usuário de Exemplo",
    "email": "usuario@example.com",
    "senha": "senha123",
}

st.title("Página de Edição de Dados do Usuário")


# Opção para editar os dados
new_nome = st.text_input("Novo Nome", user_data["nome"])
new_email = st.text_input("Novo Email", user_data["email"])
new_senha = st.text_input("Nova Senha", type="password")

# Atualiza os dados do usuário com os novos valores
user_data["nome"] = new_nome
user_data["email"] = new_email
if new_senha:
    user_data["senha"] = new_senha

#Mostra nova senha
st.write("Dados do usuário atualizados:")
st.write(f"Nome: {user_data['nome']}")
st.write(f"Email: {user_data['email']}")
st.write(f"Senha: {user_data['senha']}")
