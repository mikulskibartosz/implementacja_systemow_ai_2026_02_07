# Data Model: Todolist

**Feature**: 001-streamlit-todolist  
**Date**: 2026-02-22

## Encje

### Task

Pojedyncze zadanie na liście. Identyfikowane wewnętrznie przez **id** (unikalne); tytuł nie musi być unikalny.

| Pole | Typ (logiczny) | Obowiązkowe | Walidacja | Uwagi |
|------|----------------|-------------|-----------|--------|
| id | integer / auto | tak | unikalne, niezmienne | Klucz główny; używane przy complete/delete. |
| title | string | tak | 1–200 znaków, niepusty po trim | FR-006, FR-007. |
| description | string | nie | 0–2000 znaków | FR-007; pusty string lub NULL = brak opisu. |
| completed | boolean | tak | — | false = active, true = completed. Domyślnie false. |

**Reguły**:
- Tytuł po obcięciu białych znaków nie może być pusty (FR-006).
- Długość: title ≤ 200 znaków, description ≤ 2000 znaków (FR-007).
- Przejście stanu: tylko **active → completed**; brak cofania do active (FR-004, clarifications).

### Task list (widok)

Widok listy zadań z filtrem:
- **all** — wszystkie zadania
- **active** — `completed = false`
- **completed** — `completed = true`

Nie jest osobną encją w storage; to wynik zapytania z jednej tabeli `tasks`.

## Persystencja (SQLite3)

- **Plik**: `tasks.db` w katalogu aplikacji (np. `12_speckit/`).
- **Tabela**: jedna tabela `tasks` z kolumnami odpowiadającymi polom Task (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, description TEXT, completed INTEGER NOT NULL DEFAULT 0).
- **Brak pliku**: przy starcie tworzyć nową bazę i tabelę (FR-008).
- **Uszkodzony plik**: wyświetlić komunikat, użyć pustej listy w pamięci (lub tymczasowej bazy) bez odzyskiwania danych (FR-008).

## Stany i przejścia

- **active** (completed = false) → użytkownik może: oznaczyć jako ukończone, usunąć.
- **completed** (completed = true) → użytkownik może tylko usunąć; nie ma przejścia z powrotem na active.

## Zależności do wymagań

| Wymaganie | Odpowiedź w modelu |
|-----------|---------------------|
| FR-001, FR-002 | Task z title, description; zapis w SQLite. |
| FR-003 | Widok z filtrem all/active/completed. |
| FR-004 | Pole completed; brak przejścia completed → active. |
| FR-005 | Usuwanie po id. |
| FR-006, FR-007 | Walidacja title (niepusty, ≤200), description (≤2000). |
| FR-008 | Inicjalizacja bazy: brak pliku → utwórz; uszkodzenie → komunikat + pusta lista. |
