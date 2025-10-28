import streamlit as st
import requests

def cambio():
    st.subheader("Tipo de cambio")

    currencies =[
        ("USD","Dolar estadounidense"),
        ("ARS","Peso argentino"),
        ("EUR","Euro"),
        ("GBP","Libra esterlina"),
        ("JPY","Yen japones"),
        ("KRW","Won surcoreano"),
        ("CNY","Yuan chino"),
        ("INR","Rupia india"),
        ("MXN","Peso mexicano"),
        ("CAD","Dolar canadiense"),
        ("CHF","Franco suizo"),
        ("BRL","Real brasileño")
    ]
    
    cc1,cc2,cc3= st.columns(3)
    moneda = cc1.number_input("Moneda",step=1,value=1)

    with cc2:
        moneda_origen = st.selectbox("Moneda Origen", options=[item[1] for item in currencies])
        codigo_origen = next(item[0] for item in currencies if item[1] == moneda_origen)

        st.write(f"{codigo_origen}")

    with cc3:
        moneda_destino = st.selectbox("Moneda Destino", options=sorted([item[1] for item in currencies]))
        codigo_destino = next(item[0] for item in currencies if item[1] == moneda_destino)
        
        st.write(f"{codigo_destino}")


    api_key = st.secrets["general"]["API_KEY"]

    url = f"http://apilayer.net/api/live?access_key={api_key}&currencies={codigo_destino}&source={codigo_origen}&format=1"

    if st.button("Convertir", type="primary"):

        response = requests.get(url)
        data = response.json()

        tipo_cambio = data['quotes'][f"{codigo_origen}{codigo_destino}"]
        res_moneda = moneda * tipo_cambio
        st.subheader(f"{moneda} {moneda_origen} equivale a :orange[{res_moneda:.2f}] {moneda_destino}")



