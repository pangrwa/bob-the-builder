from typing import Self, Any, List 
from stream_tracker import StreamTracker
import sys
import io

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
            st: StreamTracker = StreamTracker(sys.stdin.buffer)
            res += self._handle_stream(flags, st) + '\n'
        else:
            for file in files:
                try:
                    with open(file, mode='rb') as f:
                        st: StreamTracker = StreamTracker(f)
                        res += self._handle_stream(flags, st)
                    res += file + '\n'# adds the file name to the result
                except FileNotFoundError as e:
                    res += str(e) + '\n'

        # remove the last \n
        res = res[:-1]
        return res

    def _handle_stream(self, flags: List[str], stream: StreamTracker) -> str:
        res: str = ""
        for flag in flags:
            res += self._handle_flag(flag, stream) + " "
        return res

    def _handle_flag(self, flag: str, stream: StreamTracker) -> str:
        match flag: 
            case '-c':
                return str(stream.num_bytes)
            case '-l':
                return str(stream.num_lines)
            case '-w':
                return str(stream.num_words)
            case '-m':
                return str(stream.num_chars)
            case _: 
                return ""
                
            


        


