import sys
import io

class StreamTracker:


    def __init__(self, buffered_reader: io.BufferedReader) -> None:
        self.buffered_reader: io.BufferedReader = buffered_reader
        self.num_bytes: int = 0
        self.num_words: int = 0
        self.num_lines: int = 0
        self.num_chars: int = 0
        self._calculate_details()
    
    # could throw a FileNotFoundException
    def _calculate_details(self) -> None:
        for line in self.buffered_reader:
            self.num_lines += 1
            self.num_words += len(line.split())
            self.num_bytes += len(line)
            self.num_chars += len(line.decode())
