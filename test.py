from uniterm import (
    Selector,
    BannerPainter,
    SelectScreen,
    Logger,
    progress_bar_1,
    hide_CLI_cursor,
    show_CLI_cursor
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
    BannerPainter.DisableAutoUpdate()
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

def test_logger() -> None:
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

if __name__ == "__main__":
    from time import sleep

    test_selector()

    test_banner_painter()

    for counter in range(100):
        progress_bar_1(
            current = counter + 1,
            current_name = "hello",
            total = 100,
            width = 100,
            longest_name = 10
        )
        sleep(0.05)

    hide_CLI_cursor()
    sleep(1)
    show_CLI_cursor()
    sleep(1)

    test_logger()
    sleep(1)
    
    test_select_screen()
