from typing import TypeAlias, Optional, List, Callable
from datetime import datetime
from dataclasses import dataclass

LevelType: TypeAlias = str
ColorType: TypeAlias = str # #xxxxxx
ColorVal: TypeAlias = int # 0-255

def b(r: ColorVal, g: ColorVal, b: ColorVal) -> ColorType:
    for c in (r, g, b):
        if not 0 <= c <= 255:
            raise ValueError("RGB values must be between 0 and 255!")
    return f"\033[38;2;{r};{g};{b}m"

_reset: ColorType = b(255, 255, 255)

@dataclass
class Colors:
    Info: ColorType
    Success: ColorType
    Warning: ColorType
    Error: ColorType

class Default:
    Info_Color: ColorType = b(100, 180, 255)
    Success_Color: ColorType = b(120, 220, 140)
    Warning_Color: ColorType = b(255, 200, 90)
    Error_Color: ColorType = b(255, 110, 110)

_levels = [_level for _level in Colors.__match_args__]
_max_width = max(len(_level) for _level in _levels)
class Levels:
    Info = ...
    Success = ...
    Warning = ...
    Error = ...
for value in _levels:
    setattr(Levels, value, value.ljust(_max_width))
del _levels
del _max_width

class Separators:
    def square_brackets(t: str) -> str:
        return f"{_reset}[{t}{_reset}]"
    
    def line(t: str):
        return f"{_reset}{t}{_reset} | "

class Logs:
    def __init__(self):
        self.logs: List[str] = []
        self.working: bool = False

    def collect(self) -> List[str]:
        temp_logs = self.logs
        self.logs = []
        return temp_logs

    def add(self, log: str) -> bool:
        if self.working:
            self.logs.append(log)
            return True
        else:
            return False

    def start(self) -> None:
        self.working = True

    def stop(self) -> None:
        self.working = False

class Logger:
    _instances = {}

    @classmethod
    def create(cls, name: str, **kwargs):
        logger = cls(name = name, **kwargs)
        cls._instances[name] = logger
        return logger
    
    @classmethod
    def get(cls, name: str):
        return cls._instances[name]

    def __init__(   
            self,
            info_color: ColorType = Default.Info_Color,
            success_color: ColorType = Default.Success_Color,
            warning_color: ColorType = Default.Warning_Color,
            error_color: ColorType = Default.Error_Color,

            name: Optional[str] = None, # extra [] field at start of string for name, Example: [Simple Logger][00:00:00][n]
            show_time: bool = True,
            log_level: LevelType = Levels.Success,
            log_info: bool = True,
            separator: Callable = Separators.line
        ):

        self.colors = Colors(
            Info = info_color,
            Success = success_color,
            Warning = warning_color,
            Error = error_color
        )

        self.show_time = show_time
        self.name = name
        self.log_level = log_level
        self.log_info = log_info

        self.separator = separator
        self.logs = Logs()


    def _get_time(self) -> str:
        return datetime.now().strftime("%H:%M:%S")
    
    def _level_to_color(self, level: LevelType) -> ColorType:
        match level:
            case Levels.Info:
                return self.colors.Info
            case Levels.Success:
                return self.colors.Success
            case Levels.Warning:
                return self.colors.Warning
            case Levels.Error:
                return self.colors.Error
            case _:
                raise ValueError(f"uniterm/logger/{self._level_to_color.__name__}/case _:, No matching color to level.")

    def _print(self, msg: str, level: LevelType) -> None:
        if (level == Levels.Info) and (self.log_info == False): return None # check info logs only/separate
        if (self.log_level == Levels.Warning) and (level not in [Levels.Info, Levels.Warning, Levels.Error]): return None # if log level set to "Levels.Warning"
        if (self.log_level == Levels.Error) and (level not in [Levels.Info, Levels.Error]): return None # if log level set to "Levels.Error"

        outstr = ""
        outstr += self.separator(self.name) if not self.name in ["", None] else ""
        outstr += self.separator(self._get_time()) if self.show_time else ""
        outstr += self.separator(self._level_to_color(level) + str(level))
        outstr += f"{msg}"
        print(outstr)

        try: self.logs.add(
            {   
                "outstr" : str(outstr),
                "msg" : str(msg),
                "level" : str(level),
                "time" : str(self._get_time())
            }
        )
        except: pass
    
    def Info(self, msg: str) -> None:
        self._print(msg, Levels.Info)

    def Success(self, msg: str) -> None:
        self._print(msg, Levels.Success)

    def Warning(self, msg: str) -> None:
        self._print(msg, Levels.Warning)

    def Error(self, msg: str) -> None:
        self._print(msg, Levels.Error)



if __name__ == "__main__":
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
    test_logger = Logger.create("test")
    test_logger.Info("This is a text")
