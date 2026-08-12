from uniterm import (
    Selector,
    BannerPainter,
    SelectScreen,
    Logger,
    progress_bar_1,
    hide_CLI_cursor,
    show_CLI_cursor,
    Waiter,
    WaiterAnimations
)

def test_selector() -> None:
    Selector.DisableAutoUpdate()
    texts1 = Selector.Texts(
        question="What is your favorite color?",
        choices=("Blue", "Green", "Red", "Purple")
    )
    choice1 = Selector.select(texts1)
    
    texts2 = Selector.Texts(
        question="Choose a programming language:",
        choices=("Python", "Java", "C++", "Rust")
    )
    choice2 = Selector.select(texts2)
    
    texts3 = Selector.Texts(
        question="Select your operating system:",
        choices=("Windows", "Linux", "macOS", "Other")
    )
    choice3 = Selector.select(texts3)
    
    texts4 = Selector.Texts(
        question="Pick a drink:",
        choices=("Water", "Coffee", "Tea", "Juice")
    )
    choice4 = Selector.select(texts4)
    
    print("Results:")
    print(choice1)
    print(choice2)
    print(choice3)
    print(choice4)

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
    logger.Info("An info message.")
    logger.Success("A success message.")
    logger.Warning("A warning message.")
    logger.Error("An error message.")

def test_color_format_switcher() -> None:
    from uniterm import switch_color_format
    print(switch_color_format("#ffaa1b"))
    print(switch_color_format((255, 170, 27)))

def test_waiter() -> None:
    import sys
    import time

    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    for animation in WaiterAnimations.__all__:
        loader = Waiter.CharCycle(
            text = "Sleeping",
            chars = animation
        )
        loader.start()
        time.sleep(5)
        loader.stop()
        os.system("cls")

if __name__ == "__main__":
    import os; os.system("")
    from time import sleep

    test_selector()

    import sys; sys.exit()

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
    
    test_color_format_switcher()
    sleep(2)
    

    test_waiter()

    sleep(5)
    test_select_screen()

    

    input()
