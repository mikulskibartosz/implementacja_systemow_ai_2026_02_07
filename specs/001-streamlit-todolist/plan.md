# Implementation Plan: Todolist Application (Streamlit, SQLite3)

**Branch**: `001-streamlit-todolist` | **Date**: 2026-02-22 | **Spec**: [spec.md](./spec.md)  
**Input**: Feature specification from `/specs/001-streamlit-todolist/spec.md`

## Summary

Aplikacja Todolist z interfejsem Streamlit i persystencją w SQLite3. Użytkownik dodaje zadania (tytuł, opcjonalny opis), oznacza je jako ukończone, usuwa; lista jest filtrowana (wszystkie / aktywne / ukończone). Dane w pliku lokalnym `tasks.db`; aplikacja jednoużytkownikowa w katalogu `12_speckit`.

## Technical Context

**Language/Version**: Python 3.11+  
**Primary Dependencies**: Streamlit  
**Storage**: SQLite3 (stdlib), plik `tasks.db` w katalogu aplikacji  
**Testing**: pytest  
**Target Platform**: Lokalne (desktop), uruchomienie przez `streamlit run`  
**Project Type**: web-app (single-user, local UI)  
**Performance Goals**: Odpowiedź UI na akcje użytkownika bez zauważalnego opóźnienia; brak wymagań na konkretne metryki.  
**Constraints**: Jedna baza w pliku, brak zewnętrznych serwerów; zgodność z konstytucją (język PL w dokumentacji, EN w kodzie; src/app.py, src/, tests/).  
**Scale/Scope**: Jedna aplikacja, jedna baza plikowa, jeden użytkownik.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Zasada | Status | Uwagi |
|--------|--------|--------|
| I. Język i nazewnictwo (PL w komentarzach/docs, EN w kodzie) | ✅ PASS | Plan i spec po polsku/EN; kod w 12_speckit z nazwami EN. |
| II. Struktura: src/, tests/, główny plik src/app.py | ✅ PASS | Struktura w 12_speckit: src/, tests/, src/app.py. |
| III. Python 3.11+, Streamlit, SQLite3 (tasks.db), brak zewn. DB | ✅ PASS | Stack zgodny z konstytucją. |
| IV. pytest, test jednostkowy dla logiki biznesowej | ⏭️ Pomijane | W tym planie zadań nie generujemy ani nie uruchamiamy testów. |
| V. Środowisko wirtualne, nie dodawać zależności bez uzgodnienia | ✅ PASS | Nie tworzyć requirements.txt w 12_speckit; nie zmieniać istniejącego. Venv istnieje (np. .venv). |

Brak naruszeń. Complexity Tracking: nie dotyczy.

## Project Structure

### Documentation (this feature)

```text
specs/001-streamlit-todolist/
├── plan.md              # Ten plik
├── research.md          # Phase 0
├── data-model.md        # Phase 1
├── quickstart.md        # Phase 1
├── contracts/           # Phase 1 (kontrakt UI)
└── tasks.md             # Phase 2 (/speckit.tasks – nie tworzony przez /speckit.plan)
```

### Source Code (application in 12_speckit)

Aplikacja powstaje w katalogu **`12_speckit`** (względem root repozytorium).

```text
12_speckit/
├── src/
│   ├── app.py           # Główny plik aplikacji Streamlit (konstytucja)
│   ├── db.py            # Inicjalizacja bazy, CRUD, obsługa brak/uszkodzenie pliku
│   └── (opcjonalnie: constants.py dla limitów 200/2000)
├── tests/
│   └── unit/            # Katalog na testy (generowanie i uruchamianie testów pomijane w tym planie)
├── tasks.db             # Plik SQLite (tworzony przy pierwszym uruchomieniu)
└── README.md            # Krótka instrukcja (opcjonalnie; quickstart w specs/)
```

**Uwaga**: Nie tworzymy ani nie modyfikujemy pliku `requirements.txt`; istniejące venv i zależności pozostają bez zmian.

**Structure Decision**: Pojedynczy projekt w `12_speckit` z warstwą UI (Streamlit) i warstwą dostępu do danych (SQLite3). Główny punkt wejścia `src/app.py` zgodnie z konstytucją.

## Complexity Tracking

Nie dotyczy — brak uzasadnionych naruszeń konstytucji.
