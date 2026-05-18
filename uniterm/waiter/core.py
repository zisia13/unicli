import threading
import itertools
import time
import sys
from typing import List

class Waiter:
    class CharCycle:
        def __init__(
                self,
                text: str = "Please wait",
                chars: List[str] = ["|", "/", "-", "\\"],
                speed: int = 1
            ):
            self.text = text
            self._running = False
            self._thread = None
            self.spinner = itertools.cycle(chars)
            self.speed = speed

        def _animate(self):
            while self._running:
                sys.stdout.write(f"\r{self.text} {next(self.spinner)}")
                sys.stdout.flush()
                time.sleep(self.speed / 10)

            sys.stdout.write("\r" + " " * (len(self.text) + 4) + "\r")
            sys.stdout.flush()

        def start(self):
            if not self._running:
                self._running = True
                self._thread = threading.Thread(target = self._animate)
                self._thread.daemon = True
                self._thread.start()

        def stop(self):
            self._running = False
            if self._thread:
                self._thread.join()



if __name__ == "__main__":
    from time import sleep
    from animations import Animations
    import os
    import sys

    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    for animation in Animations.__all__:
        loader = Waiter.CharCycle(
            text = "Sleeping",
            chars = animation
        )
        loader.start()
        time.sleep(5)
        loader.stop()
        os.system("cls")
