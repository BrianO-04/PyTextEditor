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

    for command in commands:
        if len(command) > 0:
            # parse_command(command)
            print(split_command(command))
    

def parse_command(command):
    command = split_command(command)

    if command[0] not in function_dict:
        return command
    else:
        idx = 1
        while idx < len(command):
            command[idx] = split_command(command[idx])
            
            if command[idx][0] in function_dict:
                command[idx] = run_command(command[idx])

            idx += 1

    print(command)
    return run_command(command)

def run_command(command):
    return function_dict[command[0]][0](text_edit, command[1:])

    # index = 0

    # while index < len(command):
    #     args = function_dict[command[index]][1]
    #     arg_index = 1
    #     tmp_args = []
    #     while arg_index <= args:
    #         tmp_args.append(command[index + arg_index].strip())
    #         arg_index += 1
    #     function_dict[command[index]][0](text_edit, tmp_args)
    #     index += args+1
    
    
def split_command(command):
    index = 0
    fst_index = 0

    sub_commands = []

    parens_index = 0 #tracks the index of the current parentheses
    open_parens = 0
    close_parens = 0

    for char in command:
        if char == ' ' and open_parens == 0 and index != fst_index:
            sub_commands.append(command[fst_index:index])
            fst_index = index+1
        elif char == '(':
            if open_parens == 0:
                parens_index = index
            open_parens += 1
        elif char == ')':
            close_parens += 1
            if open_parens == close_parens == 1:
                sub_commands.append([command[parens_index+1:index]])
                fst_index = index+1
                open_parens = 0
                close_parens = 0
            elif (open_parens == close_parens) and open_parens > 1:
                sub_commands.append(split_command(command[parens_index+1:index]))
                fst_index = index+1
                open_parens = 0
                close_parens = 0
        elif index == len(command)-1:
            sub_commands.append(command[fst_index:index+1])
        index += 1

    final = []

    return sub_commands


def add_func(function, name, args):
    function_dict.update({name : [function, args]})

def execute(function):
    func = function_dict[function]
    func[0]()

