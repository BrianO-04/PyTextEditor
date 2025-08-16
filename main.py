import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import uiHandler as ui
from interpreter import Interpreter

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

def replace(text_edit, inputs):
    inputs = ui.get_text_input(inputs)
    content = text_edit.get(1.0, tk.END)
    first_index = content.find(inputs[0])

    if first_index == -1:
        ui.close_popup()
        return

    new_content = ""

    while first_index != -1:
        new_content += content[:first_index] + inputs[1]
        content = content[first_index+len(inputs[0]):]
        first_index = content.find(inputs[0])
        if first_index == -1:
            new_content += content

    text_edit.delete(1.0, tk.END)
    text_edit.insert(tk.END, new_content[:-1])

    ui.close_popup()
    return 1

def remove_at_index(text_edit, index):
    index = ui.get_text_input(index)
    index = index[0]
    try:
        index = int(index)
    except:
        print("Expected an integer as input")
        return

    content = text_edit.get(1.0, tk.END)
    
    if index > len(content):
        return

    new_content = content[:index-1] + content[index:-1]
    text_edit.delete(1.0, tk.END)
    text_edit.insert(tk.END, new_content)

def add_at_index(text_edit, inputs):
    inputs = ui.get_text_input(inputs)
    content = text_edit.get(1.0, tk.END)
    try:
        index = int(inputs[0])
    except:
        print("Expected an integer as first input")
        return
    
    if index > len(content):
        index = len(content)

    new_content = content[:index] + inputs[1] + content[index:-1]
    text_edit.delete(1.0, tk.END)
    text_edit.insert(tk.END, new_content)
    ui.close_popup()

def find_first(text_edit, inputs):
    content = text_edit.get(1.0, tk.END)
    first_index = content.find(inputs[0])
    return first_index

def contains(text_edit, inputs):
    content = text_edit.get(1.0, tk.END)
    first_index = content.find(inputs[0])
    if first_index == -1:
        return 0
    return 1

def if_equal(text_edit, inputs):
    return inputs[0] == inputs[1]

def invert_func(text_edit, inputs):
    return not inputs[0]

def get_index(text_edit, inputs):
    index = int(inputs[0])
    found = text_edit.get(1.0, tk.END)[index]
    return found

def load_script():
    fp = askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not fp:
        return
    with open(fp, "r", encoding='utf8') as f:
        content = f.read()
        f.close()
    return content

def add_funcs(environment):
    environment.add_func(invert_func, "not", 1)
    environment.add_func(replace, "replace", 2)
    environment.add_func(remove_at_index, "remove", 2)
    environment.add_func(add_at_index, "add", 2)
    environment.add_func(find_first, "find", 1)
    environment.add_func(get_index, "get", 1)
    environment.add_func(contains, "contains", 1)
    environment.add_func(if_equal, "equals", 2)


def main():
    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    text_edit = tk.Text(window, font="Helvetica 18")
    text_edit.grid(row=0, column=1)

    interpret = Interpreter(text_edit)

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    frame.grid(row=0, column=0, sticky="ns")

    ui.add_side_button(frame, "Save", lambda: save(window, text_edit))
    ui.add_side_button(frame, "Open", lambda: load(window, text_edit))
    ui.add_side_button(frame, "Replace All", lambda: ui.create_popup(text_edit, "Replace All", ["Original: ", "New: "], replace))

    #TEMP BUTTONS
    ui.add_side_button(frame, "Remove at index", lambda: ui.create_popup(text_edit, "Add at index", ["Index: "], remove_at_index))
    ui.add_side_button(frame, "Add at index", lambda: ui.create_popup(text_edit, "Add at index", ["Index: ", "New Text: "], add_at_index))
    ui.add_side_button(frame, "Interpreter Test", lambda: interpret.execute(load_script()))

    window.bind("<Control-s>", lambda x: save(window, text_edit))
    window.bind("<Control-o>", lambda x: open(window, text_edit))

    add_funcs(interpret)

    window.mainloop()

main()