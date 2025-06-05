import streamlit as st

st.title("🏆Main Quest")

st.header("Passar a todas as cadeiras da universidade.")
st.markdown(
    ":red-badge[Díficil] :orange-badge[⚠️ Atenção Máxima]"
)

st.markdown("### Recompensas")
st.markdown("""
- **200 C**
- **100 XP**
""")
# registar a data
clicked = st.button("Concluida")
