import time, sys
from typing import TypeAlias

ColorString: TypeAlias = str

def _b(r: int, g: int, b: int):
    return f"\033[38;2;{r};{g};{b}m"

class _c:
    WHITE = _b(255, 255, 255)
    BLACK = _b(0, 0, 0)
    GRAY = _b(128, 128, 128)
        
    RED = _b(255, 0, 0)
    GREEN = _b(0, 255, 0)
    BLUE = _b(0, 0, 255)
        
    YELLOW = _b(255, 255, 0)
    CYAN = _b(0, 255, 255)
    MAGENTA = _b(255, 0, 255)

    ORANGE = _b(255, 165, 0)
    PURPLE = _b(128, 0, 128)
    PINK = _b(255, 192, 203)
    LIME = _b(0, 255, 0)
    OLIVE = _b(128, 128, 0)
    NAVY = _b(0, 0, 128)

    PASTELL_GREEN = _b(144, 238, 144)
    PASTELL_RED = _b(255, 114, 118)
        
    _theme_color = _b(155, 220, 33)
    _reset = _b(255, 255, 255)
    
def progress_bar_1(
        current: str,
        current_name: str,
        total: int,
        width: int,
        longest_name: int,

        finished_color: ColorString = _c.PASTELL_GREEN,
        unfinished_color: ColorString = _c.PASTELL_RED,
        current_item_name_color: ColorString = _c._theme_color,
        reset: ColorString = _c._reset
    ):

    PROGRESSBAR_ASCII_COMPLETE = finished_color + "━" + reset #"█"
    PROGRESSBAR_ASCII_FINISHED = unfinished_color + "━" + reset
    theme_color = current_item_name_color
    
    if len(str(current_name)) < longest_name:
        diff = longest_name - len(str(current_name))
        current_name = str(current_name) + str(" " * diff)

    i = total - (total - current)
    percent = i / total
    filled = int(width * percent)
    if int(current) == int(total):
        space = ""
    else:
        space = " "

    bar = PROGRESSBAR_ASCII_COMPLETE * filled + space + PROGRESSBAR_ASCII_FINISHED * (width - filled)

    sys.stdout.write(f'\r[{bar}] {current}/{total} {percent * 100:.1f}% File: {theme_color}{current_name}{_c._reset}')
    sys.stdout.flush()
    sys.stdout.write("\033[A")
    time.sleep(0.01)



if __name__ == "__main__":
    for counter in range(100):
        progress_bar_1(
            counter + 1,
            "hello",
            100,
            100,
            10
        )
        time.sleep(0.05)
