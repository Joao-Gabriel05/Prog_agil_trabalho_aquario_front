import streamlit as st
from datetime import datetime, timedelta

def proximo_dia_util(data):
    # Definindo um intervalo de 2 dias úteis (excluindo sábado e domingo)
    dias_uteis = 0
    while dias_uteis < 2:
        data += timedelta(days=1)
        if data.weekday() not in [5, 6]:  # 5 = sábado, 6 = domingo
            dias_uteis += 1
    return data

def hora_disponivel(horarios_ocupados):
    hora_atual = datetime.now().replace(second=0, microsecond=0)  # Obtém a hora atual

    # Ajusta a hora para 7h, início do intervalo
    hora = hora_atual.replace(hour=7, minute=0)

    # Define o final do intervalo às 22h
    hora_fim = hora_atual.replace(hour=22, minute=0)

    intervalo = timedelta(hours=1)

    while hora <= hora_fim:
        if hora not in horarios_ocupados and hora > hora_atual:
            return hora.time()
        hora += intervalo


agora = datetime.now().replace(second=0, microsecond=0)

data_atual = str(agora).split()[0]
hora_atual = str(agora).split()[1][:2]

print(data_atual, hora_atual)