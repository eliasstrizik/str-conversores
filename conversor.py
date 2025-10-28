import streamlit as st

def conv():
    st.subheader("Conversor de unidades")

    def conversor_unidades(valor, origen, destino):

        conversion_unidades = {
            "milimetros": 0.1,
            "centimetros": 1,
            "metros": 100,
            "Kilometros": 100000,

        }
        valor_centimetros = valor * conversion_unidades[origen]
        result = valor_centimetros / conversion_unidades[destino]
        return result
    unidades = ["milimetros","centimetros","metros","kilometros"]

    col1,col2,col3 = st.columns(3)
    valor = col1.number_input("Valor a convertir", min_value=0.0,value=1.0)
    origen   = col2.selectbox("Unidad de origen", unidades)
    destino  = col3.selectbox("Unidad de destino", unidades)


    if st.button("Convertir"):
        result = conversor_unidades(valor,origen,destino)
        st.subheader(f"{valor} {origen} son equivalentes a {result:.2f} {destino}")

