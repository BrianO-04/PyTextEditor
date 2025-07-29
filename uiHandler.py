import tkinter as tk
from tkinter import *

side_button_index = 0
side_buttons = []

popup_open = False

def add_side_button(frame, text, command):
    global side_button_index
    global side_buttons
    button = tk.Button(frame, text=text, command=command)
    button.grid(row=side_button_index, column=0, padx=5, pady=5, sticky="ew")
    side_button_index += 1
    side_buttons.append(button)

#any command given must take 3 parameters, window, text_edit, and inputs array
def create_popup(text_edit, window_title, input_boxes, command):
    global popup_window
    global popup_open

    if popup_open:
        return
    else:
        popup_open = True

    popup_window = Tk()
    popup_window.protocol("WM_DELETE_WINDOW", close_popup)

    popup_window.title(window_title)
    size = len(input_boxes) * 50 + 60
    popup_window.geometry(f"500x{size}")
    
    frame = Frame(popup_window)
    frame.pack(pady=5)

    buttons_frame = Frame(popup_window)
    buttons_frame.pack(pady=5, side=tk.BOTTOM)

    inputs = []

    cur_row = 0
    for x in input_boxes:
        label = Label(frame, text=x)
        inp_frame = Frame(frame, width=400, height=50)
        inp_frame.grid_propagate(False)
        inp = tk.Text(inp_frame, font="Helvetica 18")
        inp.grid(row=0, column=0)

        label.grid(row=cur_row, column=0)
        inp_frame.grid(row=cur_row, column=1)
        cur_row += 1
        
        inputs.append(inp)

    confirm = Button(buttons_frame, text="Confirm", command=lambda: command(text_edit, inputs))
    cancel = Button(buttons_frame, text="Cancel", command=lambda: close_popup())

    confirm.grid(row=0, column=0, pady=5, padx=5)
    cancel.grid(row=0, column=1, pady=5, padx=5)

def close_popup():
    global popup_open
    if popup_open:
        popup_window.destroy()
    popup_open = False

def get_text_input(text_boxes):
    if type(text_boxes[0]) != tk.Text:
        return text_boxes
    output = []
    for x in text_boxes:
        output.append(x.get(1.0, tk.END).strip())
    return output