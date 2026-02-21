import streamlit as st
import requests

API_URL = "http://localhost:3000/predict"

st.title("Klasyfikator Irysów")


st.image("iris.png", caption="https://www.embedded-robotics.com/iris-dataset-classification/")

with st.form("iris_form"):
    sepal_length = st.number_input("Długość działki", value=5.1, min_value=0.0, max_value=10.0)
    sepal_width = st.number_input("Szerokość działki", value=3.5, min_value=0.0, max_value=10.0)
    petal_length = st.number_input("Długość płatka", value=1.4, min_value=0.0, max_value=10.0)
    petal_width = st.number_input("Szerokość płatka", value=0.2, min_value=0.0, max_value=10.0)
    submit = st.form_submit_button("Przewidź")

if submit:
    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    response = requests.post(API_URL, json={"iris_features": data})
    if response.status_code == 200:
        result = response.text
        st.write(f"Przewidziana klasa: {result}")
    else:
        st.error(f"Błąd: {response.status_code}")
        st.error(response.text)