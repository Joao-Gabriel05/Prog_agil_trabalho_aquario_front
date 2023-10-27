import streamlit as st
import datetime

st.title("Agende seu Aquário")

d = datetime.timedelta(days=7)

st.date_input("Selecione uma data para agendar:", min_value=datetime.datetime.now(), max_value=(datetime.datetime.now()+d))

h = st.time_input("Selecione um horário:", value=None, step=3600)

b = st.button("Agendar")
if b:
    st.write("Aquário agendado às:", h)