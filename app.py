# Nombre: Jared Alejandro Rosas Molina
# Matricula: 365337

import numpy as np
import joblib
import streamlit as st
import pandas as pd

# Se asigna la ruta del archivo, en este caso esta en la misma carpeta entonces solo es necesario
# asignarle el nombre.
#MODEL_PATH = "modelo_entrenado.pkl"

#Se hacen las predicciones del modelo
def predicciones(x, model):
    y = model.predict(x)
    return y


def main ():
    # Se carga el modelo a utilizar
    modelo = joblib.load("modelo_entrenado.pkl")

    st.title("Implementación de VR para predicción de precio de BTC")
    st.write("Nombre: Jared Alejandro Rosas Molina")
    st.write("Matricula: 365337")
# Se le pide al usuario que ingrese los datos necesarios para la predicción
    o = st.text_input("Ingrese precio de entrada: ")
    h = st.text_input("Ingrese precio más alto:")
    l = st.text_input("Ingrese precio más bajo: ")
    c = st.text_input("Ingrese precio de cierre: ")
    r = st.text_input("Ingrese RSI: ")
    sign = st.selectbox(
        "Selecciona un estado:",
        ["Sobreventa", "Sobrecompra", "Normal"])
    if sign == "Sobreventa":
        sign = 1
    elif sign == "Normal":
        sign = 2
    else:
        sign = 0


    
    #Se crea el boton, que cuando se le de clic sera un boleano que dara true y ejecutara todo lo siguiente,
    # y junto con ello la predicción y se muestra en pantalla.
    if st.button("Predecir"):
        x = {
            "Open": [np.float64(o)],
            "High": [np.float64(h)],
            "Low": [np.float64(l)],
            "Close": [np.float64(c)],
            "RSI_14": [np.float64(r)],
            "RSI_Sign": [sign]
        }
        pred = predicciones(pd.DataFrame(x), modelo)

        st.write(f'La predicción de valor de la casa es: {pred[0]}')
    


if __name__ == "__main__":
    main()