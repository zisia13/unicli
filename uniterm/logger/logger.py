from typing import TypeAlias, Optional
from datetime import datetime
from dataclasses import dataclass

LevelType: TypeAlias = int
ColorType: TypeAlias = str
ColorVal: TypeAlias = int

def b(r: ColorVal, g: ColorVal, b: ColorVal) -> ColorType:
    return f"\033[38;2;{r};{g};{b}m"

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

class Levels():
    Info = "Info"
    Success = "Success"
    Warning = "Warning"
    Error = "Error"

class Logger:
    def __init__(
            self,
            info_color: ColorType = Default.Info_Color,
            success_color: ColorType = Default.Success_Color,
            warning_color: ColorType = Default.Warning_Color,
            error_color: ColorType = Default.Error_Color,

            name: Optional[str] = None, # extra [] field at start of string for name, Example: [Simple Logger][00:00:00][n]
            show_time: bool = True,
            log_level: LevelType = Levels.Success,
            log_info: bool = True
        ):

        self.colors = Colors(
            Info = info_color,
            Success = success_color,
            Warning = warning_color,
            Error = error_color
        )

        self.reset: ColorType = b(255, 255, 255)

        self.show_time = show_time
        self.name = name
        self.log_level = log_level
        self.log_info = log_info

    def _get_time(self) -> str:
        return datetime.now().strftime("%H:%M:%S")
    
    def _asb(self, f: str) -> str: # "add square brackets"
        return f"{self.reset}[{f}{self.reset}]"
    
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
        outstr += self._asb(self.name) if not self.name in ["", None] else ""
        outstr += self._asb(self._get_time()) if self.show_time else ""
        outstr += self._asb(self._level_to_color(level) + str(level))
        outstr += f": {msg}"
        print(outstr)
    
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
