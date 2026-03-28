import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")

tasks = []


def refresh_tasks():
    listbox.delete("1.0", "end")

    for task in tasks:
        listbox.insert("end", task + "\n")


def add_task():
    task = entry.get()

    if not task:
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return

    tasks.append(task)
    refresh_tasks()
    entry.delete(0, "end")


def delete_task():
    try:
        selected = listbox.get("sel.first", "sel.last").strip()

        if selected in tasks:
            tasks.remove(selected)

        refresh_tasks()

    except:
        messagebox.showwarning("Warning", "Select a task first!")


def clear_tasks():
    tasks.clear()
    refresh_tasks()


app = ctk.CTk()

app.title("ToDo Task Manager")

app.geometry("400x350")

entry = ctk.CTkEntry(app, width=150)
entry.pack(pady=5)

add_btn = ctk.CTkButton(app, text="Add", command=add_task)
add_btn.pack(pady=3)

delete_btn = ctk.CTkButton(app, text="Delete", command=delete_task)
delete_btn.pack(pady=3)

clear_btn = ctk.CTkButton(app, text="Clear", command=clear_tasks)
clear_btn.pack(pady=3)

listbox = ctk.CTkTextbox(app, width=200, height=60)
listbox.pack(pady=5)

app.mainloop()


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed")

    return a / b
