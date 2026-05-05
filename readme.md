# uniterm


## Installation

```bash
pip install uniterm
```

## Modules

### `Selector` — terminal menu (Windows)

Interactive choice with arrow keys or **W**/**S**, confirm with **Enter**.

```python
from uniterm import Selector

texts = Selector.Texts(
    question="Pick a package:",
    choices=("numpy", "requests", "rich", "exit"),
)
choice = Selector.select(texts)
print(f"Selected: {choice}")
```

**Note:** This menu targets **Windows** (`msvcrt`). It will not work as-is on Linux or macOS.

### `BannerPainter` - gradients for ASCII banners

Color multi-line text with RGB gradients:

```python
from uniterm import BannerPainter

banner = r"""
  __  __       _       _
 |  \/  |_   _| |_ __ | | ___ _ __
 | |\/| | | | | __/ _` | |/ _ \ '__|
 | |  | | |_| | || (_| | |  __/ |
 |_|  |_|\__,_|\__\__,_|_|\___|_|
"""

print(BannerPainter.two_color_horizontal(banner, (60, 90, 200), (180, 80, 200)) + BannerPainter.reset)
```

Additional static methods:

- `two_color_horizontal` / `two_color_vertical`
- `four_color_horizontal` / `four_color_vertical`

Repo demo: `python -m uniterm.banner.test` (after install, or with `PYTHONPATH` set).

## Local demos

```bash
python -m uniterm.select.select   # interactive menu
python -m uniterm.banner.test     # banner samples
```

## License

See [`licence.md`](licence.md): **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International** (CC BY-NC-SA 4.0).

## Links

- Repository: [github.com/zisia13/uniterm](https://github.com/zisia13/uniterm)
