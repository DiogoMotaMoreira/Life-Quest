import streamlit as st
import json
from datetime import datetime

with open("dados/info.json", "r", encoding="utf-8") as f:
    data = json.load(f)


habitos = data.get("habitos", [])
data_hoje = datetime.now().strftime("%Y-%m-%d")

ultimo_registo = habitos[-1] if habitos else {}
ja_registado_hoje = ultimo_registo.get("data") == data_hoje

# if ja_registado_hoje:
#     nhe = ultimo_registo.get("estudo")
#     nht = ultimo_registo.get("trabalho")
#     sleep = ultimo_registo.get("sono")
#     força =  ultimo_registo.get("força")
#     corrida = ultimo_registo.get("corrida")
#     sprint = ultimo_registo.get("sprint")
#     
#     complet = ultimo_registo.get("tarefas_diarias")
# else:
#     nhe = 0
#     nht = 0
#     sleep = False
#     força = False
#     complet = False



st.title("📅 Registo Diário")

st.markdown("### Força")
st.checkbox("Treino físico (20+ min)")
st.checkbox("Caminhada/corrida/bicicleta")

st.markdown("### Vitalidade")
st.checkbox("Dormir 7-8h")
st.checkbox("Beber 2L de água")
st.checkbox("Comer 3 refeições saudáveis")
st.checkbox("Meditação/respiração (5 min)")

st.markdown("### Inteligência")
st.checkbox("Ler por 20 min")
st.checkbox("Resolver 1 desafio mental (quebra-cabeça, lógica, etc.)")
st.checkbox("Estudar algo novo (idioma, programação, etc.)")

st.markdown("### Saberdoria")
st.checkbox("Escrever no diário (reflexão ou lição do dia)")
st.checkbox("Praticar gratidão (3 coisas positivas)")
st.checkbox("Conversar com alguém mais experiente")

st.markdown("### Carisma")
st.checkbox("Fazer 1 nova interação/conversa")
st.checkbox("Escutar com atenção (sem interromper)")
st.checkbox("Participar de grupo/evento social")

st.markdown("### Destreza")
st.checkbox("Tocar instrumento/desenhar/jogo de reflexo")
st.checkbox("Yoga, dança ou alongamento")
st.checkbox("Atividade de coordenação (manualidade, arte, etc.)")

st.markdown("### Sorte")
st.checkbox("Dizer “sim” a algo novo")
st.checkbox("Explorar algo fora da rotina")
st.checkbox("Jogar algo leve por diversão")
st.checkbox("Anotar uma “coincidência positiva” do dia")










if st.button("Guardar Registo"):
    h = {
        "data": data_hoje,
        "estudo": nhe,
        "trabalho": nht,
        "força": força,
        
        "sono": sleep,
        "tarefas_diarias": complet
    }
    if ja_registado_hoje:
        habitos[-1] = h  # Atualiza o último registo
    else:
        habitos.append(h)  # Adiciona novo registo
    
    data["habitos"] = habitos

    with open("dados/info.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    st.success("Registo guardado com sucesso!")




