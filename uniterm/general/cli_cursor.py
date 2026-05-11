import sys

def hide_CLI_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_CLI_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()