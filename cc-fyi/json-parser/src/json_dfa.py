from typing import Self, Type, Any, Set, DefaultDict, overload, Callable
from my_token import Token
from enum import Enum
from collections import defaultdict


# singleton
class JSONDFA:
    class State(Enum):
        START = 0
        FAIL = 1
        LBRACE = 2
        RBRACE = 3
        LSQUARE = 4
        RSQUARE = 5
        OPEN_QUOTE = 6
        STRING = 7
        CLOSE_QUOTE = 8
        COLON = 9
        COMMA = 10
        NUM = 12
        MINUS = 13
        ID = 14
        WHITESPACE = 15

    _instance: Self = None
    _NUM_ASCII_CHARS: int = 128
    _accepting_states: Set["JSONDFA.State"]
    _transitions: DefaultDict["JSONDFA.State", DefaultDict[int, "JSONDFA.State"]] = (
        defaultdict(lambda: defaultdict(int))
    )

    def __new__(self: Type[Self], *args: Any, **kwargs: Any) -> Self:
        if self._instance is None:
            self._instance = super().__new__(self)
        return self._instance

    def __init__(self) -> None:
        for i in JSONDFA.State:
            for j in range(JSONDFA._NUM_ASCII_CHARS):
                JSONDFA._transitions[i][j] = JSONDFA.State.FAIL

        self._fill_accepting_states()

        self._register_transition(JSONDFA.State.START, "{", JSONDFA.State.LBRACE)
        self._register_transition(JSONDFA.State.START, "}", JSONDFA.State.RBRACE)
        self._register_transition(JSONDFA.State.START, "[", JSONDFA.State.LSQUARE)
        self._register_transition(JSONDFA.State.START, "]", JSONDFA.State.RSQUARE)
        self._register_transition(JSONDFA.State.START, '"', JSONDFA.State.OPEN_QUOTE)
        self._register_transition(JSONDFA.State.START, ":", JSONDFA.State.COLON)
        self._register_transition(JSONDFA.State.START, ",", JSONDFA.State.COMMA)
        self._register_transition(JSONDFA.State.START, "0123456789", JSONDFA.State.NUM)
        self._register_transition(JSONDFA.State.NUM, "0123456789", JSONDFA.State.NUM)
        self._register_transition(JSONDFA.State.START, "-", JSONDFA.State.MINUS)

        self._register_transitions(
            JSONDFA.State.START,
            lambda x: chr(x) in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_",
            JSONDFA.State.ID,
        )
        self._register_transitions(
            JSONDFA.State.ID,
            lambda x: chr(x)
            in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789",
            JSONDFA.State.ID,
        )

        self._register_transitions(
            JSONDFA.State.OPEN_QUOTE,
            lambda x: chr(x)
            in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~",
            JSONDFA.State.STRING,
        )
        self._register_transitions(
            JSONDFA.State.STRING,
            lambda x: chr(x)
            in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 	",
            JSONDFA.State.STRING,
        )
        self._register_transition(JSONDFA.State.STRING, '"', JSONDFA.State.CLOSE_QUOTE)

        self._register_transitions(
            JSONDFA.State.START,
            lambda x: chr(x) in " \t\n\r\x0b\x0c",
            JSONDFA.State.WHITESPACE,
        )

    def tokenise(self, input: str) -> list[Token]:
        current_state: JSONDFA.State = JSONDFA.State.START
        tokens: list[Token] = []
        n: int = len(input)
        munched_input: str = ""

        i: int = 0
        while i < n:
            c = input[i]
            next_state = JSONDFA._transitions[current_state][ord(c)]
            # if this is end of the input or the next state is a fail
            if next_state == JSONDFA.State.FAIL:
                # check whether or not the current state is accepting
                if current_state in JSONDFA._accepting_states:
                    # handle special keywords
                    if current_state == JSONDFA.State.ID:
                        match munched_input:
                            case "null":
                                tokens.append(Token(Token.Kind.NULL, munched_input))
                            case "false":
                                tokens.append(Token(Token.Kind.FALSE, munched_input))
                            case "true":
                                tokens.append(Token(Token.Kind.TRUE, munched_input))
                            case _:
                                tokens.append(
                                    Token(
                                        self._state_to_kind(current_state),
                                        munched_input,
                                    )
                                )
                    else:
                        tokens.append(
                            Token(self._state_to_kind(current_state), munched_input)
                        )
                    # reset default
                    current_state = JSONDFA.State.START
                    munched_input = ""
                else:  # current state is not accepting, input is invalid
                    raise ValueError(f"Unable to scan and tokenise input: {input}")
            else:  # exists a transition
                munched_input += c
                current_state = next_state
                i += 1
        if current_state in JSONDFA._accepting_states:
            tokens.append(Token(self._state_to_kind(current_state), munched_input))
        else:
            raise ValueError(f"Unable to scan and tokenise input: {input}")
        return tokens

    def _state_to_kind(self, state: "JSONDFA.State") -> Token.Kind:
        match state:
            case JSONDFA.State.LBRACE:
                return Token.Kind.LBRACE
            case JSONDFA.State.RBRACE:
                return Token.Kind.RBRACE
            case JSONDFA.State.LSQUARE:
                return Token.Kind.LSQUARE
            case JSONDFA.State.RSQUARE:
                return Token.Kind.RSQUARE
            case JSONDFA.State.CLOSE_QUOTE:
                return Token.Kind.STRING
            case JSONDFA.State.COLON:
                return Token.Kind.COLON
            case JSONDFA.State.COMMA:
                return Token.Kind.COMMA
            case JSONDFA.State.MINUS:
                return Token.Kind.MINUS
            case JSONDFA.State.NUM:
                return Token.Kind.NUM
            case JSONDFA.State.ID:
                return Token.Kind.ID
            case JSONDFA.State.WHITESPACE:
                return Token.Kind.WHITESPACE
            case _:
                raise ValueError(f"Invalid accepting state: {state}")

    def _fill_accepting_states(self) -> None:
        JSONDFA._accepting_states = {
            JSONDFA.State.LBRACE,
            JSONDFA.State.RBRACE,
            JSONDFA.State.LSQUARE,
            JSONDFA.State.RSQUARE,
            JSONDFA.State.CLOSE_QUOTE,
            JSONDFA.State.COLON,
            JSONDFA.State.COMMA,
            JSONDFA.State.MINUS,
            JSONDFA.State.NUM,
            JSONDFA.State.ID,
            JSONDFA.State.WHITESPACE,
        }

    def _register_transition(
        self, state: "JSONDFA.State", input: str, next_state: "JSONDFA.State"
    ) -> None:
        for c in input:
            JSONDFA._transitions[state][ord(c)] = next_state

    def _register_transitions(
        self,
        state: "JSONDFA.State",
        input: Callable[[int], bool],
        next_state: "JSONDFA.State",
    ) -> None:
        for i in range(JSONDFA._NUM_ASCII_CHARS):
            if input(i):
                JSONDFA._transitions[state][i] = next_state


test = JSONDFA()
