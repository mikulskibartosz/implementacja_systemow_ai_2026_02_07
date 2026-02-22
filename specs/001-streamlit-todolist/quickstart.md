# Quickstart: Todolist (12_speckit)

**Feature**: 001-streamlit-todolist  
**Date**: 2026-02-22

## Wymagania

- Python 3.11+
- Środowisko wirtualne w `.venv` (używane bez tworzenia i bez instalacji zależności)

## Uruchomienie

1. Przejdź do katalogu aplikacji:
   ```bash
   cd 12_speckit
   ```

2. Aktywuj istniejące venv (`.venv/bin`):
   ```bash
   source .venv/bin/activate   # Linux/macOS
   # .venv\Scripts\activate    # Windows
   ```

3. Uruchom aplikację:
   ```bash
   streamlit run src/app.py
   ```

4. Otwórz w przeglądarce adres podany w terminalu (zazwyczaj http://localhost:8501).

## Testy

Z katalogu `12_speckit`:

```bash
pytest tests/ -v
```

(Zgodnie z konstytucją: pytest, testy w `tests/`.)

## Plik bazy

- Przy pierwszym uruchomieniu w `12_speckit` powstaje plik `tasks.db` (jeśli brak pliku — FR-008).
- Baza znajduje się w katalogu roboczym z którego uruchomiono `streamlit run` (np. `12_speckit/tasks.db`).
