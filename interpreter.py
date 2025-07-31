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
    
    commands = []
    for c in content.split(";"):
        if len(c.strip()) > 0:
            commands.append(c.strip())
    
    print(commands)

    for command in commands:
        if len(command) > 0:
            run_command(command)
    

def run_command(command):
    parse_command(command)
    command = command.split(" ")
    index = 0

    while index < len(command):
        args = function_dict[command[index]][1]
        arg_index = 1
        tmp_args = []
        while arg_index <= args:
            tmp_args.append(command[index + arg_index].strip())
            arg_index += 1
        function_dict[command[index]][0](text_edit, tmp_args)
        index += args+1
    
    #print(f"command: {command}\nArgs: {args}")

def parse_command(command):
    index = 0
    for char in command:
        if char == '(':
            print(f"( at {index}")
        elif char == ')':
            print(f") at {index}")
        index += 1


def add_func(function, name, args):
    function_dict.update({name : [function, args]})

def execute(function):
    func = function_dict[function]
    func[0]()

