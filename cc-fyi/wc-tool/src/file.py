class File:

    def __init__(self, file_name: str):
        self.file_name: str = file_name
        self.num_bytes: int = 0
        self.num_words: int = 0
        self.num_lines: int = 0
        self.num_chars: int = 0
        self._calculate_details()
    
    # could throw a FileNotFoundException
    def _calculate_details(self) -> None:
        with open(self.file_name, mode='rb') as f:
           for line in f:
               self.num_lines += 1
               self.num_words += len(line.split())
               self.num_bytes += len(line)
               self.num_chars += len(line.decode())

