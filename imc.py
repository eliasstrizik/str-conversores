import streamlit as st
import pandas as pd
def imc():
    st.subheader("Indice de Masa Corporal")

    st.latex(r"\text{IMC} = \frac{\text{Peso (kg)}} {\text{Altura(m)}^2} ")

    st.markdown("**Tabla de IMC segun la OMS**")

    datos_imc = {
        "Categoria": [
            "Peso insuficiente",
            "Peso normal",
            "Sobrepeso",
            "Obesidad grado 1",
            "Obesidad grado 2",
            "Obesidad grado 3 (Mórbida)"
        ],
        "Rango de IMC": [
            "menor a 18.5",
            "18.5 – 24.9",
            "25.0 – 29.9",
            "30.0 – 34.9",
            "35.0 – 39.9",
            "≥ 40.0"
        ]
    }
    
    tabla_imc = pd.DataFrame(datos_imc)
    st.table(tabla_imc)

    c1,c2 = st.columns(2)
    peso = c1.number_input("Peso", step=1.5)
    altura = c2.number_input("Altura")

    def imc_calc(peso, altura):
        if altura <= 0 or peso <= 0:
            return None, "La altura y el peso deben ser mayores que 0", False
        imc = peso / (altura**2)
        show_video = imc >= 30
        msg = f"Tu IMC es: {imc:.2f}"
        return imc, msg, show_video


    if st.button("Calcular", type="primary"):
        imc, msg, show_video = imc_calc(peso, altura)
        if imc is None:
            st.error(msg)
        else:
            st.success(msg)
            if show_video:
                st.video("https://www.youtube.com/watch?v=a1Q50KpvLYA", width=500)