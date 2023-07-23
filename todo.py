import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

def edit_task():
    try:
        index = listbox.curselection()[0]
        task = listbox.get(index)
        new_task = entry.get()
        if new_task:
            listbox.delete(index)
            listbox.insert(index, new_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")
    except IndexError:
        pass

def delete_task():
    try:
        index = listbox.curselection()[0]
        confirmed = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this task?")
        if confirmed:
            listbox.delete(index)
    except IndexError:
        pass

def main():
    global entry, listbox

    root = tk.Tk()
    root.title("To-Do List")

    # Create a frame
    frame = tk.Frame(root)
    frame.pack(pady=10)

    # Create a listbox
    listbox = tk.Listbox(
        frame,
        width=50,
        height=10,
        font=("Baloo Bhai", 12),
        bd=0,
        selectbackground="#a6a6a6"
    )
    listbox.pack(side=tk.LEFT, fill=tk.BOTH)

    # Create a scrollbar
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

    # Add scrollbar to the listbox
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    # Create an entry widget
    entry = tk.Entry(
        root,
        font=("Baloo Bhai", 12)
    )
    entry.pack(pady=10)

    # Create buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    add_button = tk.Button(
        button_frame,
        text="Add Task",
        command=add_task,
        font=("Baloo Bhai", 12)
    )
    add_button.pack(side=tk.LEFT)

    edit_button = tk.Button(
        button_frame,
        text="Edit Task",
        command=edit_task,
        font=("Baloo Bhai", 12)
    )
    edit_button.pack(side=tk.LEFT)

    delete_button = tk.Button(
        button_frame,
        text="Delete Task",
        command=delete_task,
        font=("Baloo Bhai", 12)
    )
    delete_button.pack(side=tk.LEFT)

    root.mainloop()

if __name__ == "__main__":
    main()
