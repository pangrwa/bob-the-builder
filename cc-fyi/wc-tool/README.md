# pywc
This a command used in a terminal to count the number of words, lines, character and bytes from a buffered reader.
This includes files and anything that is given to the standard input. 

## Installation
1. The python version that I used is `3.12.3`
2. Follow the steps below
```[bash]
# install virtual environment
python3 -m venv venv

# activate it
source venv/bin/activate

# install the "package" created
python3 -m pip install --editable .

# Follow what the features has been provided for pywc

# when you're done deactivte environment
deactivate
```

## Features

Flags:
- `-c`: counts the number of bytes
- `-l`: counts the number of lines
- `-w`: counts the number of words
- `-m`: counts the number of characters

Examples:
```[bash]
> pywc -c test.txt
342190 test.txt

# no flags given: lines , words, characters
> pywc test.txt
7145   58164  342190 test.txt

# using standard output
> cat test.txt | pywc -l
7145
# press ctr-d to signal EOF if you're interacting with the terminal to type in standard input

# multiple files
❯ pywc test.txt src/stream_tracker.py
342190 7145 58164 test.txt
641 21 58 src/stream_tracker.py

# invalid file
❯ pywc test.txt a.txt
342190 7145 58164 test.txt
[Errno 2] No such file or directory: 'a.txt'
```
