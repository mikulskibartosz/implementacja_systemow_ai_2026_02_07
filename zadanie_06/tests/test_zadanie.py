from enum import Enum

class TaskStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "status": TaskStatus.PENDING})

    def remove_task(self, task):
        self.tasks = [item for item in self.tasks if item.get("task") != task]

    def mark_task_as_completed(self, task):
        self.tasks = [{"task": item.get("task"), "status": TaskStatus.COMPLETED} if item.get("task") == task else item for item in self.tasks]

    def get_pending_tasks(self):
        return [item.get("task") for item in self.tasks if item.get("status") == TaskStatus.PENDING]

    def get_all_tasks(self):
        return [(item.get("task"), item.get("status")) for item in self.tasks]


class TodoListAssert:
    def __init__(self, todo_list):
        self.todo_list = todo_list

    def has_task_count(self, expected_count):
        assert len(self.todo_list.tasks) == expected_count
        return self

    def includes_task(self, task):
        assert any(item.get("task") == task for item in self.todo_list.tasks)
        return self

    def does_not_include_task(self, task):
        assert not any(item.get("task") == task for item in self.todo_list.tasks)
        return self

    def has_task_with_status(self, task, status):
        assert any(item.get("task") == task and item.get("status") == status for item in self.todo_list.tasks)
        return self

def test_add_task():
    # Given
    todo_list = TodoList()

    # When
    todo_list.add_task("Buy groceries")

    # Then
    TodoListAssert(todo_list) \
        .has_task_count(1) \
        .includes_task("Buy groceries") \
        .has_task_with_status("Buy groceries", TaskStatus.PENDING)


def test_remove_task():
    # Given
    todo_list = TodoList()
    todo_list.add_task("Buy groceries")

    # When
    todo_list.remove_task("Buy groceries")

    # Then
    TodoListAssert(todo_list) \
        .has_task_count(0) \
        .does_not_include_task("Buy groceries")


def test_mark_task_as_completed():
    # Given
    todo_list = TodoList()
    todo_list.add_task("Buy groceries")

    # When
    todo_list.mark_task_as_completed("Buy groceries")

    # Then
    TodoListAssert(todo_list) \
        .has_task_with_status("Buy groceries", TaskStatus.COMPLETED)


def test_get_pending_tasks():
    # Given
    todo_list = TodoList()
    todo_list.add_task("Buy groceries")
    todo_list.add_task("Buy fruits")
    todo_list.mark_task_as_completed("Buy groceries")

    # When
    pending_tasks = todo_list.get_pending_tasks()

    # Then
    assert pending_tasks == ["Buy fruits"]


def test_get_all_tasks():
    # Given
    todo_list = TodoList()
    todo_list.add_task("Buy groceries")
    todo_list.add_task("Buy fruits")
    todo_list.mark_task_as_completed("Buy groceries")

    # When
    all_tasks = todo_list.get_all_tasks()

    # Then
    assert all_tasks == [("Buy groceries", TaskStatus.COMPLETED), ("Buy fruits", TaskStatus.PENDING)]