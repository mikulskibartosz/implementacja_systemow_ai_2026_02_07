# Feature Specification: Todolist Application (Streamlit, SQLite3)

**Feature Branch**: `001-streamlit-todolist`  
**Created**: 2026-02-22  
**Status**: Draft  
**Input**: User description: "Aplikacja Todolist w Streamlit z baza SQLite3. Uzytkownik moze dodawac nowe zadania (tytul oraz opcjonalny opis), oznaczac zadania jako ukonczone, usuwac zadania z listy. Wszystkie zadania sa przechowywane w lokalnym pliku SQLite3, dzieki czemu dane nie znikaja po ponownym uruchomieniu aplikacji. Interfejs Streamlit wyswietla liste zadan z mozliwoscia filtrowania (wszystkie, aktywne, ukonczone) oraz formularz do dodawania nowych zadan. Aplikacja jest jednouzytkownikowa i dziala lokalnie."

## Clarifications

### Session 2026-02-22

- Q: Czy użytkownik może ponownie oznaczyć ukończone zadanie jako aktywne (uncomplete)? → A: Nie — po oznaczeniu jako ukończone zadanie pozostaje ukończone; ewentualna korekta tylko przez usunięcie i dodanie od nowa.
- Q: Jakie limity znaków przyjąć dla tytułu i opisu zadania? → A: 200 znaków tytuł, 2000 znaków opis.
- Q: Co ma robić aplikacja przy braku pliku bazy lub jej uszkodzeniu? → A: Brak pliku: tworzyć nową, pustą bazę. Uszkodzenie: komunikat dla użytkownika, aplikacja działa z pustą listą (bez odzyskiwania danych).
- Q: Czy system ma zezwalać na wiele zadań z tym samym tytułem? → A: Tak — dozwolone; każde zadanie ma wewnętrzną tożsamość (np. ID).
- Q: Czy przy pustej liście pokazywać wyraźny komunikat dla użytkownika? → A: Tak — przy pustej liście pokazać krótki komunikat (np. "Brak zadań" / "Dodaj pierwsze zadanie").

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add New Tasks (Priority: P1)

The user can add a new task by providing a title (required) and optionally a description. The task appears in the task list and is stored so it remains after the application is restarted.

**Why this priority**: Adding tasks is the core value of a todolist; without it there is no product.

**Independent Test**: Can be fully tested by opening the app, submitting a new task with title (and optionally description), and verifying the task appears in the list and persists after restart.

**Acceptance Scenarios**:

1. **Given** the app is open, **When** the user enters a title and submits the form, **Then** a new task appears in the list with that title and status "active".
2. **Given** the app is open, **When** the user enters a title and an optional description and submits, **Then** a new task appears with both title and description.
3. **Given** the user has added at least one task, **When** the user restarts the application, **Then** previously added tasks are still visible.

---

### User Story 2 - View and Filter Task List (Priority: P2)

The user sees a list of all tasks and can filter the view to show all tasks, only active (incomplete) tasks, or only completed tasks.

**Why this priority**: Viewing and filtering is essential to manage many tasks; it follows the ability to add tasks.

**Independent Test**: Can be tested by adding a mix of active and completed tasks, then switching filters and verifying the displayed list matches the selected filter.

**Acceptance Scenarios**:

1. **Given** there are tasks (some active, some completed), **When** the user selects "all", **Then** every task is shown.
2. **Given** there are tasks (some active, some completed), **When** the user selects "active", **Then** only tasks not marked completed are shown.
3. **Given** there are tasks (some active, some completed), **When** the user selects "completed", **Then** only tasks marked as completed are shown.

---

### User Story 3 - Mark Tasks as Completed (Priority: P3)

The user can mark a task as completed. Completed tasks are visually distinguishable and can be filtered (see User Story 2).

**Why this priority**: Completing tasks is the main way to track progress; it depends on having tasks to complete.

**Independent Test**: Can be tested by adding a task, marking it completed, and verifying it appears under "completed" filter and is visually distinct.

**Acceptance Scenarios**:

1. **Given** an active task is visible, **When** the user marks it as completed, **Then** the task is shown as completed and appears when filtering by "completed". The user cannot revert a completed task to active; correction is only by deleting and re-adding the task.

---

### User Story 4 - Delete Tasks (Priority: P4)

The user can remove a task from the list. Once deleted, the task is no longer stored or displayed.

**Why this priority**: Deletion supports list hygiene and correction of mistakes; it is secondary to add/complete/view.

**Independent Test**: Can be tested by adding a task, deleting it, and verifying it no longer appears and does not reappear after restart.

**Acceptance Scenarios**:

1. **Given** a task exists in the list, **When** the user deletes that task, **Then** the task is removed from the list.
2. **Given** the user has deleted a task, **When** the application is restarted, **Then** the deleted task does not reappear.

---

### Edge Cases

- What happens when the user submits a new task with an empty title? The system should reject or prevent submission (e.g. require non-empty title) and show a clear message.
- When the storage file is missing: the application creates a new empty database and runs with an empty task list. When the storage file is corrupted: the application shows a clear, user-friendly message (e.g. that data could not be loaded), starts with an empty list, and does not attempt to recover previous data.
- When title exceeds 200 characters or description exceeds 2000 characters, the system rejects input and shows a clear message (e.g. "Title max 200 characters").

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow the user to add a new task with a required title and an optional description.
- **FR-002**: System MUST persist all tasks in local storage so that data survives application restart.
- **FR-003**: System MUST display the list of tasks and support filtering by: all, active (incomplete), completed.
- **FR-004**: System MUST allow the user to mark a task as completed. Once completed, a task cannot be reverted to active; the user may delete and re-add it if needed.
- **FR-005**: System MUST allow the user to delete a task; once deleted, the task is permanently removed from storage.
- **FR-006**: System MUST prevent adding a task with an empty title (validation or clear feedback).
- **FR-007**: System MUST enforce maximum length: title 200 characters, description 2000 characters; reject overlong input with a clear message.
- **FR-008**: System MUST handle missing storage file by creating a new empty store and running with an empty list; and handle corrupted storage by showing a user-friendly message and running with an empty list (no data recovery).
- **FR-009**: System MUST display a clear message when the task list is empty (e.g. "Brak zadań" or "Dodaj pierwsze zadanie").
- **FR-010**: System MUST run as a single-user, local application (no multi-user or remote access requirement).

### Key Entities

- **Task**: A single todo item with a unique identity (e.g. internal ID) used for actions like complete/delete. Attributes: title (required, max 200 characters; need not be unique), optional description (max 2000 characters), completion status (active/completed). Stored in local persistence.
- **Task list (view)**: The current set of tasks displayed to the user, possibly filtered by status (all / active / completed).

## Assumptions

- The application is built in the repository directory **`12_speckit`** (at repo root); all application code and assets live there.
- Application is single-user and runs locally; no authentication or authorization is required.
- Persistence is implemented with a local file (e.g. SQLite3) as indicated by the user; exact technology is an implementation choice.
- UI is web-based (e.g. Streamlit) as indicated by the user; no specific framework is mandated in success criteria.
- Title is limited to 200 characters and description to 2000 characters (enforced by FR-007).
- "Active" means not completed; "completed" means the user has marked the task as done. No automatic completion (e.g. by date) is required unless specified later.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: User can add a new task (with title and optional description) and see it in the list in a single interaction (e.g. one form submit).
- **SC-002**: User can complete the primary flow (add task → mark completed → see it under "completed" filter) in under one minute.
- **SC-003**: All tasks added in a session remain available after the application is closed and reopened (persistence).
- **SC-004**: User can filter the list to only active or only completed tasks and see the list update immediately.
- **SC-005**: User can delete a task and confirm it is gone from the list and does not reappear after restart.
