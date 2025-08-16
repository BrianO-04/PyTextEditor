from tokens import Token, TokenType

WHITESPACE = ' \n\t'
DIGITS = '123456789'
QUOTES = '"\''

class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()
        
    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char != None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char in DIGITS:
                yield self.generate_num()
            elif self.current_char in QUOTES:
                yield self.generate_string()
            elif self.current_char.isalpha():
                yield self.generate_cmd()
            elif self.current_char == '(':
                yield self.generate_sub()
            elif self.current_char == ';':
                self.advance()
                yield Token(TokenType.SEMICOLON)
            else:
                raise Exception(f'Illegal char {self.current_char}')


    def generate_cmd(self):
        cmd = ''
        cmd += self.current_char
        self.advance()
        while self.current_char != None and self.current_char.isalpha():
            cmd += self.current_char
            self.advance()
        return Token(TokenType.COMMAND, cmd)

    def generate_num(self):
        num_str = self.current_char
        self.advance()
        while self.current_char != None and self.current_char in DIGITS:
            num_str += self.current_char
            self.advance()
        return Token(TokenType.NUM, int(num_str))
    
    def generate_string(self):
        quote_type = self.current_char #record if it is started with a ' or a "
        final_str = ''
        self.advance()
        while self.current_char != None and self.current_char != quote_type:
            final_str += self.current_char
            self.advance()
        self.advance()
        return Token(TokenType.STRING, final_str)
    
    def generate_sub(self):
        self.advance()
        final = ''
        extra_parens = 0
        while self.current_char != ')' or extra_parens > 0:
            if self.current_char == '(':
                extra_parens += 1
            elif self.current_char == ')':
                extra_parens -= 1
            final += self.current_char
            self.advance()
        self.advance()
        return Token(TokenType.SUB_COMMAND, final)