import streamlit as st

def main():
    st.title("Escolha de Prédio")

    # Exiba as imagens dos prédios lado a lado
    col1, col2 = st.columns(2)

    with col1:
        img_predio1 = st.image("stats\imagens\predio1.jpg", caption="Prédio 1", width=200,)
        button_predio1 = st.button("Selecionar Prédio 1")

    with col2:
        img_predio2 = st.image("stats\imagens\predio2.jpeg", caption="Prédio 2", width=200)
        button_predio2 = st.button("Selecionar Prédio 2")

    # Verifique qual botão foi clicado
    if button_predio1:
        st.write("Colocar rota predio1 ")
    elif button_predio2:
        st.write("Colocar rota predio 2")

if __name__ == "__main__":
    main()