from uniterm import (
    Selector,
    BannerPainter,
    SelectScreen
)

def test_selector() -> None:
    Selector.DisableAutoUpdate()
    texts = Selector.Texts(
        question = "Select something:",
        choices = ("Option 1", "Option 2", "Option 3")
    )
    choice = Selector.select(texts)
    print(f"Selected: {choice}")

def test_banner_painter() -> None:
    raw = """-----------------------------------------------"""
    start_color = (255, 0, 0)
    end_color = (0, 255, 0)
    BannerPainter.DisableAutoUpdate()
    banner = BannerPainter.two_color_horizontal(
        text = raw,
        start_color = start_color,
        end_color = end_color
    )
    print(banner)

def test_select_screen() -> None:
    options = ["Option 1", "Option 2", "Option 3"]
    select_screen = SelectScreen()
    select_screen.DisableAutoUpdate()

    choice = select_screen.select_interface(
        message = "Select something:", 
        choices = options, 
        endless = True
    )
    print(f"Selected: {choice}")

if __name__ == "__main__":
    from time import sleep

    test_selector()
    sleep(4)

    test_banner_painter()
    sleep(4)

    test_select_screen()
    sleep(4)
