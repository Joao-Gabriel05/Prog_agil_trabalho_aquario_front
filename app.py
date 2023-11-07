import streamlit as st
import requests
from constantes import *

#login caso ja tenha cadastro
def login():
    st.title("Login")

    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        resposta = requests.post(f'{API}/login', json={"email": email, "senha": senha})
        if resposta.status_code == 200:
            if email == "admin@admin":
                st.session_state.admin = True
            st.success("Login bem-sucedido!")
            st.session_state.logado = True
            st.experimental_rerun()
        else:
            st.error(f"Email ou senha incorretos.{resposta.status_code}")

#caso seja a primeira vez no app
def cadastro():
    st.title("Cadastro")

    nome_completo = st.text_input("Nome Completo")
    novo_email = st.text_input("Email")
    nova_senha = st.text_input("Senha", type="password")

    if st.button("Cadastrar"):
        resposta = requests.post(f'{API}/usuarios', json={"nome": nome_completo, "email": novo_email, "senha": nova_senha})
        if resposta.status_code == 201:
            st.success("Conta criada com sucesso!")
            st.session_state.logado = True
            st.experimental_rerun()
        else:
            st.error(resposta.json()['erro'])
        
def menu_login_cadastro():
    st.sidebar.title("Menu")
    escolha = st.sidebar.radio("Selecione uma opção", ["Login", "Cadastro"])

    if escolha == "Login":
        login()
    elif escolha == "Cadastro":
        cadastro()

def listar_aquarios(predio):
    resposta = requests.get(f'{API}/aquarios')
    data = resposta.json()
    if resposta.status_code == 200:
        for aquario in data['aquarios']:
            with st.container():
                if 'img' in aquario:
                    st.image('https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80')
                st.button(f"Nome: {aquario['nome']} Local: {aquario['local']}")
    else:
        st.error(data['erro'])
    
def menu_predio():
    st.sidebar.title("Menu")
    escolha = st.sidebar.radio("Selecione o prédio", ["P1", "P2"])

    listar_aquarios(escolha)

def aquarios_admin():
    tab1, tab2, tab3 = st.tabs(['Cadastrar', 'Editar', 'Deletar'])
    with tab1:
        st.title("Cadastro")

        nome = st.text_input("Nome do aquario")
        local = st.text_input("Local do aquario Ex: P1, 2 andar")
        foto = st.file_uploader("Foto do aquario")

        if st.button("Cadastrar"):
            resposta = requests.post(f'{API}/usuarios', json={"nome": nome, "local": local, "foto": foto})
            if resposta.status_code == 201:
                st.success("Conta criada com sucesso!")
                st.session_state.logado = True
                st.experimental_rerun()
            else:
                st.error(resposta.json()['erro'])

def menu_admin():
    st.sidebar.title("Menu")
    escolha = st.sidebar.radio("Selecione o recurso", ["Aquarios"])

    aquarios_admin()

def roda():

    if "logado" not in st.session_state:
        st.session_state.logado = False
    if "admin" not in st.session_state:
        st.session_state.admin = False

    if not st.session_state.logado:
        menu_login_cadastro()
    elif st.session_state.admin:
        menu_admin()
    else:
        menu_predio()

if __name__ == "__main__":
    roda()