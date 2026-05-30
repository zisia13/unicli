import os
import msvcrt
from dataclasses import dataclass
from typing import Sequence, Tuple, Optional

from ..update import ClassAutoupdateable, classautoupdatecheck

ANSI_RESET = "\033[0m"
ANSI_BOLD = "\033[1m"

class Selector(ClassAutoupdateable):
    _autoupdate = True

    @classmethod
    def DisableAutoUpdate(cls) -> None:
        cls._autoupdate = False
    
    @dataclass(frozen = True)
    class Actions:
        up: str = "up"
        down: str = "down"
        enter: str = "enter"
        other: str = "other"

    @dataclass(frozen = False)
    class Colors:
        question: str = "\033[38;5;111m"   # soft blue
        pointer: str = "\033[38;5;219m"    # pink/magenta
        choice: str = "\033[38;5;252m"     # hellgrau
        selected_choice: str = "\033[38;5;120m"  # soft green

        @staticmethod
        def build_single_values(r: int, g: int, b: int) -> str:
            return f"\033[38;2;{r};{g};{b}m"

        @staticmethod
        def build_tuple(color_tuple: Tuple[int, int, int]) -> str:
            return f"\033[38;2;{color_tuple[0]};{color_tuple[1]};{color_tuple[2]}m"

    class Texts:
        def __init__(self, question: str, choices: Sequence[str], pointer: str = ">"):
            self.question = question
            self.choices = choices
            self.pointer = pointer

    @dataclass(frozen = False)
    class Keybinds:
        up_chars: Sequence[bytes] = (b"w", b"W")
        down_chars: Sequence[bytes] = (b"s", b"S")
        enter_chars: Sequence[bytes] = (b"\r", b"\n")
        arrow_prefix_chars: Sequence[bytes] = (b"\x00", b"\xe0")
        up_arrow_char: bytes = b"H"
        down_arrow_char: bytes = b"P"

    @staticmethod
    def _enable_ansi_on_windows() -> None:
        os.system("")

    @staticmethod
    def _read_key(keybinds: Keybinds) -> str:
        actions = Selector.Actions()
        key = msvcrt.getch()

        if key in keybinds.arrow_prefix_chars:
            special = msvcrt.getch()
            if special == keybinds.up_arrow_char:
                return actions.up
            if special == keybinds.down_arrow_char:
                return actions.down
            return actions.other

        if key in keybinds.enter_chars:
            return actions.enter

        if key in keybinds.up_chars:
            return actions.up
        if key in keybinds.down_chars:
            return actions.down

        return actions.other

    @staticmethod
    def _render_menu(texts: Texts, colors: Colors, selected_index: int) -> None:
        print(f"{colors.question}{ANSI_BOLD}{texts.question}{ANSI_RESET}")
        for index, choice in enumerate(texts.choices):
            is_selected = index == selected_index
            if is_selected:
                print(
                    f"{colors.pointer}{texts.pointer}{ANSI_RESET} "
                    f"{colors.selected_choice}{choice}{ANSI_RESET}"
                )
            else:
                prespace = (len(texts.pointer) + 1) * " "
                print(f"{prespace}{colors.choice}{choice}{ANSI_RESET}")

    @classmethod
    @classautoupdatecheck
    def select(
        cls,
        texts: Texts,
        colors: Optional[Colors] = None,
        keybinds: Optional[Keybinds] = None,
    ) -> str:
        texts.choices = list(texts.choices) # cant change values in tuple for spaces so convert to list

        if not texts.choices:
            raise ValueError("choices must not be empty.")

        if keybinds is None:
            keybinds = cls.Keybinds()
        if colors is None:
            colors = cls.Colors()
        if colors.pointer is None:
            colors.pointer = ">"

        actions = cls.Actions()

        cls._enable_ansi_on_windows()
        selected_index = 0
        line_count = len(texts.choices) + 1

        # calc longest choice for formatting reasons
        longest_option: int = 0
        for choice in texts.choices:
            if len(choice) > longest_option:
                longest_option = len(choice)
        longest_option += len(texts.pointer)

        # add spaces to every choice and strip them later when returning value
        for counter, choice in enumerate(texts.choices):
            if longest_option > len(choice):
                diff = longest_option - len(choice)
                texts.choices[counter] = choice + diff * " "

        print("\033[?25l", end = "")
        try:
            while True:
                cls._render_menu(texts, colors, selected_index)
                key = cls._read_key(keybinds)

                if key == actions.up:
                    selected_index = (selected_index - 1) % len(texts.choices)
                elif key == actions.down:
                    selected_index = (selected_index + 1) % len(texts.choices)
                elif key == actions.enter:
                    print("\033[?25h", end = "")
                    return texts.choices[selected_index].strip() # stip to remove the added spaces from before

                # Move cursor to menu start and redraw.
                print(f"\033[{line_count}F", end = "")
        finally:
            print("\033[?25h", end = "")


if __name__ == "__main__":

    demo_texts = Selector.Texts(
        question = "Is this a test question?",
        choices = ("numpy", "requests", "rich", "exit")
    )
    demo_colors = Selector.Colors()

    selected = Selector.select(demo_texts, demo_colors)
    print(f"\nSelected: {selected}")
