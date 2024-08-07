from collections import defaultdict
from typing import Self, DefaultDict, Set
from typing import List, Any
from my_token import Token
from json_exceptions import JSONParserException


# singleton
class JSONParser:
    _instance: Self = None
    NONTERMINALS = ".NONTERMINALS"
    RULES = ".RULES"
    LOOKUP = ".LOOKUP"
    END = ".END"

    def __new__(cls, *args: Any, **kwargs: Any) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self._read_cfg("../rules.txt")

    def parse(self, input: List[Token]) -> List[str]:
        try:
            self._ll1_parse(input)
            fi = self._formatted_input(input)
            return fi
        except JSONParserException as e:
            raise e

    def _formatted_input(self, input: List[Token]) -> List[str]:
        output = []
        whitespace_count: int = 0
        for token in input:
            match token.get_kind():
                case Token.Kind.LBRACE:
                    output.append("{")
                    output.append("\n")
                    whitespace_count += 1
                    output.append(" " * whitespace_count * 2)
                case Token.Kind.RBRACE:
                    whitespace_count -= 1
                    output.append("\n")
                    output.append(" " * whitespace_count * 2)
                    output.append("}")
                case Token.Kind.LSQUARE:
                    output.append("[")
                    output.append("\n")
                    whitespace_count += 1
                    output.append(" " * whitespace_count * 2)
                case Token.Kind.RSQUARE:
                    whitespace_count -= 1
                    output.append("\n")
                    output.append(" " * whitespace_count * 2)
                    output.append("]")
                case Token.Kind.STRING:
                    output.append(f"{token.get_lexeme()}")
                case Token.Kind.COLON:
                    output.append(": ")
                case Token.Kind.COMMA:
                    output.append(",")
                    output.append("\n")
                    output.append(" " * whitespace_count * 2)
                case Token.Kind.MINUS:
                    output.append("-")
                case Token.Kind.NUM:
                    output.append(token.get_lexeme())
                case Token.Kind.NULL:
                    output.append("null")
                case Token.Kind.FALSE:
                    output.append("false")
                case Token.Kind.TRUE:
                    output.append("true")
        output = "".join(output)
        return output

    def _ll1_parse(self, input: List[Token]) -> None:
        stack: List[str] = ["start"]
        input = (
            [
                Token(Token.Kind.BOF, "BOF"),
            ]
            + input
            + [
                Token(Token.Kind.EOF, "EOF"),
            ]
        )
        for token in input:
            # replace nontermainsl with terminal
            while stack and stack[-1] in self._non_terminals:
                non_terminal = stack.pop()
                if (non_terminal not in self._lookup) or (
                    token.get_kind().name not in self._lookup[non_terminal]
                ):
                    raise JSONParserException(f"Unexpected token: {token.get_lexeme()}")
                    return False  # error, unable to find a suitable rule
                rule_number = self._lookup[non_terminal][token.get_kind().name]
                rule = self._rules[rule_number]
                # not nullable rule
                if len(rule) > 1:

                    stack.extend(reversed(rule[1:]))

            # check if terminal matches
            if stack and stack[-1] == token.get_kind().name:
                stack.pop()
            else:
                raise JSONParserException(
                    f"Unexpected token: {token.get_lexeme()}, expected a {stack[-1]}"
                )
                return False
        # return True

    def _read_cfg(self, filename: str):
        self._rules: DefaultDict[int, List[str]] = defaultdict(list)
        self._lookup: DefaultDict[str, DefaultDict[str, int]] = defaultdict(
            lambda: defaultdict(int)
        )
        self._non_terminals: Set[str] = set()
        with open(filename, "r") as file:
            # remove first header
            file.readline()
            # retrieve all non terminals
            for line in file:
                line = line.strip()
                if line == JSONParser.RULES:
                    break
                self._non_terminals.add(line)

            rule_number: int = 0
            # retrieve all the rules
            for line in file:
                line = line.strip()
                if line == JSONParser.LOOKUP:
                    break
                line = line.split(" ")
                self._rules[rule_number] = line
                rule_number += 1

            # retrieve predict table
            for line in file:
                line = line.strip()
                if line == JSONParser.END:
                    break
                line = line.split(" ")
                non_terminal, terminal = line[0], line[1]
                rule_number = int(line[2])
                self._lookup[non_terminal][terminal] = rule_number
