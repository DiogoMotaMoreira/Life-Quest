import streamlit as st
import json
import pandas as pd


with open("dados/info.json", "r", encoding="utf-8") as f:
    data = json.load(f)



st.title("🧭Side Quest")

i = 1
list = []
for q in data.get("quests", []):
    list.append({
        "Feito": False,
        "Nome": q.get("nome", ""),
        "Dificuldade": q.get("dificuldade", 0),
        "Xp": q.get("xp", 0),
        "Coins": q.get("coins", 0),
        "Remove": False
    })

df = pd.DataFrame(list)
edited_df = st.data_editor(df , hide_index=True)


