from typing import Self, Any, List 
from file import File
import sys

class PYWC:
    # Singleton
    _instance: Self = None

    def __new__(cls: type[Self], *args: Any, **kwargs: Any) -> Self:
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


    def handle_command(self, flags: List[str], files: List[str]) -> str:
        if len(flags) == 0:
           flags = ['-c', '-l', '-w']
        res: str = ""
        if len(files) == 0:
            self._handle_input(flags)
            return 
        for file in files:
            try:  
                f: File = File(file)
                res += self._handle_file(flags, f) + '\n'
            except FileNotFoundError as e:
                res += str(e) + '\n'

        # remove the last \n
        res = res[:-1]
        return res

    # todo
    def _handle_input(self, flags: List[str]):
        pass

    def _handle_file(self, flags: List[str], file: File) -> str:
        res: str = ""
        for flag in flags:
            res += self._handle_flag(flag, file) + " "
        res += file.file_name
        return res

    def _handle_flag(self, flag: str, file: File) -> str:
        match flag: 
            case '-c':
                return str(file.num_bytes)
            case '-l':
                return str(file.num_lines)
            case '-w':
                return str(file.num_words)
            case '-m':
                return str(file.num_chars)
            case _: 
                return ""
                
            


        


