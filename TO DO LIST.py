import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []
        self.setup()
        self.root.config(bg="pink")

    def setup(self):
        heading = tk.Label(self.root, text="TO-DO LIST", font=("Arial", 16, "bold"), bg="purple")
        heading.grid(row=0, column=0, columnspan=3, pady=15)

        self.entry = tk.Entry(self.root, width=40,font=("Arial ",16))
        self.entry.grid(row=1, column=0, padx=30, pady=20, columnspan=2)

        self.priority_var = tk.StringVar()
        self.priority_var.set("Priority")
        priorities = ["High", "Medium", "Low"]
        self.priority_menu = tk.OptionMenu(self.root, self.priority_var, *priorities)
        self.priority_menu.config(font=("Arial ",14))
        self.priority_menu.grid(row=2, column=0, padx=20,pady=20, columnspan=3)

        add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_button.grid(row=1, column=2, padx=20)

        self.listbox = tk.Listbox(self.root, width=50,font=("Arial",18))
        self.listbox.grid(row=3, column=0, columnspan=3, pady=10, padx=20)

        mark_done_button = tk.Button(self.root, text="Mark as Done", command=self.mark_done)
        mark_done_button.grid(row=4, column=0, padx=10, pady=5)

        delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        delete_button.grid(row=4, column=1, padx=10, pady=5)

        clear_button = tk.Button(self.root, text="Clear All", command=self.clear_tasks)
        clear_button.grid(row=4, column=2, padx=10, pady=5)

    def add_task(self):
        name = self.entry.get().strip()
        priority = self.priority_var.get()
        if name:
            self.tasks.append({"name": name, "priority": priority, "completed": False})
            self.update_list()
            self.entry.delete(0, tk.END)

    def update_list(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task["completed"] else "✗"
            item = f"[{status}] {task['name']} (Priority: {task['priority']})"
            self.listbox.insert(tk.END, item)

    def mark_done(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = True
            self.update_list()
        else:
            messagebox.showinfo("Select Task", "Please select a task to mark as done.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            del self.tasks[selected[0]]
            self.update_list()
        else:
            messagebox.showinfo("Select Task", "Please select a task to delete.")

    def clear_tasks(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
            self.tasks.clear()
            self.update_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
