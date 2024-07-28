from json_dfa import JSONDFA
from json_parser import JSONParser
from my_token import Token
import sys
import io


json_dfa = JSONDFA()
json_parser = JSONParser()


def scan(buffered_reader: io.TextIOWrapper) -> None:
    for line in buffered_reader:
        tokens = json_dfa.tokenise(line)
        new_tokens = []
        for token in tokens:
            if token.get_kind() == Token.Kind.WHITESPACE:
                continue
            new_tokens.append(token)
        for t in new_tokens:
            print(t)


def main():
    args = sys.argv[1:]
    # lets just handle for 1 file for now
    if len(args) > 0:
        try:
            with open(args[0], "r") as file:
                buffered_reader = file
                scan(buffered_reader)
        except FileNotFoundError as e:
            print(e)
    else:
        buffered_reader = sys.stdin.buffer
        scan(buffered_reader)


if __name__ == "__main__":
    main()
