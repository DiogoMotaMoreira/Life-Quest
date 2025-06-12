import streamlit as st
import json

with open("dados/info.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def showCreate():
    st.title("Create Main Quest")
    nome = st.text_input(label="Nome:")
    r_coins = st.number_input(label="Coins:" , min_value=0)
    r_xp = st.number_input(label="Xp:" , min_value=0)

    data["mainQuest"] = {
        "nome": nome,
        "recompensas": {
            "coins": r_coins,
            "xp": r_xp
        }
    }
    
    if st.button("Guardar Main Quest"):
        with open("dados/info.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        st.page_link("1_mainQuest.py")
    




def showMain():
    st.title("🏆Main Quest")

    st.header(nome)

    st.markdown("### Recompensas")
    st.markdown(f"""
    - **{r_coins} C**
    - **{r_xp} XP**
    """)
    # registar a data
    clicked = st.button("Concluida")





mq  = data.get("mainQuest",{})
nome = mq.get("nome", "")
badges = mq.get("badges", [])
recompensas = mq.get("recompensas", {})
r_coins = recompensas.get("coins", 0)
r_xp = recompensas.get("xp", 0)

if nome:
    showMain()
else:
    showCreate()
