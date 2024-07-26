import sys 
from typing import List
from pywc import PYWC

def is_flag(arg: str) -> bool:
    return arg[0] == '-'

def main():
    args: List[str] = sys.argv[1:]
    # remove the executable path
    flags: List[str] = []
    files: List[str] = []

    for arg in args: 
        if is_flag(arg):
            flags.append(arg)
        else: 
            files.append(arg)

    pywc = PYWC()
    print(pywc.handle_command(flags, files))


if __name__ == "__main__":
    main()
    
