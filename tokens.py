from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    NUM = 0
    STRING = 1
    SUB_COMMAND = 2
    COMMAND = 3
    SEMICOLON = 4

@dataclass
class Token:
    type: TokenType
    value: any = None