from datetime import datetime, date

def get_time():
    return datetime.now().strftime("%I:%M %p")

def get_date():
    return date.today().strftime("%d-%m-%Y")

def say_hello():
    return "Hello Hardik! 👋 Welcome back."

def calculate(expression):
    try:
        return str(eval(expression))
    except:
        return "Invalid calculation."
    
def save_note(note):

    with open("notes.txt", "a") as file:
        file.write(note + "\n")

    return "Note saved successfully."


def show_notes():

    try:
        with open("notes.txt", "r") as file:
            notes = file.read()

        if notes.strip() == "":
            return "No notes found."

        return notes

    except FileNotFoundError:
        return "No notes found."
    
def add_task(task):

    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

    return "Task added successfully."


def show_tasks():

    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            return "No tasks found."

        output = ""

        for index, task in enumerate(tasks, start=1):
            output += f"{index}. {task}"

        return output

    except FileNotFoundError:
        return "No tasks found."


def delete_task(task_number):

    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        task_number = int(task_number)

        if task_number < 1 or task_number > len(tasks):
            return "Invalid task number."

        tasks.pop(task_number - 1)

        with open("tasks.txt", "w") as file:
            file.writelines(tasks)

        return "Task deleted successfully."

    except:
        return "Invalid task number."