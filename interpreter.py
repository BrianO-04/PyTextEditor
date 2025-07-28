import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

function_dict = {}
text_edit = None

def load_script():
    fp = askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not fp:
        return
    with open(fp, "r", encoding='utf8') as f:
        content = f.read()
        f.close()
    
    content = content.split(" ")
    length = len(content)
    index = 0

    while index < length:
        if content[index] in function_dict:
            args = []
            total_args = function_dict[content[index]][1]
            tmp_idx = 0
            while tmp_idx < total_args:
                args.append(content[index+1+tmp_idx])
            function_dict[content[index]][0](text_edit, args)
            index = index + total_args

    print(content)

def add_func(function, name, args):
    function_dict.update({name : [function, args]})

def execute(function):
    func = function_dict[function]
    func[0]()

