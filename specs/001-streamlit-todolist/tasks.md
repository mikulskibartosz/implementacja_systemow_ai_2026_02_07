# Tasks: Todolist Application (Streamlit, SQLite3)

**Input**: Design documents from `/specs/001-streamlit-todolist/`  
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: Generowanie i uruchamianie testów są pomijane w tym planie zadań.

**Organization**: Zadania pogrupowane według user story (US1–US4); każda historia niezależnie testowalna.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Można wykonać równolegle (inne pliki, brak zależności)
- **[Story]**: Oznaczenie user story (US1, US2, US3, US4)
- W opisie podane ścieżki plików względem repozytorium (aplikacja w `12_speckit/`)

## Path Conventions

- Aplikacja w katalogu **`12_speckit/`**: `12_speckit/src/`, `12_speckit/tests/`
- Główny plik: `12_speckit/src/app.py` (konstytucja)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Inicjalizacja struktury projektu w `12_speckit`

- [x] T001 Create directory structure in 12_speckit: src/, tests/unit/ per plan.md
- [x] T002 [P] Create minimal 12_speckit/src/app.py stub (Streamlit app that runs and shows a title)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Warstwa bazy danych i walidacji; wymagana przed implementacją user stories.

**⚠️ CRITICAL**: Żadna user story nie może się rozpocząć przed zakończeniem tej fazy.

- [x] T003 Implement database initialization and connection in 12_speckit/src/db.py: init_db(), get_connection(), create table `tasks` (id, title, description, completed); missing file → create new DB; corrupted file → show message and run with empty list (FR-008)
- [x] T004 Implement add_task(title, description) with validation in 12_speckit/src/db.py: reject empty title (FR-006), title max 200 chars, description max 2000 chars (FR-007); return/raise clear error for UI message
- [x] T005 Implement get_tasks(filter), complete_task(id), delete_task(id) in 12_speckit/src/db.py per data-model.md (filter: all | active | completed)

**Checkpoint**: Warstwa db gotowa; można rozpoczynać user stories.

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Użytkownik dodaje zadanie (tytuł, opcjonalny opis); zadanie pojawia się na liście i jest zapisane w SQLite (persystencja po restarcie).

**Independent Test**: Uruchom aplikację, dodaj zadanie z tytułem (i opcjonalnie opisem), sprawdź że pojawia się na liście; zrestartuj aplikację i sprawdź że zadanie nadal jest widoczne.

### Implementation for User Story 1

- [x] T006 [US1] Add task form (title required, description optional) and submit handler in 12_speckit/src/app.py; show validation messages for empty title and length limits per contracts/ui-contract.md
- [x] T007 [US1] Display task list in 12_speckit/src/app.py: load tasks via get_tasks("all"), show title, description, status (active/completed)

**Checkpoint**: User Story 1 działa samodzielnie: dodawanie zadań i wyświetlanie listy z persystencją.

---

## Phase 4: User Story 2 - View and Filter Task List (Priority: P2)

**Goal**: Użytkownik widzi listę zadań i może filtrować: Wszystkie / Aktywne / Ukończone.

**Independent Test**: Dodaj mix zadań aktywnych i ukończonych; przełącz filtr i sprawdź że lista pokazuje tylko wybrany podzbiór.

### Implementation for User Story 2

- [x] T008 [US2] Add filter control (Wszystkie | Aktywne | Ukończone) in 12_speckit/src/app.py per contracts/ui-contract.md
- [x] T009 [US2] Wire filter to get_tasks(filter) and refresh list display in 12_speckit/src/app.py

**Checkpoint**: User Stories 1 i 2 działają: dodawanie, lista, filtrowanie.

---

## Phase 5: User Story 3 - Mark Tasks as Completed (Priority: P3)

**Goal**: Użytkownik może oznaczyć zadanie jako ukończone; ukończone są wizualnie odróżnialne i widoczne w filtrze „Ukończone”. Brak cofania do aktywnego (FR-004).

**Independent Test**: Dodaj zadanie, kliknij „Oznacz jako ukończone”; sprawdź że znika z „Aktywne” i pojawia się w „Ukończone”.

### Implementation for User Story 3

- [x] T010 [US3] Add "Oznacz jako ukończone" button for each active task in 12_speckit/src/app.py (identify task by id)
- [x] T011 [US3] Wire button to complete_task(id) and refresh list in 12_speckit/src/app.py; completed tasks visually distinct (e.g. strikethrough or label)

**Checkpoint**: User Stories 1–3 działają: dodawanie, filtrowanie, oznaczanie ukończonych.

---

## Phase 6: User Story 4 - Delete Tasks (Priority: P4)

**Goal**: Użytkownik może usunąć zadanie z listy; po usunięciu zadanie znika na stałe (również po restarcie).

**Independent Test**: Dodaj zadanie, usuń je; sprawdź że znika z listy i nie pojawia się po restarcie aplikacji.

### Implementation for User Story 4

- [x] T012 [US4] Add "Usuń" button for each task in 12_speckit/src/app.py (identify task by id)
- [x] T013 [US4] Wire delete button to delete_task(id) and refresh list in 12_speckit/src/app.py

**Checkpoint**: Wszystkie user stories (1–4) zaimplementowane.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Komunikaty pustej listy, uszkodzonej bazy oraz dokumentacja.

- [x] T014 [P] Show empty list message (e.g. "Brak zadań" or "Dodaj pierwsze zadanie") in 12_speckit/src/app.py when task list is empty for current filter (FR-009)
- [x] T015 Ensure corrupt DB message is shown on app startup when storage is corrupted in 12_speckit/src/app.py (FR-008; message from db layer or displayed in UI)
- [x] T016 [P] Add 12_speckit/README.md with short run instructions per specs/001-streamlit-todolist/quickstart.md (no venv creation, no pip install)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: Brak zależności — można zacząć od razu.
- **Phase 2 (Foundational)**: Zależy od Phase 1 — blokuje wszystkie user stories.
- **Phase 3–6 (User Stories)**: Zależą od Phase 2; kolejność P1 → P2 → P3 → P4 (US2–US4 rozszerzają ten sam app.py).
- **Phase 7 (Polish)**: Zależy od zakończenia Phase 6.

### User Story Dependencies

- **US1 (P1)**: Po Phase 2; brak zależności od innych stories.
- **US2 (P2)**: Po US1 (lista musi być wyświetlana).
- **US3 (P3)**: Po US2 (lista z filtrem; przycisk „Oznacz jako ukończone” na elemencie listy).
- **US4 (P4)**: Po US3 (przycisk „Usuń” obok „Oznacz jako ukończone”).

### Within Each Phase

- Phase 2: T003 → T004 → T005 (db.py).
- Phase 3: T006 (formularz) → T007 (lista).
- Phase 4–6: po jednym–dwa zadania na story, sekwencyjnie w app.py.

### Parallel Opportunities

- Phase 1: T002 [P] równolegle z T001.
- Phase 7: T014 [P], T016 [P] można wykonać równolegle.

---

## Implementation Strategy

### MVP First (User Story 1)

1. Phase 1: Setup (T001–T002).
2. Phase 2: Foundational (T003–T005).
3. Phase 3: User Story 1 (T006–T007).
4. **STOP i WALIDACJA**: Uruchom aplikację, dodaj zadanie, zrestartuj — lista się zachowuje (MVP).

### Incremental Delivery

1. Setup + Foundational → gotowa warstwa db.
2. US1 → dodawanie i lista → demo MVP.
3. US2 → filtrowanie → demo.
4. US3 → ukończ zadanie → demo.
5. US4 → usuń zadanie → demo.
6. Phase 7 → pusta lista, uszkodzona baza, README.

### Suggested MVP Scope

- **MVP**: Phase 1 + Phase 2 + Phase 3 (T001–T007).  
- Niezależny test: dodaj zadanie → zobacz na liście → zrestartuj aplikację → zadanie nadal na liście.

---

## Notes

- Ścieżki względem root repozytorium; aplikacja w `12_speckit/`.
- Komentarze i dokumentacja po polsku, nazwy w kodzie po angielsku (konstytucja).
- Po każdym checkpoint można zatrzymać się i przetestować daną user story.
- Generowanie i uruchamianie testów są pomijane w tym planie.
