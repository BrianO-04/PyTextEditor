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
    index = 0

    while index < len(content):
        args = function_dict[content[index]][1]
        arg_index = 1
        tmp_args = []
        while arg_index <= args:
            tmp_args.append(content[index + arg_index].strip())
            arg_index += 1
        function_dict[content[index]][0](text_edit, tmp_args)
        index += args+1
    
    print(f"content: {content}\nArgs: {args}")

def add_func(function, name, args):
    function_dict.update({name : [function, args]})

def execute(function):
    func = function_dict[function]
    func[0]()

