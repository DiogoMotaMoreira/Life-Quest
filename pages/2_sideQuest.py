import streamlit as st
import json


with open("dados/info.json", "r", encoding="utf-8") as f:
    data = json.load(f)



st.title("🧭Side Quest")

i = 1
for q in data.get("quests", []):
    st.markdown(
        f"""
        <div style="border:1px solid #ccc; border-radius:8px; padding:16px; margin-bottom:16px;">
            <h3>{q.get("nome", "")}</h3>
            <p><strong>Dificuldade:</strong> {q.get("dificuldade", 0)}</p>
            <p><strong>XP:</strong> {q.get("xp", 0)}</p>
            <p><strong>C:</strong> {q.get("coins", 0)}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.button(f"Concluido {i}")
    i +=1

