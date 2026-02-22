"""
Główny plik aplikacji Todolist (Streamlit).
Aplikacja jednoużytkownikowa z persystencją w SQLite3.
"""
import streamlit as st

from db import (
    init_db,
    get_corrupt_message,
    add_task,
    get_tasks,
    complete_task,
    delete_task,
    ValidationError,
)

st.set_page_config(page_title="Todolist", layout="centered")
st.title("Todolist")

# Inicjalizacja bazy przy starcie (FR-008)
init_db()

# Komunikat przy uszkodzonej bazie (FR-008, T015)
corrupt_msg = get_corrupt_message()
if corrupt_msg:
    st.warning(corrupt_msg)

# Formularz dodawania zadania (T006, FR-006, FR-007)
with st.form("add_task_form", clear_on_submit=True):
    title_input = st.text_input("Tytuł *", placeholder="Tytuł zadania", max_chars=200)
    description_input = st.text_area(
        "Opis (opcjonalnie)", placeholder="Opis", max_chars=2000, height=80
    )
    submitted = st.form_submit_button("Dodaj")
    if submitted:
        try:
            add_task(title_input or "", description_input or "")
            st.success("Zadanie dodane.")
            st.rerun()
        except ValidationError as e:
            st.error(str(e))

# Filtr listy (T008, T009, FR-003)
filter_choice = st.radio(
    "Filtr",
    options=["Wszystkie", "Aktywne", "Ukończone"],
    horizontal=True,
    key="filter",
)
filter_map = {"Wszystkie": "all", "Aktywne": "active", "Ukończone": "completed"}
filter_kind = filter_map[filter_choice]

# Lista zadań (T007, T010–T013)
tasks = get_tasks(filter_kind)

if not tasks:
    st.info("Brak zadań. Dodaj pierwsze zadanie.")  # FR-009, T014
else:
    for task_id, title, description, completed in tasks:
        with st.container():
            col1, col2 = st.columns([4, 1])
            with col1:
                if completed:
                    st.markdown(f"~~{title}~~ **(ukończone)**")
                else:
                    st.markdown(f"**{title}**")
                if description:
                    st.caption(description)
            with col2:
                if not completed:
                    if st.button("Oznacz jako ukończone", key=f"complete_{task_id}"):
                        complete_task(task_id)
                        st.rerun()
                if st.button("Usuń", key=f"delete_{task_id}"):
                    delete_task(task_id)
                    st.rerun()
            st.divider()
