import tkinter as tk

side_button_index = 0

def add_button(frame, text, command):
    global side_button_index
    button = tk.Button(frame, text=text, command=command)
    button.grid(row=side_button_index, column=0, padx=5, pady=5, sticky="ew")
    side_button_index += 1