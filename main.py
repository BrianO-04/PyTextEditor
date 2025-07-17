import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def save(window, text_edit):
    fp = asksaveasfilename(filetypes=[("Text Files", "*.txt")])

    if not fp:
        return
    
    with open(fp, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
        f.close()
    window.title(f"{fp}")

def load(window, text_edit):
    fp = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not fp:
        return
    
    text_edit.delete(1.0, tk.END)
    with open(fp, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
        f.close()
    window.title(f"{fp}")


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

    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns")

    window.bind("<Control-s>", lambda x: save(window, text_edit))
    window.bind("<Control-o>", lambda x: open(window, text_edit))

    window.mainloop()

main()