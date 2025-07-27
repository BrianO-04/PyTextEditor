import tkinter as tk
from tkinter import *

side_button_index = 0
side_buttons = []

def add_side_button(frame, text, command):
    global side_button_index
    global side_buttons
    button = tk.Button(frame, text=text, command=command)
    button.grid(row=side_button_index, column=0, padx=5, pady=5, sticky="ew")
    side_button_index += 1
    side_buttons.append(button)

def create_popup(window, text_edit, window_title, input_boxes, command):
    global popup_window
    popup_window = Tk()

    popup_window.title(window_title)
    size = len(input_boxes) * 50 + 60
    print(size)
    popup_window.geometry(f"500x{size}")
    
    frame = Frame(popup_window)
    frame.pack(pady=5)

    buttons_frame = Frame(popup_window)
    buttons_frame.pack(pady=5, side=tk.BOTTOM)

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

    confirm = Button(buttons_frame, text="Confirm", command=command)
    cancel = Button(buttons_frame, text="Cancel", command=popup_window.destroy)

    confirm.grid(row=0, column=0, pady=5, padx=5)
    cancel.grid(row=0, column=1, pady=5, padx=5)