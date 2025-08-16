from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    NUM = 0
    STRING = 1
    OPEN_PAREN = 2
    CLOSE_PAREN = 3
    COMMAND = 4
    SEMICOLON = 5

@dataclass
class Token:
    type: TokenType
    value: any = None