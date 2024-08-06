from json_dfa import JSONDFA
from json_parser import JSONParser
from my_token import Token
from typing import List
import sys
import io


def scan(buffered_reader: io.TextIOWrapper) -> List[Token]:
    json_dfa = JSONDFA()
    all_tokens = []
    for line in buffered_reader:
        tokens = json_dfa.tokenise(line)
        new_tokens = []
        for token in tokens:
            if token.get_kind() == Token.Kind.WHITESPACE:
                continue
            new_tokens.append(token)
        all_tokens.extend(new_tokens)
    return all_tokens


def parse(tokens: List[Token]) -> None:
    json_parser = JSONParser(tokens)


def main():
    args = sys.argv[1:]
    # lets just handle for 1 file for now
    tokens: List[Token] = []
    if len(args) > 0:
        try:
            with open(args[0], "r") as file:
                buffered_reader = file
                tokens = scan(buffered_reader)
        except FileNotFoundError as e:
            print(e)
    else:
        buffered_reader = sys.stdin.buffer
        tokens = scan(buffered_reader)

    parse(tokens)


if __name__ == "__main__":
    main()
