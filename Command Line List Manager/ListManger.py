import os
import sys

LIST_FILE = "todo.txt"

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

clear_console()

def addto(task):
    with open(LIST_FILE, "a") as f:
        towrite = "[ ] " + task + "\n"
        f.write(towrite)

def list_todo():
    if os.path.exists(LIST_FILE):
        with open(LIST_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    else:
        return []

def delete(index):
    tasks = list_todo()
    if index < 0 or index >= len(tasks):
        return f"Task number {index + 1} is out of range."

    being_removed = tasks.pop(index)

    with open(LIST_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")
    
    return f"Removed task {index + 1}: {being_removed}"

def done(index):
    tasks = list_todo()
    if index < 0 or index >= len(tasks):
        return f"Task number {index + 1} is out of range."

    # Remove existing '[ ]' or '[x]' at the start of the task, then add '[x]'
    task_text = tasks[index]
    # Strip leading '[ ] ' or '[x] ' from the task string if present
    if task_text.startswith("[ ] "):
        task_text = task_text[4:]  # remove first 4 chars '[ ] '
    elif task_text.startswith("[x] "):
        task_text = task_text[4:]  # remove first 4 chars '[x] '

    tasks[index] = f"[x] {task_text}"

    with open(LIST_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

    return f"Marked task {index + 1} as done: {tasks[index]}"


if len(sys.argv) < 2:
    print("Missing objective. Use 'help' for options.")
    sys.exit()

objective = sys.argv[1]
giventask = sys.argv[2] if len(sys.argv) > 2 and sys.argv[1] in ['add', 'done', 'remove'] else None


def check():
    if objective == 'help':
        print("Use 'list' to print, 'add' to add to list, 'remove' to delete, and 'done' to check off.\n")
        return False
    if objective in ['add', 'done', 'remove'] and not giventask:
        print("With 'add', write what to add. With 'done' or 'remove', give the task number.\n")
        return False
    return True
    

if check():
    if objective == 'add':
        addto(giventask)
        print(f"Added: {giventask}")

    elif objective == 'remove':
        if giventask.isdigit():
            deleted = delete(int(giventask)-1)
            print(deleted)
        else:
            print("Please enter a valid task number to remove.")

    elif objective == 'list':
        tasks = list_todo()
        if not tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}: {task}")
    elif objective == 'done':
        if giventask.isdigit():
            result = done(int(giventask) - 1)
            print(result)
        else:
            ("Please enter a valid task number to mark as done.")
