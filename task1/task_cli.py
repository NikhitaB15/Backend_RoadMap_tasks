import sys
import json
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task["status"] == status]
    for task in tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']}")

def delete_tasks(x):
    tasks = load_tasks()
    for i in range(len(tasks)):
        if tasks[i]["id"] == x:
            tasks=tasks[:i]+tasks[i+1:]
        else:
            print(f"Task {x} not found")
            break
        save_tasks(tasks)        
        print(f"Task {x} deleted successfully")
def update_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == int(task_id):
            task["description"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated to {status}")
            return
    else:
        print(f"Task {task_id} not found")
    
# Main CLI logic
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: task-cli add <description>")
        else:
            add_task(sys.argv[2])
    elif command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status)
    elif command == "update":
        status = sys.argv[3]
        update = update_task(sys.argv[2], status)
    elif command == "delete":
        position = sys.argv[2] if len(sys.argv) > 2 else None
        delete_tasks(int(position))        
    else:
        print(f"Unknown command: {command}")