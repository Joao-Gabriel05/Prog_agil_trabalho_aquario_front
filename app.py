import streamlit as st
import requests
from constantes import *
from datetime import datetime
from functions import *

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
            verifica_agendamento()
            st.session_state.id_usuario = resposta.json()['sucesso']
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
            st.session_state.id_usuario = resposta.json()['sucesso']
            st.experimental_rerun()
        else:
            st.error(resposta.json()['erro'])

def tela_edicao():
    st.title("Editar Cadastro")

    usuario_atual = st.session_state.usuario_atual

    nome_completo = st.text_input("Nome Completo", value=usuario_atual.get('nome', ''))
    novo_email = st.text_input("Email", value=usuario_atual.get('email', ''))
    nova_senha = st.text_input("Nova Senha", type="password")

    if st.button("Salvar Alterações"):
        dados_usuario = {"nome": nome_completo, "email": novo_email, "senha": nova_senha}
        resposta = requests.put(f'{API}/usuarios/{usuario_atual["id"]}', json=dados_usuario)

        if resposta.status_code == 200:
            st.success("Cadastro atualizado com sucesso!")
            st.experimental_rerun()
        else:
            st.error(resposta.json().get('erro', 'Erro desconhecido'))


        
def menu_login_cadastro():
    st.sidebar.title("Menu")
    escolha = st.sidebar.radio("Selecione uma opção", ["Login", "Cadastro"])

    if escolha == "Login":
        login()
    elif escolha == "Cadastro":
        cadastro()

def listar_aquarios(predio):
    tab1, tab2 = st.tabs(['Agendar', 'Meus Agendamentos'])
    
    with tab1:
        st.title('Selecione o aquario para agendar')

        resposta = requests.get(f'{API}/aquarios')
        data = resposta.json()
        if resposta.status_code == 200:
            lista1 = []
            lista2 = []
            for aquario in data['aquarios']:
                if predio in aquario['local']:
                    lista1.append(f'Nome: {aquario["nome"]}; Local: {aquario["local"]}')
                    lista2.append(aquario["_id"])

            if not lista1:
                st.write('sem aquarios disponiveis')
            else:
                aquario_ecolhido = st.radio('Aquarios:',options=lista1, captions=lista2)

                # Obtendo a data atual
                data_atual = datetime.now().date()

                # Encontrando o próximo dia útil após dois dias a partir da data atual
                data_dia_util = proximo_dia_util(data_atual)

                # Widget para seleção de data a partir do dia útil encontrado
                dia = st.date_input("Selecione uma data", min_value=data_atual, max_value=data_dia_util)

                resposta = requests.get(f'{API}/aquarios/{lista2[lista1.index(aquario_ecolhido)]}')
                json = resposta.json()

                horarios_ocupados = []

                if 'agendamentos' in json['aquario']:
                    for agendamento in json['aquario']['agendamentos']:
                        horarios_ocupados.append(int(agendamento['agendamento'].split('-')[1][:1]))

                    # Horários já ocupados (simulados para o exemplo)
                    # horarios_ocupados = [datetime.strptime("13:00", "%H:%M").time(), datetime.strptime("16:30", "%H:%M").time()]

                # Obtendo o próximo horário disponível
                horario_disponivel = hora_disponivel(horarios_ocupados)

                # Widget para seleção de horário a partir do próximo horário disponível
                hora = st.time_input("Escolha um horário", horario_disponivel, step=3600)

                hora_atual = str(datetime.now().replace(second=0, microsecond=0)).split()[1][:2]

                if st.button('Agendar'):
                    if 7 <= int(str(hora)[:2]) <= 22 and int(hora_atual) <= int(str(hora)[:2]) and int(str(hora)[:2]) not in horarios_ocupados:
                        resposta = requests.post(f'{API}/agendamentos/usuario/{st.session_state.id_usuario}/aquario/{lista2[lista1.index(aquario_ecolhido)]}',json={"agendamento": f"{dia.strftime('%d/%m/%Y')}-{int(str(hora)[:2])}_{int(str(hora)[:2])+1}"})
                        if resposta.status_code == 200:
                            st.success('agendamento realizado')
                        else:
                            st.error(resposta.json()['erro'])
                    else:
                        st.error('horario invalido')

    with tab2:
        st.title('Meus Agendamentos')
        
        resposta = requests.get(f'{API}/usuarios/{st.session_state.id_usuario}')
        data = resposta.json()
        if resposta.status_code == 200:
            lista1 = []
            lista2 = []
            if 'agendamentos' in data['usuario']:
                for agendamento in data['usuario']['agendamentos']:
                    lista1.append(f'Data: {agendamento["agendamento"].split("-")[0]}; Hora: das {agendamento["agendamento"].split("-")[1].split("_")[0]}hrs até as {agendamento["agendamento"].split("-")[1].split("_")[1]}hrs')
                    lista2.append(f'Nome: {agendamento["aquario"]["nome"]}; Local: {agendamento["aquario"]["local"]}; id: {agendamento["aquario"]["_id"]}')

            if not lista1:
                st.write('sem agendamentos')
            else:
                agendamento_escolhido = st.radio('Agendamentos:',options=lista1, captions=lista2)

            # if st.button("Deletar Agendamento"):
            #     id_aquario = lista2[lista1.index(agendamento_escolhido)].split(';')[2][4:]
            #     st.write(id_aquario)
            #     deletado = data['usuario']['agendamentos'][lista1.index(agendamento_escolhido)]
            #     del data['usuario']['agendamentos'][lista1.index(agendamento_escolhido)]
            #     del data['usuario']['_id']
            #     if requests.put(f'{API}/usuarios/{st.session_state.id_usuario}', json=data).status_code == 200:

            #         print('oi')
            #         resposta = requests.get(f'{API}/aquarios/{id_aquario}')
            #         if resposta.status_code == 200:
            #             data = resposta.json()
            #             data['aquario']['agendamentos'].remove(deletado)
            #             del data['aquario']['_id']
            #             if requests.put(f'{API}/aquarios/{id_aquario}', json=data).status_code == 200:
            #                 st.success('deletado com sucesso')

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

        if st.button("Cadastrar"):
            resposta = requests.post(f'{API}/aquarios', json={"nome": nome, "local": local})
            if resposta.status_code == 201:
                st.success("aquario criado com sucesso!")
            else:
                st.error(resposta.json()['erro'])

    with tab2:
        st.title('Selecione o aquario para editar')

        resposta = requests.get(f'{API}/aquarios')
        data = resposta.json()
        if resposta.status_code == 200:
            lista1 = []
            lista2 = []
            for aquario in data['aquarios']:
                lista1.append(f'Nome: {aquario["nome"]}; Local: {aquario["local"]}')
                lista2.append(aquario["_id"])
            aquario_ecolhido = st.radio('Aquarios:',options=lista1, captions=lista2)

            nome = st.text_input("Nome do aquario", aquario_ecolhido.split(';')[0])
            local = st.text_input("Local do aquario Ex: P1, 2 andar", aquario_ecolhido.split(';')[1])

            if st.button('Atualizar Aquario'):
                resposta = requests.put(f'{API}/aquarios/{lista2[lista1.index(aquario_ecolhido)]}', json={"nome": nome, "local": local})
                if resposta.status_code == 200:
                    st.success('atualizado com sucesso')
                    st.experimental_rerun()
                else:
                    st.error(resposta.json()['erro'])

    with tab3:
        st.title('Selecione o aquario para deletar')

        resposta = requests.get(f'{API}/aquarios')
        data = resposta.json()
        if resposta.status_code == 200:
            lista1 = []
            lista2 = []
            for aquario in data['aquarios']:
                lista1.append(f'Nome: {aquario["nome"]}; Local: {aquario["local"]}')
                lista2.append(aquario["_id"])
            aquario_ecolhido = st.radio('Aquarios:',options=lista1, captions=lista2, key='radio_aquario_deletar')

            if st.button('Deletar Aquario'):
                resposta = requests.delete(f'{API}/aquarios/{lista2[lista1.index(aquario_ecolhido)]}')
                if resposta.status_code == 200:
                    st.success('deletado com sucesso')
                    st.experimental_rerun()
                else:
                    st.error(resposta.json()['erro'])

def verifica_agendamento():

    agora = datetime.now().replace(second=0, microsecond=0)

    data_atual = str(agora).split()[0]
    hora_atual = str(agora).split()[1][:2]

    resposta = requests.get(f'{API}/aquarios')
    json = resposta.json()

    for aquario in json['aquarios']:
        if 'agendamentos' in aquario:
            for agendamento in aquario['agendamentos']:
                entrada_horario = agendamento['agendamento']
            
                data, hora = entrada_horario.split('-')
                if data[:2] < data_atual[-1:-3]:
                    return True
                    
                elif data[:2] == data_atual[-1:-3]:
                    hora_desejada = str(hora)[:2]
                    if int(hora_desejada) <= int(hora_atual):
                        id = aquario["_id"]
                        del aquario["_id"]
                        aquario['agendamentos'].remove(agendamento)
                        resposta = requests.put(f'{API}/aquarios/{id}', json=aquario)


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
