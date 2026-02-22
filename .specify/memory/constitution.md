<!--
Sync Impact Report
==================
Version change: N/A → 1.0.0
Modified principles: (none – initial adoption)
Added sections: Core Principles (5), Wymagania techniczne, Środowisko deweloperskie, Governance
Removed sections: (none)
Templates:
  .specify/templates/plan-template.md – ✅ Constitution Check refers to constitution file (generic)
  .specify/templates/spec-template.md – ✅ no mandatory sections changed
  .specify/templates/tasks-template.md – ✅ paths src/, tests/ align with Principle 2
Follow-up TODOs: (none)
-->

# Konstytucja projektu: Aplikacja Todolist

## Zasady podstawowe

### I. Język i nazewnictwo

- Komentarze, dokumentacja i opisy w projekcie MUSZĄ być w języku polskim.
- Nazwy zmiennych, funkcji i klas w kodzie źródłowym MUSZĄ być w języku angielskim.

**Uzasadnienie**: Spójność z zespołem i odbiorcami dokumentacji przy zachowaniu
konwencji branżowej w kodzie (czytelność dla narzędzi i współpracowników).

### II. Struktura projektu

- Struktura katalogów MUSI być prosta: `src/` dla kodu źródłowego, `tests/` dla testów.
- Główny plik aplikacji MUSI znajdować się w `src/app.py`.

**Uzasadnienie**: Łatwa nawigacja, jasny podział odpowiedzialności i spójność
z typowymi projektami Python.

### III. Stack technologiczny

- Python w wersji 3.11 lub nowszej.
- Streamlit do budowy interfejsu użytkownika.
- SQLite3 (biblioteka standardowa) do przechowywania danych; baza w pliku
  lokalnym `tasks.db`. Nie stosować zewnętrznych baz danych.

**Uzasadnienie**: Minimalna zależność zewnętrzna, prostota wdrożenia i brak
wymagań infrastrukturalnych poza Pythonem i Streamlit.

### IV. Testy jednostkowe

- Testy MUSZĄ być realizowane z użyciem pytest.
- Każda funkcja logiki biznesowej MUSI mieć odpowiadający jej test jednostkowy.

**Uzasadnienie**: Pewność regresji i możliwość refaktoryzacji przy zachowaniu
zgodności z wymaganiami.

### V. Środowisko wirtualne i zależności

- Należy korzystać ze środowiska wirtualnego w katalogu głównym projektu.
- Nie dodawać żadnych zależności do pliku `requirements.txt`.

**Uzasadnienie**: Izolacja projektu i stabilna, zdefiniowana lista zależności
bez rozrostu bez uzasadnienia.

## Wymagania techniczne

- Baza danych: wyłącznie plik SQLite `tasks.db` (biblioteka standardowa).
- Brak zewnętrznych serwerów baz danych. Wszystkie dane w pliku lokalnym.

## Środowisko deweloperskie

- Uruchamianie aplikacji i testów w ramach venv w katalogu głównym projektu.
- Lista zależności zamrożona w `requirements.txt` – zmiany tylko po uzgodnieniu
  i aktualizacji konstytucji lub dokumentacji projektu.

## Governance

- Konstytucja ma pierwszeństwo przed innymi praktykami projektowymi.
- Zmiany wymagają aktualizacji tego dokumentu, wpisu w Sync Impact Report
  oraz (w razie potrzeby) migracji lub aktualizacji planu/specyfikacji.
- Wersjonowanie: semver (MAJOR.MINOR.PATCH) w polu Version poniżej.
- Przy przeglądach i planach (np. Constitution Check w planie) należy
  weryfikować zgodność z niniejszymi zasadami.

**Wersja**: 1.0.0 | **Ratifikacja**: 2026-02-22 | **Ostatnia zmiana**: 2026-02-22
