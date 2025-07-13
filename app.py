
import streamlit as st
import pandas as pd
import joblib

# Cargar modelo previamente entrenado
model = joblib.load('model.pkl')

st.title("Predicción de intención de compra")

# Campos de entrada para algunas características del dataset
Administrative = st.number_input("Administrative", 0)
Administrative_Duration = st.number_input("Administrative Duration", 0.0)
Informational = st.number_input("Informational", 0)
Informational_Duration = st.number_input("Informational Duration", 0.0)
ProductRelated = st.number_input("Product Related", 0)
ProductRelated_Duration = st.number_input("Product Related Duration", 0.0)
BounceRates = st.number_input("Bounce Rates", 0.0)
ExitRates = st.number_input("Exit Rates", 0.0)
PageValues = st.number_input("Page Values", 0.0)
SpecialDay = st.number_input("Special Day", 0.0)

# Realizar predicción
if st.button("Predecir"):
    X = pd.DataFrame([[Administrative, Administrative_Duration, Informational, Informational_Duration,
                       ProductRelated, ProductRelated_Duration, BounceRates, ExitRates,
                       PageValues, SpecialDay]],
                     columns=['Administrative', 'Administrative_Duration', 'Informational', 'Informational_Duration',
                              'ProductRelated', 'ProductRelated_Duration', 'BounceRates', 'ExitRates',
                              'PageValues', 'SpecialDay'])
    prediction = model.predict(X)[0]
    resultado = "Compra" if prediction else "No Compra"
    st.success(f"Resultado: {resultado}")
