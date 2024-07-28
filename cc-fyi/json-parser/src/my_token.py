from enum import Enum
from typing import Self


class Token:
    class Kind(Enum):
        LBRACE = 0
        RBRACE = 1
        LSQUARE = 2
        RSQUARE = 3
        STRING = 4
        COLON = 5
        COMMA = 6
        MINUS = 7
        NUM = 8
        ID = 9
        WHITESPACE = 10

        NULL = 11
        FALSE = 12
        TRUE = 13

    def __init__(self, kind: "Token.Kind", lexeme: str):
        self.kind = kind
        self.lexeme = lexeme

    def __str__(self):
        return f"[ {self.kind}, {self.lexeme} ]"

    def get_kind(self) -> "Token.Kind":
        return self.kind

    def get_lexeme(self) -> str:
        return self.lexeme
