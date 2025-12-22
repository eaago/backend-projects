# Task Tracker CLI

A simple, terminal-based task tracker written in Python. Manage tasks with statuses (`todo`, `in-progress`, `done`), store them to a JSON file, and interact through a command-line interface.

---

## Features

* Add, update, delete tasks
* Mark tasks as **todo**, **in-progress**, or **done**
* List tasks by status or view all
* Storage of tasks using `task_list.json`
* Terminal screen clearing per input for cleaner outputs

---

## Requirements

* Python **3.8+**
* Standard library only (no external dependencies)

---

## Installation

1. Clone or download this repository
2. Ensure Python is installed:

```bash
python --version
```

3. Navigate to the project directory

---

## Usage

Run the application:

```bash
python task_tracker_cli.py
```

---

## Commands

### `help`

Display the list of available commands.

```text
help
```

---

### `add`

Add a new task.

```text
add <task_description>
```

Example:

```text
add Take the cats to the catio
```

---

### `update`

Update the description of an existing task.

```text
update <task_id> <new_description>
```

Example:

```text
update 2 Brush the cats
```

---

### `delete`

Delete a task by its ID.

```text
delete <task_id>
```

Example:

```text
delete 3
```

---

### `list`

List tasks. Optionally filter by status.

```text
list
list todo
list in-progress
list done
```

---

### `mark-in-progress`

Mark a task as in progress.

```text
mark-in-progress <task_id>
```

---

### `mark-done`

Mark a task as completed.

```text
mark-done <task_id>
```

---

### `close`

Save tasks to disk and exit the application.

```text
close
```

---

## Data Storage

Tasks are stored in a file named:

```text
task_list.json
```

Each task follows this structure:

```json
  {
    "id": 1,
    "description": "Feed the cats",
    "status": "todo",
    "createdAt": "2025-12-21 23:50:50",
    "updatedAt": "2025-12-21 23:50:50"
  }
```

---

## Notes & Limitations

* Task IDs are automatically reassigned after deletions
* Descriptions are parsed from space-separated input (quotes are not required)
* Input is case-sensitive


---

## License

This project is for learning and personal use. Feel free to modify and expand it.


