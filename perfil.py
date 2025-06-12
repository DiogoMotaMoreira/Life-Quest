import json
import streamlit as st
import pandas as pd

def openInfo():
    return open("dados/info.json", "r", encoding="utf-8")


f = openInfo()
data = json.load(f)



# Save the info
picture = data.get("image", "")
name  = data.get("name", "")
level = data.get("level", 0)
coins = data.get("coins",0)
xp = data.get("xp", 0)


stats = data.get("stats", {})
quests = data.get("quests", [])
habitos = data.get("habitos", [])


forca = stats.get("Força", 0)
vitalidade = stats.get("Vitalidade", 0)
inteligencia = stats.get("Inteligência", 0)
sabedoria = stats.get("Sabedoria", 0)
carisma = stats.get("Carisma", 0)
destreza = stats.get("Destreza", 0)
sorte = stats.get("Sorte", 0)


if picture:
    st.image(picture, width=200)
st.title(name)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"**Level:** {level}")
with col2:
    st.markdown(f"**XP:** {xp}")
with col3:
    st.markdown(f"**C:** {coins}")

st.header("Character Stats:")

stats_df = pd.DataFrame(
    {"name": ["Força", "Vitalidade", "Inteligência", "Sabedoria", "Carisma", "Destreza", "Sorte"], 
    "points": [forca, vitalidade, inteligencia, sabedoria, carisma, destreza, sorte]}
)
st.dataframe(stats_df, hide_index=True)

#st.markdown("## DASHBOARDS")

#Gráfico de XP por semana

#Dias consecutivos com progresso
#Quests concluídas vs pendentes
#Nível atual + tempo estimado até próximo


