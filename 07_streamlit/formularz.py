import streamlit as st

st.title("Sages")
st.write("Witaj w aplikacji Sages!")

st.sidebar.header("Menu")
param = st.sidebar.slider("Wartość parametru", 0, 100, 50)

if st.button("Kliknij mnie"):
    st.write(f"Wartość parametru: {param}")
    st.success("Kliknięto przycisk!")

st.subheader("Elementy wejściowe")

name = st.text_input("Imię")
desc = st.text_area("Opis")

age = st.number_input("Wiek", value=20, min_value=0, max_value=100)
height = st.slider("Wzrost", value=170, min_value=0, max_value=250)

option = st.selectbox("Wybierz opcję", ["Opcja 1", "Opcja 2", "Opcja 3"])
options = st.multiselect("Wybierz opcje", ["Opcja 1", "Opcja 2", "Opcja 3"])

date = st.date_input("Wybierz datę")
file_name = st.file_uploader("Wybierz plik", type=["py"])

switch = st.toggle("Włącz/Wyłącz")

check = st.checkbox("Zaznacz mnie")

if switch:
    if st.button("Zapisz"):
        st.write(f"Imię: {name}")
        st.write(f"Opis: {desc}")
        st.write(f"Wiek: {age}")
        st.write(f"Wzrost: {height}")
        st.write(f"Opcja: {option}")
        st.write(f"Opcje: {options}")
        st.write(f"Data: {date}")
        st.write(f"Plik: {file_name}")
        st.write(f"Switch: {switch}")
        st.write(f"Check: {check}")
