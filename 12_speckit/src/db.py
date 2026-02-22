"""
Warstwa dostępu do bazy SQLite3 dla Todolist.
Inicjalizacja bazy, CRUD, obsługa brakującego/uszkodzonego pliku (FR-008).
Komentarze po polsku, nazwy w kodzie po angielsku (konstytucja).
"""
import os
import sqlite3
from typing import Literal

# Limity z specyfikacji (FR-007)
TITLE_MAX_LEN = 200
DESCRIPTION_MAX_LEN = 2000

# Ścieżka do pliku bazy: katalog roboczy (12_speckit przy uruchomieniu streamlit run src/app.py)
def _db_path() -> str:
    return os.path.join(os.getcwd(), "tasks.db")

# Flaga ustawiana przy wykryciu uszkodzonej bazy (komunikat w UI)
_corrupt_message: str | None = None

def get_corrupt_message() -> str | None:
    """Zwraca komunikat o uszkodzonej bazie, jeśli wystąpił przy starcie; inaczej None."""
    return _corrupt_message

def init_db() -> None:
    """
    Inicjalizuje połączenie i tabelę tasks.
    Brak pliku → tworzy nową bazę (FR-008).
    Uszkodzony plik → ustawia komunikat, aplikacja działa z pustą listą (bez odzyskiwania).
    """
    global _corrupt_message
    _corrupt_message = None
    path = _db_path()
    if os.path.exists(path):
        try:
            conn = sqlite3.connect(path)
            if conn.execute(
                "SELECT 1 FROM sqlite_master WHERE type='table' AND name='tasks'"
            ).fetchone() is None:
                _create_table(conn)
            conn.close()
            return
        except (sqlite3.Error, OSError):
            _corrupt_message = "Nie udało się wczytać danych. Lista jest pusta."
            try:
                os.remove(path)
            except OSError:
                pass
    conn = sqlite3.connect(path)
    _create_table(conn)
    conn.close()

def _create_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed INTEGER NOT NULL DEFAULT 0
        )
        """
    )
    conn.commit()

def get_connection() -> sqlite3.Connection:
    """Zwraca połączenie do bazy. Przed pierwszym użyciem należy wywołać init_db()."""
    return sqlite3.connect(_db_path())

class ValidationError(Exception):
    """Błąd walidacji (pusty tytuł lub przekroczone limity)."""
    pass

def add_task(title: str, description: str = "") -> int:
    """
    Dodaje zadanie. Zwraca id.
    FR-006: odrzuca pusty tytuł (po strip).
    FR-007: tytuł max 200 znaków, opis max 2000; przy błędzie ValidationError z czytelnym komunikatem.
    """
    t = (title or "").strip()
    if not t:
        raise ValidationError("Tytuł nie może być pusty.")
    if len(t) > TITLE_MAX_LEN:
        raise ValidationError("Tytuł może mieć co najwyżej 200 znaków.")
    if len(description or "") > DESCRIPTION_MAX_LEN:
        raise ValidationError("Opis może mieć co najwyżej 2000 znaków.")
    conn = get_connection()
    try:
        cur = conn.execute(
            "INSERT INTO tasks (title, description, completed) VALUES (?, ?, 0)",
            (t, (description or "").strip() or None),
        )
        conn.commit()
        return cur.lastrowid
    finally:
        conn.close()

FilterKind = Literal["all", "active", "completed"]

def get_tasks(filter_kind: FilterKind = "all") -> list[tuple[int, str, str | None, bool]]:
    """
    Zwraca listę zadań: (id, title, description, completed).
    filter_kind: all | active | completed (FR-003).
    """
    conn = get_connection()
    try:
        if filter_kind == "active":
            cur = conn.execute(
                "SELECT id, title, description, completed FROM tasks WHERE completed = 0 ORDER BY id"
            )
        elif filter_kind == "completed":
            cur = conn.execute(
                "SELECT id, title, description, completed FROM tasks WHERE completed = 1 ORDER BY id"
            )
        else:
            cur = conn.execute(
                "SELECT id, title, description, completed FROM tasks ORDER BY id"
            )
        return [(row[0], row[1], row[2], bool(row[3])) for row in cur.fetchall()]
    finally:
        conn.close()

def complete_task(task_id: int) -> None:
    """Oznacza zadanie jako ukończone (FR-004). Nie cofa completed → active."""
    conn = get_connection()
    try:
        conn.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        conn.commit()
    finally:
        conn.close()

def delete_task(task_id: int) -> None:
    """Usuwa zadanie na stałe (FR-005)."""
    conn = get_connection()
    try:
        conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
    finally:
        conn.close()
