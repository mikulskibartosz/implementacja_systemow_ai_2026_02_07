# Kontrakt UI: Aplikacja Todolist (Streamlit)

**Feature**: 001-streamlit-todolist  
**Date**: 2026-02-22

Opis interfejsu użytkownika na poziomie ekranów i akcji (niezależny od konkretnych widgetów Streamlit).

---

## Sekcje / Ekran

1. **Formularz dodawania zadania**
   - Wejście: tytuł (obowiązkowy), opis (opcjonalny).
   - Akcja: „Dodaj” / submit.
   - Walidacja: tytuł niepusty, tytuł ≤ 200 znaków, opis ≤ 2000 znaków; przy błędzie — czytelny komunikat (FR-006, FR-007).

2. **Filtr listy**
   - Wybór jednej z wartości: **Wszystkie** | **Aktywne** | **Ukończone** (FR-003).
   - Po zmianie filtra lista odświeża się (te same dane, inny podzbiór).

3. **Lista zadań**
   - Dla każdego zadania: tytuł, opcjonalnie opis, status (aktywne/ukończone), akcje: **Oznacz jako ukończone** (tylko dla aktywnych), **Usuń** (FR-004, FR-005).
   - Identyfikacja zadania do akcji: po wewnętrznym id (nie po tytule).
   - Gdy lista pusta (dla wybranego filtra): wyświetlony komunikat np. „Brak zadań” / „Dodaj pierwsze zadanie” (FR-009).

4. **Komunikat przy uszkodzonej bazie**
   - Gdy przy starcie wykryto uszkodzenie pliku bazy: jeden czytelny komunikat dla użytkownika; aplikacja działa z pustą listą (FR-008).

---

## Komunikaty (minimalny zestaw)

| Sytuacja | Oczekiwany przekaz (po polsku) |
|----------|---------------------------------|
| Pusta lista | Np. „Brak zadań” lub „Dodaj pierwsze zadanie”. |
| Pusty tytuł | Np. „Tytuł nie może być pusty.” |
| Tytuł za długi | Np. „Tytuł może mieć co najwyżej 200 znaków.” |
| Opis za długi | Np. „Opis może mieć co najwyżej 2000 znaków.” |
| Uszkodzona baza | Np. „Nie udało się wczytać danych. Lista jest pusta.” (bez blokowania dalszego działania). |

---

## Zachowanie

- Oznaczenie jako ukończone: tylko dla zadań w stanie „aktywne”; po akcji zadanie przechodzi do „ukończone” i nie można tego cofnąć (FR-004).
- Usuwanie: trwałe usunięcie z bazy; po odświeżeniu/restarcie zadanie nie wraca (FR-005).
- Wszystkie zmiany zapisywane od razu w SQLite (brak trybu „niezapisane zmiany”).
