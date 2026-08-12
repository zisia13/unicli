import os
import sys
import msvcrt
import re
from typing import Dict, TypeAlias

Word: TypeAlias = str # "Banana"
Color: TypeAlias = str # built color: "\033[38;2;245;200;75m"

class KeyBinds:
    Enter = ("\r", "\n")
    Backspace = ("\b", "\x08")
    SpecialArrow = ("\x00", "\xe0")
    CtrlC = ("\x03")

class LiveHighlightingInputWin:
    def __init__(self, colors: Dict[Word, Color], prompt: str = "-> "):
        self.reset = "\033[0m"
        self.prompt = prompt
        self.colors = colors

    def _colorize(self, text: str) -> str:
        def _replace(match: re.Match) -> str:
            word = match.group(0)
            color = self.colors.get(word)
            if color:
                return f"{color}{word}{self.reset}"
            return word
        return re.sub(r"[A-Za-zÄÖÜäöüß]+", _replace, text)

    def _redraw(self, buffer: str) -> None:
        sys.stdout.write(f"\r\033[K{self.prompt}{self._colorize(buffer)}") #! \033[K = clear rest of line
        sys.stdout.flush()

    def get_input(self) -> str:
        buffer = ""
        self._redraw(buffer)
    
        while True:
            char = msvcrt.getwch()
    
            if char in KeyBinds.Enter:
                sys.stdout.write("\n")
                break
    
            if char in KeyBinds.Backspace:
                if buffer:
                    buffer = buffer[:-1]
                    self._redraw(buffer)
                continue
    
            if char in KeyBinds.SpecialArrow:
                msvcrt.getwch()
                continue
    
            if char in KeyBinds.CtrlC:
                sys.stdout.write("\n")
                raise KeyboardInterrupt
    
            if char.isprintable(): #! normal char
                buffer += char
                self._redraw(buffer)

        return buffer



if __name__ == "__main__":
    try:

        test = {
            "Banana": "\033[38;2;245;200;75m",
            "Apple":  "\033[38;2;152;195;121m",
            "Lemon":  "\033[38;2;255;235;120m"
        }
        os.system("")
        lhi = LiveHighlightingInputWin(test)
        inp = lhi.get_input()
        print(inp)
    except KeyboardInterrupt:
        sys.exit()
