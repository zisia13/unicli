# this file is fully vibecoded

from __future__ import annotations

import ctypes
import re
import shutil
import sys
import threading
import time


class CarouselAnimation:
    """
    ```python
    carousel = CarouselAnimation(XXX)
    carousel.start()
    do_something()
    carousel.stop(clear = False)
    ```
    """

    ANSI_RE: re.Pattern[str] = re.compile(r"\033\[[0-?]*[ -/]*[@-~]")

    def __init__(
        self,
        words: list[str],
        band_length: int = 40,
        delay: float = 0.12,
        separator: str = "   ",
    ) -> None:
        if not words:
            raise ValueError("words must contain at least one string")
        if band_length < 1:
            raise ValueError("band_length must be at least 1")

        self.words: list[str] = words
        self.band_length: int = band_length
        self.delay: float = delay
        self.separator: str = separator
        self._tape: str = self.separator.join(self.words) + self.separator
        self._visible_tape_length: int = self._visible_length(self._tape)
        if self._visible_tape_length < 1:
            raise ValueError("words must contain at least one visible character")

        self._stop_event: threading.Event = threading.Event()
        self._lock: threading.RLock = threading.RLock()
        self._thread: threading.Thread | None = None
        self._row: int | None = None
        self._terminal_height: int | None = None
        self._terminal_width: int | None = None

    def start(self) -> None:
        with self._lock:
            if self._thread and self._thread.is_alive():
                return

            self._enable_windows_ansi()
            size = shutil.get_terminal_size(fallback = (80, 24))
            self._terminal_width = size.columns
            self._terminal_height = size.lines
            self._row = self._terminal_height - 1
            self._stop_event.clear()

            self._hide_cursor()
            self._thread = threading.Thread(target = self._run, daemon = True)
            self._thread.start()

    def stop(self, clear: bool = True) -> None:
        self._stop_event.set()
        if self._thread:
            self._thread.join(timeout = 1.0)

        with self._lock:
            if clear and self._is_visible():
                self._clear_animation_line()
            self._show_cursor()
            sys.stdout.flush()

    @property
    def is_running(self) -> bool:
        return bool(self._thread and self._thread.is_alive())

    def println(self, text: str = "") -> None:
        with self._lock:
            if not self.is_running:
                print(text)
                return

            if self._is_visible():
                self._clear_animation_line()

            assert self._terminal_height is not None
            self._move_cursor(self._terminal_height, 1)
            sys.stdout.write(text + "\n")
            sys.stdout.flush()

            assert self._row is not None
            self._row -= self._count_terminal_rows(text)
            if self._row < 0:
                self._stop_event.set()

    def _run(self) -> None:
        frame: int = 0

        while not self._stop_event.is_set():
            with self._lock:
                if not self._is_visible():
                    self._stop_event.set()
                    break

                offset = frame % self._visible_tape_length
                self._render(self._band_window(offset))

            frame += 1
            time.sleep(self.delay)

        with self._lock:
            self._show_cursor()
            sys.stdout.flush()

    def _render(self, text: str) -> None:
        assert self._row is not None
        sys.stdout.write("\033[s")
        self._move_cursor(self._row + 1, 1)
        sys.stdout.write("\033[2K")
        sys.stdout.write(text)
        sys.stdout.write("\033[0m")
        sys.stdout.write("\033[u")
        sys.stdout.flush()

    def _clear_animation_line(self) -> None:
        assert self._row is not None
        sys.stdout.write("\033[s")
        self._move_cursor(self._row + 1, 1)
        sys.stdout.write("\033[2K")
        sys.stdout.write("\033[u")

    def _is_visible(self) -> bool:
        return (
            self._row is not None
            and self._terminal_height is not None
            and 0 <= self._row < self._terminal_height
        )

    def _count_terminal_rows(self, text: str) -> int:
        assert self._terminal_width is not None
        width = max(1, self._terminal_width)
        lines: list[str] = text.splitlines() or [""]
        rows: int = 0

        for line in lines:
            line_length = self._visible_length(line)
            rows += max(1, (line_length + width - 1) // width)

        return rows

    def _band_window(self, offset: int) -> str:
        assert self._terminal_width is not None
        visible_width: int = min(self.band_length, max(1, self._terminal_width - 1))
        repeats: int = ((offset + visible_width) // self._visible_tape_length) + 2
        repeated_tape: str = self._tape * repeats
        return self._ansi_visible_slice(repeated_tape, offset, visible_width)

    def _ansi_visible_slice(self, text: str, start: int, length: int) -> str:
        result: list[str] = []
        visible_index: int = 0
        visible_written: int = 0
        active_sgr: list[str] = []
        index: int = 0

        while index < len(text) and visible_written < length:
            match = self.ANSI_RE.match(text, index)

            if match:
                sequence = match.group(0)
                active_sgr = self._update_active_sgr(active_sgr, sequence)

                if visible_index >= start:
                    result.append(sequence)

                index = match.end()
                continue

            char = text[index]

            if visible_index >= start:
                if visible_written == 0 and active_sgr:
                    result.extend(active_sgr)

                result.append(char)
                visible_written += 1

            visible_index += 1
            index += 1

        if visible_written < length:
            result.append(" " * (length - visible_written))

        return "".join(result)

    def _update_active_sgr(self, active_sgr: list[str], sequence: str) -> list[str]:
        if not sequence.endswith("m"):
            return active_sgr

        if sequence in ("\033[m", "\033[0m"):
            return []

        return active_sgr + [sequence]

    def _visible_length(self, text: str) -> int:
        return len(self.ANSI_RE.sub("", text))

    def _move_cursor(self, row: int, column: int) -> None:
        sys.stdout.write(f"\033[{row};{column}H")

    def _hide_cursor(self) -> None:
        sys.stdout.write("\033[?25l")

    def _show_cursor(self) -> None:
        sys.stdout.write("\033[?25h")

    def _enable_windows_ansi(self) -> None:
        if sys.platform != "win32":
            return

        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)
        mode = ctypes.c_uint32()

        if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            kernel32.SetConsoleMode(handle, mode.value | 0x0004)


if __name__ == "__main__":
    carousel = CarouselAnimation(
        [
            "\033[1;38;5;81mMIDNIGHT DROP\033[0m",
            "\033[1;38;5;219mSOFT NEON DEALS\033[0m",
            "\033[1;38;5;228mLIMITED EDITION\033[0m",
            "\033[1;38;5;120mFREE SHIPPING\033[0m",
        ],
        band_length = 64,
        delay = 0.07,
        separator = "\033[38;5;245m  *  \033[0m",
    )

    carousel.start()

    try:
        for i in range(8):
            time.sleep(1.6)
            carousel.println(f"Log line {i + 1}")

            if not carousel.is_running:
                break
    finally:
        carousel.stop(clear = False)

    print("Carousel is no longer visible and has stopped.")
