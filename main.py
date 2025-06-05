import json
import streamlit as st

# Carregar dados do ficheiro JSON
with open("dados/info.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Guardar info em variáveis
nivel = data.get("nivel", 0)
xp = data.get("xp", 0)
quests = data.get("quests", [])
habitos = data.get("habitos", [])

# Calcular XP ganho em estudo e trabalho de todos os dias
xp_estudo_total = sum(h["estudo"] * 15 for h in habitos)
xp_trabalho_total = sum(h["trabalho"] * 20 for h in habitos)


st.image("https://cdn.iconscout.com/icon/free/png-256/free-avatar-icon-download-in-svg-png-gif-file-formats--user-boy-avatars-flat-icons-pack-people-456322.png")
st.title("DIOGO MOREIRA")
st.markdown(f"**Level:** {nivel}  \n **XP:** {xp}")

st.header("Character Stats:")
st.markdown(f"**Sabedoria (XP ganho em estudo)**: {xp_estudo_total}")
st.markdown(f"**Criação (XP ganho em projeto)**: {xp_trabalho_total}")
st.markdown(f"**Foco (dias seguidos com todas as tarefas concluídas)**")
st.markdown(f"**Energia (média de sono nos últimos 7 dias)**")

st.markdown("## DASHBOARDS")
#Gráfico de XP por semana
#Dias consecutivos com progresso
#Quests concluídas vs pendentes
#Nível atual + tempo estimado até próximo


