import streamlit as st

st.markdown("<h1 style='text-align: center;margin-top:-50px;margin-bottom: 80px; color: white;'>App Name</h1>", unsafe_allow_html=True)

with st.container():
    st.markdown(
        """
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Escolha de Prédio</title>
            <link rel="stylesheet" type="text/css" href="agendamento/streamlit.css">
        </head>
        <body>
            <h1>Escolha de Prédio</h1>

            <div style="display: flex; justify-content: space-between;">

                <div style="flex: 1;">
                    <img src="stats/imagens/predio1.jpg" alt="Prédio 1" width="200">
                    <button onclick="selecionarPredio(1)">Selecionar Prédio 1</button>
                </div>

                <div style="flex: 1;">
                    <img src="stats/imagens/predio2.jpeg" alt="Prédio 2" width="200">
                    <button onclick="selecionarPredio(2)">Selecionar Prédio 2</button>
                </div>

            </div>

            <script>
                function selecionarPredio(predio) {
                    if (predio === 1) {
                        alert("Colocar rota predio 1");
                    } else if (predio === 2) {
                        alert("Colocar rota predio 2");
                    }
                }
            </script>
        </body>
        """,
        unsafe_allow_html=True
    )
