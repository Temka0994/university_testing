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

    tasks.append(task)

    refresh_tasks()
    entry.delete(0, "end")


def delete_task():
    try:
        tasks.pop()
        refresh_tasks()
    except:
        messagebox.showwarning("Warning", "There are no tasks!")


def clear_tasks():
    listbox.delete("1.0", "end")


app = ctk.CTk()

app.title("Todo")

app.geometry("250x200")

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
