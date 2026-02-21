import streamlit as st

st.title("Układ strony")

col1, col2 = st.columns(2)

with col1:
    st.write("Kolumna 1")

with col2:
    st.write("Kolumna 2")


tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("Tab 1")

with tab2:
    st.write("Tab 2")

with tab3:
    st.write("Tab 3")

with st.container():
    st.write("To jest w kontenerze")

with st.expander("Rozwiń mnie"):
    st.write("To jest w rozwijanym kontenerze")