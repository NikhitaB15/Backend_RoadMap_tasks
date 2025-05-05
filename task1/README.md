# Task Tracker CLI

Task Tracker CLI is a simple command-line interface (CLI) application to help you track and manage your tasks. You can add, update, delete, and list tasks, as well as mark them as "in-progress" or "done". Tasks are stored in a JSON file for persistence.

---

## Features

- Add a new task with a description.
- Update an existing task's description.
- Delete a task by its ID.
- Mark a task as "in-progress" or "done".
- List all tasks or filter tasks by their status (`todo`, `in-progress`, `done`).

---

## Task Properties

Each task has the following properties:

- **id**: A unique identifier for the task.
- **description**: A short description of the task.
- **status**: The status of the task (`todo`, `in-progress`, `done`).
- **createdAt**: The date and time when the task was created.
- **updatedAt**: The date and time when the task was last updated.

---

## Usage

### Add a Task
```bash
python [task_cli.py](http://_vscodecontentref_/1) add "Task description"