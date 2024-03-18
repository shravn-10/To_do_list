import tkinter
import random
from tkinter import messagebox

# Function to update the tasks displayed in the listbox
def update_tasks():
    clear_listbox()
    for task, completed in tasks:
        lb_tasks.insert("end", f"[{'x' if completed else ' '}] {task}")
    numtask = len(tasks)
    label_dsp_count['text'] = numtask

# Function to clear the listbox
def clear_listbox():
    lb_tasks.delete(0, "end")

# Function to add a new task
def add_task():
    label_dsply["text"] = ""
    Ntask = text_input.get()
    if Ntask != "":
        tasks.append((Ntask, False))
        update_tasks()
    else:
        label_dsply["text"] = "please enter the text"
    text_input.delete(0, 'end')

# Function to delete all tasks
def delete_all():
    conf = messagebox.askquestion('Delete all??', 'Are you sure to delete all tasks?')
    if conf.upper() == "YES":
        global tasks
        tasks = []
        update_tasks()
    else:
        pass

# Function to delete the selected task
def delete_one():
    selected_index = lb_tasks.curselection()
    if selected_index:
        index = selected_index[0]
        task, completed = tasks[index]
        if completed:
            conf = messagebox.askquestion('Unmark as Completed?', 'Do you want to unmark this task as completed?')
            if conf.upper() == "YES":
                tasks[index] = (task, False)
        else:
            tasks.pop(index)
        update_tasks()

# Function to mark the selected task as completed
def mark_completed():
    selected_index = lb_tasks.curselection()
    if selected_index:
        index = selected_index[0]
        task, completed = tasks[index]
        tasks[index] = (task, True)
        update_tasks()

# Function to edit the selected task
def edit_task():
    selected_index = lb_tasks.curselection()
    if selected_index:
        index = selected_index[0]
        task, _ = tasks[index]
        edit_window = tkinter.Toplevel(root)
        edit_window.title("Edit Task")
        edit_window.geometry("200x100")
        edit_window.grab_set()

        edit_label = tkinter.Label(edit_window, text="Edit Task:")
        edit_label.pack()

        edit_entry = tkinter.Entry(edit_window, width=15)
        edit_entry.insert(0, task)
        edit_entry.pack()

        def update_task():
            new_task = edit_entry.get()
            tasks[index] = (new_task, False)
            edit_window.destroy()
            update_tasks()

        update_button = tkinter.Button(edit_window, text="Update", command=update_task)
        update_button.pack()

# Function to show completed tasks
def show_completed():
    completed_window = tkinter.Toplevel(root)
    completed_window.title("Completed Tasks")
    completed_window.geometry("200x200")
    completed_window.grab_set()

    completed_tasks_listbox = tkinter.Listbox(completed_window)
    completed_tasks_listbox.pack()

    for task, completed in tasks:
        if completed:
            completed_tasks_listbox.insert("end", task)

# Function to show uncompleted tasks
def show_uncompleted():
    uncompleted_window = tkinter.Toplevel(root)
    uncompleted_window.title("Uncompleted Tasks")
    uncompleted_window.geometry("200x200")
    uncompleted_window.grab_set()

    uncompleted_tasks_listbox = tkinter.Listbox(uncompleted_window)
    uncompleted_tasks_listbox.pack()

    for task, completed in tasks:
        if not completed:
            uncompleted_tasks_listbox.insert("end", task)

# Function to sort tasks in ascending order
def sort_asc():
    tasks.sort(key=lambda x: x[0].lower())
    update_tasks()

# Function to sort tasks in descending order
def sort_dsc():
    tasks.sort(key=lambda x: x[0].lower(), reverse=True)
    update_tasks()

# Function to select and display a random task
def random_task():
    randtask = random.choice(tasks)
    label_dsply["text"] = randtask[0]

# Function to display the number of tasks
def number_task():
    numtask = len(tasks)
    label_dsply["text"] = numtask

# Function to save the tasks to a file
def save_act():
    savecon = messagebox.askquestion('Save Confirmation', 'Save your progress?')
    if savecon.upper() == "YES":
        with open("SaveFile.txt", "w") as filehandle:
            for task, _ in tasks:
                filehandle.write('%s\n' % task)
    else:
        pass

# Function to display information about the application
def load_info():
    messagebox.showinfo("Info", "This is a Todo List V.1.1\nCreated by\n1. Muhammad Nihaal\n2.M Sai Shravan\n3.Karthik\nPython Project")

# Function to load tasks from a file
def load_act():
    loadcon = messagebox.askquestion('Load Confirmation', 'Load your saved progress?')
    if loadcon.upper() == "YES":
        tasks.clear()
        with open('SaveFile.txt', 'r') as filereader:
            for line in filereader:
                currentask = line.strip()
                tasks.append((currentask, False))
            update_tasks()
    else:
        pass

# Function to exit the application
def exit_app():
    confex = messagebox.askquestion('Quit Confirmation', 'Are you sure you want to quit?')
    if confex.upper() == "YES":
        root.destroy()
    else:
        pass

root = tkinter.Tk() #init
root.configure(bg="white")
root.title("My Todo List")
root.geometry("500x700")

tasks = []

# GUI (graphical user interface)
label_title = tkinter.Label(root, text="Todo List", bg="#6C63FF", fg="white", font=("Arial", 24, "bold"))
label_title.grid(row=0, column=0, columnspan=4, pady=(20, 10))

label_dsply = tkinter.Label(root, text="", bg="#f0f0f0", font=("Arial", 12))
label_dsply.grid(row=0, column=4, columnspan=2, pady=(20, 10))

label_dsp_count = tkinter.Label(root, text="", bg="#f0f0f0", font=("Arial", 12))
label_dsp_count.grid(row=0, column=6, pady=(20, 10))

text_input = tkinter.Entry(root, width=30, font=("Arial", 12))
text_input.grid(row=1, column=1, columnspan=4, pady=(10, 0))

# Apply a consistent color scheme to buttons
button_bg_color = "#6C63FF"
button_fg_color = "white"

text_add_bttn = tkinter.Button(root, text="Add Task", bg=button_bg_color, fg=button_fg_color, font=("Arial", 12), command=add_task)
text_add_bttn.grid(row=1, column=0, padx=(10, 5), pady=(10, 0))

delone_bttn = tkinter.Button(root, text="Delete Task", bg="white", font=("Arial", 12), command=delete_one)
delone_bttn.grid(row=3, column=0)

delall_bttn = tkinter.Button(root, text="Delete All", bg="white", font=("Arial", 12), command=delete_all)
delall_bttn.grid(row=3, column=1)

markcomp_bttn = tkinter.Button(root, text="Mark Completed", bg="white", font=("Arial", 12), command=mark_completed)
markcomp_bttn.grid(row=4, column=0)

edit_bttn = tkinter.Button(root, text="Edit Task", bg="white", font=("Arial", 12), command=edit_task)
edit_bttn.grid(row=4, column=1)

showcomp_bttn = tkinter.Button(root, text="Show Completed", bg="white", font=("Arial", 12), command=show_completed)
showcomp_bttn.grid(row=5, column=0)

showuncomp_bttn = tkinter.Button(root, text="Show Uncompleted", bg="white", font=("Arial", 12), command=show_uncompleted)
showuncomp_bttn.grid(row=5, column=1)

sortasc_bttn = tkinter.Button(root, text="Sort (ASC)", bg="white", font=("Arial", 12), command=sort_asc)
sortasc_bttn.grid(row=6, column=0)

sortdsc_bttn = tkinter.Button(root, text="Sort (DSC)", bg="white", font=("Arial", 12), command=sort_dsc)
sortdsc_bttn.grid(row=6, column=1)

random_bttn = tkinter.Button(root, text="Random Task", bg="white", font=("Arial", 12), command=random_task)
random_bttn.grid(row=7, column=0)

numtask_bttn = tkinter.Button(root, text="Number of Tasks", bg="white", font=("Arial", 12), command=number_task)
numtask_bttn.grid(row=7, column=1)

exit_bttn = tkinter.Button(root, text="Exit App", bg="white", font=("Arial", 12), command=exit_app)
exit_bttn.grid(row=8, column=0)

save_button = tkinter.Button(root, text="Save TodoList", bg="white", font=("Arial", 12), command=save_act)
save_button.grid(row=9, column=3, columnspan=2)

load_button = tkinter.Button(root, text="Load Last TodoList", bg="white", font=("Arial", 12), command=load_act)
load_button.grid(row=9, column=1, columnspan=2)

info_button = tkinter.Button(root, text="Info", bg="white", font=("Arial", 12), command=load_info)
info_button.grid(row=10, column=0)

listbox_bg_color = "#EAEAEA"
listbox_fg_color = "black"

lb_tasks = tkinter.Listbox(root, height=12, width=45, bg=listbox_bg_color, fg=listbox_fg_color, font=("Arial", 12))
lb_tasks.grid(row=2, column=0, columnspan=7, padx=10, pady=(5, 0))

scrollbar = tkinter.Scrollbar(root, command=lb_tasks.yview)
scrollbar.grid(row=2, column=7, rowspan=12, sticky='ns')
lb_tasks.config(yscrollcommand=scrollbar.set)

root.mainloop()
