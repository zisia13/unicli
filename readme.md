# uniterm

## Installation

```bash
pip install uniterm
```
## important for windows
```bash
pip install windows-curses
```

## Modules
```python
from uniterm import (
    Selector,
    BannerPainter,
    SelectScreen
)
```

### `Selector` — selection request

Interactive choice with arrow keys or **W**/**S**, confirm with **Enter**.

```python
texts = Selector.Texts(
    question = "Select something:",
    choices = ("Option 1", "Option 2", "Option 3")
)
choice = Selector.select(texts)
print(f"Selected: {choice}")
```

### `BannerPainter` - gradients for ASCII banners

Color multi-line text with RGB gradients:

```python
raw = """"""
raw += """-----------------------------------------------"""
raw += """                  Projectname                  """
raw += """-----------------------------------------------"""
start_color = (255, 0, 0)
end_color = (0, 255, 0)
banner = BannerPainter.two_color_horizontal(
    text = raw,
    start_color = start_color,
    end_color = end_color
)
print(banner)
```

Additional static methods:

- `two_color_horizontal` / `two_color_vertical`
- `four_color_horizontal` / `four_color_vertical`


### `SelectScreen` - selection menu screen

Interactive choice menu with arrow keys or **W**/**S**, confirm with **Enter**/**e**.

```python
options = ["Option 1", "Option 2", "Option 3"]
select_screen = SelectScreen()
choice = select_screen.select_interface(
    message = "Select something:", 
    choices = options, 
    endless = True
)
print(f"Selected: {choice}")
```

### `progress_bar_1` - progress bar function
```python
for counter in range(100):
    progress_bar_1(
        counter + 1,
        "hello",
        100,
        100,
        10
    )
    time.sleep(0.05)
```

### `Logger` - A simple logger with log levels
```python
from uniterm.logger.logger import Levels
logger = Logger(
    name = "Test",
    show_time = True,
    log_info = True,
    log_level = Levels.Success
)
logger.Info("hello")
logger.Success("hello")
logger.Warning("hello")
logger.Error("hello")
```

## Local demos
```bash
python -m uniterm.select.select
python -m uniterm.banner.test
```

## License
See [`licence.md`](licence.md): **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International** (CC BY-NC-SA 4.0).

## Links
- Repository: [github.com/zisia13/uniterm](https://github.com/zisia13/uniterm)
- Banner Creator: n/a

## important for windows for SelectScreen
```bash
pip install windows-curses
```
