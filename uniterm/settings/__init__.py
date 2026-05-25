import os
import inspect
from pathlib import Path

DisableAutoUpdateFileName: str = ".uniterm_disable_update"

def get_caller_path():
    frame = inspect.stack()[2]
    caller_file = frame.filename
    return Path(caller_file).parent

def is_perma_disable_auto_update_file_present() -> bool:
    """
    Filename to disable autoupdate of lib permanently: ".uniterm_disable_update"
    """
    caller_path = get_caller_path()
    for filename in os.listdir(caller_path):
        if filename == DisableAutoUpdateFileName:
            return True
    return False
