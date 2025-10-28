import streamlit as st
from imc import imc
from conversor import conv
from cambio import cambio
st.set_page_config("Conversores")

st.title(":blue[Calculos y conversores]")

tab1,tab2,tab3=st.tabs(["IMC","Conversor de unidades","Conversor de moneda"])

with tab1:
    imc()

with tab2:
    conv()

with tab3:
    cambio()