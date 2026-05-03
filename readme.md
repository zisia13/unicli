# uniterm

A small **CLI utility** library: interactive selection menus, colored ASCII banners, and ANSI truecolor — with **no runtime dependencies**.

**Status:** Alpha · **Python:** 3.9+

## Installation

```bash
pip install uniterm
```

Or from the repository in editable mode:

```bash
git clone https://github.com/zisia13/uniterm.git
cd uniterm
pip install -e .
```

## Modules

### `Selector` — terminal menu (Windows)

Interactive choice with arrow keys or **W**/**S**, confirm with **Enter**. Uses `msvcrt` and ANSI colors; the cursor is hidden while selecting.

```python
from uniterm import Selector

texts = Selector.Texts(
    question="Pick a package:",
    choices=("numpy", "requests", "rich", "exit"),
)
choice = Selector.select(texts)
print(f"Selected: {choice}")
```

Optional: custom colors (`Selector.Colors`) and key bindings (`Selector.Keybinds`).

**Note:** This menu targets **Windows** (`msvcrt`). It will not work as-is on Linux or macOS.

### `BannerPainter` — gradients for ASCII banners

Color multi-line text with RGB gradients (truecolor ANSI):

```python
from uniterm.banner import BannerPainter

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

## Build & publish

Local build:

```bash
pip install build
python -m build
```

On a **published GitHub Release**, the workflow [`.github/workflows/publish.yml`](.github/workflows/publish.yml) builds the package and publishes it to **PyPI** (trusted publishing).

## License

See [`licence.md`](licence.md): **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International** (CC BY-NC-SA 4.0).

## Links

- Repository: [github.com/zisia13/uniterm](https://github.com/zisia13/uniterm)
