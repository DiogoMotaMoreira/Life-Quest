import streamlit as st

st.title("📅 Registo Diário")

#15 xp/h
st.number_input("Número de Horas de Estudo:", step=1, min_value=0)
#20 xp/h
st.number_input("Número de Horas de Trabalho:", step=1, min_value=0)

st.checkbox("Dormiste +7h?")
st.checkbox("Cumpriste todas as tarefas de hoje?")


