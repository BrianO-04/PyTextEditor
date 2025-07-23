import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import *

def save(window, text_edit):
    fp = asksaveasfilename(filetypes=[("Text Files", "*.txt")])

    if not fp:
        return
    
    with open(fp, "w", encoding='utf8') as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
        f.close()
    window.title(f"{fp}")

def load(window, text_edit):
    fp = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not fp:
        return
    
    text_edit.delete(1.0, tk.END)
    with open(fp, "r", encoding='utf8') as f:
        content = f.read()
        text_edit.insert(tk.END, content)
        f.close()
    window.title(f"{fp}")

def replace_window(window, text_edit):
    global replace_popup
    replace_popup = Tk()
    replace_popup.title("Replace All")
    replace_popup.geometry("500x150")
    
    rep_frame = Frame(replace_popup)
    rep_frame.pack(pady=5)

    buttons_frame = Frame(replace_popup)
    buttons_frame.pack(pady=5, side=tk.BOTTOM)

    orig_label = Label(rep_frame, text="Original text: ")
    orig_inp_frame = Frame(rep_frame, width=400, height=50)
    orig_inp_frame.grid_propagate(False)
    orig_inp = tk.Text(orig_inp_frame, font="Helvetica 18")
    orig_inp.grid(row=0, column=0)

    new_label = Label(rep_frame, text="New text: ")
    new_inp_frame = Frame(rep_frame, width=400, height= 50)
    new_inp_frame.grid_propagate(False)
    new_inp = tk.Text(new_inp_frame, font="Helvetica 18")
    new_inp.grid(row=0, column=0)

    orig_label.grid(row=0, column=0)
    orig_inp_frame.grid(row=0, column=1)

    new_label.grid(row=1, column=0)
    new_inp_frame.grid(row=1, column=1)

    confirm = Button(buttons_frame, text="Confirm", command=lambda: replace(window, text_edit, orig_inp.get(1.0, tk.END).strip(), new_inp.get(1.0, tk.END).strip()))
    cancel = Button(buttons_frame, text="Cancel", command=replace_popup.destroy)

    confirm.grid(row=0, column=0, pady=5, padx=5)
    cancel.grid(row=0, column=1, pady=5, padx=5)

def replace(window, text_edit, original, replace):
    content = text_edit.get(1.0, tk.END)
    first_index = content.find(original)

    print(original)
    print(replace)

    if first_index == -1:
        replace_popup.destroy()
        return

    new_content = ""

    while first_index != -1:
        new_content += content[:first_index] + replace
        content = content[first_index+len(original):]
        first_index = content.find(original)
        if first_index == -1:
            new_content += content

    text_edit.delete(1.0, tk.END)
    text_edit.insert(tk.END, new_content[:-1])

    replace_popup.destroy()

def remove_at_index(window, text_edit, index):
    content = text_edit.get(1.0, tk.END)
    if index > len(content):
        return

    new_content = content[:index-1] + content[index:-1]
    text_edit.delete(1.0, tk.END)
    text_edit.insert(tk.END, new_content)

def add_at_index(text_edit, index, string):
    content = text_edit.get(1.0, tk.END)
    if index > len(content):
        index = len(content)

    new_content = content[:index] + string + content[index:-1]
    text_edit.delete(1.0, tk.END)
    text_edit.insert(tk.END, new_content)

def main():
    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    text_edit = tk.Text(window, font="Helvetica 18")
    text_edit.grid(row=0, column=1)

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    
    save_button = tk.Button(frame, text="Save", command=lambda: save(window, text_edit))
    open_button = tk.Button(frame, text="Open", command=lambda: load(window, text_edit))
    replace_button = tk.Button(frame, text="Replace all", command=lambda: replace_window(window, text_edit))

    #TEMP BUTTONS
    remove_at_button = tk.Button(frame, text="Remove at index", command=lambda: remove_at_index(window, text_edit, 5))
    add_at_button = tk.Button(frame, text="Add at index", command=lambda: add_at_index(text_edit, 5, "test"))

    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    replace_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    remove_at_button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
    add_at_button.grid(row=4, column=0, padx=5, pady=5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns")

    window.bind("<Control-s>", lambda x: save(window, text_edit))
    window.bind("<Control-o>", lambda x: open(window, text_edit))

    window.mainloop()

main()