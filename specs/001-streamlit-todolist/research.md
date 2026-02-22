# Research: Todolist (Streamlit, SQLite3)

**Feature**: 001-streamlit-todolist  
**Date**: 2026-02-22

Wszystkie wybory techniczne i zachowania wynikają ze specyfikacji oraz konstytucji projektu; brak otwartych NEEDS CLARIFICATION. Poniżej utrwalone decyzje.

---

## Stack i lokalizacja

- **Decision**: Python 3.11+, Streamlit, SQLite3 (stdlib), aplikacja w katalogu `12_speckit`.
- **Rationale**: Konstytucja projektu (III: Streamlit, SQLite3, plik `tasks.db`); spec: aplikacja w `12_speckit`.
- **Alternatives considered**: Inne UI (Flask, FastAPI) lub bazy — odrzucone przez konstytucję.

---

## Persystencja i obsługa błędów storage

- **Decision**: Brak pliku → tworzenie nowej pustej bazy; uszkodzony plik → komunikat dla użytkownika, start z pustą listą (bez odzyskiwania danych).
- **Rationale**: Clarification Q3 w spec; minimalna złożoność i przewidywalne zachowanie.
- **Alternatives considered**: Blokowanie startu przy uszkodzeniu — gorsze UX; próba naprawy DB — poza zakresem.

---

## Limity i walidacja

- **Decision**: Tytuł max 200 znaków, opis max 2000; puste tytuły odrzucane; duplikaty tytułów dozwolone; każde zadanie ma unikalne ID.
- **Rationale**: Clarifications (limity, duplikaty); Key Entities (unikalna tożsamość zadania).
- **Alternatives considered**: Unikalność tytułu — odrzucona (clarification: duplikaty dozwolone).

---

## Testy i struktura kodu

- **Decision**: pytest w `tests/`; logika dostępu do bazy i walidacja w module (np. `db.py`) z testami jednostkowymi; główny plik `src/app.py`.
- **Rationale**: Konstytucja (IV: pytest, test na logikę biznesową; II: src/app.py, src/, tests/).
- **Alternatives considered**: Testy tylko E2E — niewystarczające dla regresji logiki (const. IV).

---

## Kontrakt użytkownika (UI)

- **Decision**: Interfejs opisany w contracts/ jako ekrany i akcje (formularz dodawania, lista z filtrem, przyciski ukończ/usuń, komunikat przy pustej liście).
- **Rationale**: Umożliwia spójną implementację i testy akceptacyjne bez przywiązania do konkretnych widgetów.
- **Alternatives considered**: Brak kontraktu — ryzyko rozjazdu między spec a implementacją.
