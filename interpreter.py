import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from lexer import Lexer
from tokens import Token, TokenType

class Interpreter:
    def __init__(self, text_edit):
        self.function_dict = {}
        self.text_edit = text_edit

    def advance(self):
        try:
            self.current_token = next(self.commands)
        except StopIteration:
            self.current_token = None

    def add_func(self, func, name, args):
        self.function_dict.update({name : [func, args]})

    # creates and returns an iteratable list of command tokens from text
    def parse(self, text):
        lexer = Lexer(text)
        commands = lexer.generate_tokens()
        commands = iter(list(commands))
        return commands

    def execute(self, text):
        self.commands = self.parse(text)
        self.advance()

        while self.current_token != None:
            if self.current_token.type == TokenType.COMMAND:
                self.run_command()

    def run_command(self):
        if self.current_token.value not in self.function_dict:
            raise Exception(f"Function {self.current_token.value} not found in namespace")

        command = self.current_token.value
        args = []

        self.advance()
        while (self.current_token != None) and (self.current_token.type != TokenType.SEMICOLON):
            if self.current_token.type == TokenType.NUM or self.current_token.type == TokenType.STRING:
                args.append(self.current_token.value)
                self.advance()
            elif self.current_token.type == TokenType.SUB_COMMAND:
                
                tmp_interpreter = Interpreter(self.text_edit)
                tmp_interpreter.function_dict = self.function_dict
                tmp_commands = tmp_interpreter.parse(self.current_token.value)
                tmp_interpreter.commands = tmp_commands
                tmp_interpreter.advance()

                args.append(tmp_interpreter.run_command())
                self.advance()
            elif self.current_token.type == TokenType.COMMAND:
                raise Exception(f"Function can not take command '{self.current_token.value}' as an argument")
        
        self.advance()
        print(f'Command: {command}\nArgs: {args}')
        return self.function_dict[command][0](self.text_edit, args)



# function_dict = {}
# text_edit = None

# def load_script():
#     fp = askopenfilename(filetypes=[("Text Files", "*.txt")])
#     if not fp:
#         return
#     with open(fp, "r", encoding='utf8') as f:
#         content = f.read()
#         f.close()
    
#     lexer = Lexer(content)
#     commands = lexer.generate_tokens()
#     commands = iter(list(commands))
    
#     try:
#         current_token = next(commands)
#     except StopIteration:
#         current_token = None

#     while current_token != None:
#         if current_token.type == TokenType.COMMAND:
#             pass



# def add_func(function, name, args):
#     function_dict.update({name : [function, args]})

# def execute(function):
#     func = function_dict[function]
#     func[0]()

