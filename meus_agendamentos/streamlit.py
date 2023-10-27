
import streamlit.components.v1 as components
import requests 
import streamlit as st
import pandas as pd

st.title('Meus Agendamentos:')
df = pd.DataFrame(
    [
       {"Horário": "16:00", "Local":'P1', "Andar":"3",'Aquario':"3"},
   ]
)
df2 = pd.DataFrame(
    [
       {"Horário": "16:00", "Local":'P1', "Andar":"3",'Aquario':"3"},
   ]
)
# edited_df = st.data_editor(df, num_rows="fixed")

# favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
# st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
st.dataframe(
    df,hide_index=True, 
)
check1=st.checkbox('Deletar 1')
st.write('---')
st.dataframe(
    df2,hide_index=True, 
)
check2=st.checkbox('Deletar 2')
st.link_button('Remarcar','https://insper.avaliar.org/')

if check1:
    st.warning('deletei')