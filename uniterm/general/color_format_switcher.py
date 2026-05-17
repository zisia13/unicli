from typing import Union, Tuple, TypeAlias

ColorHex: TypeAlias = str # "#xxxxxx"
ColorTuple: TypeAlias = Tuple[int, int, int] # (xx, xx, xx)
ColorStringLength: int = 7
ColorTupleLength: int = 3

HEX_TABLE = {
    "0" : 0,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "A" : 10,
    "B" : 11,
    "C" : 12,
    "D" : 13,
    "E" : 14,
    "F" : 15
}

def _str_to_nr(char: str) -> int:
    is_number: bool = None
    try:
        _ = int(char)
        is_number = True
    except:
        is_number = False

    if is_number:
        return HEX_TABLE[char]
    else:
        try:
            return HEX_TABLE[char.upper()]
        except:
            return HEX_TABLE[char]

def _nr_to_str(nr: int) -> str:
    for char in HEX_TABLE:
        if HEX_TABLE[char] == nr:
            return char

def switch_color_format(color: Union[ColorHex, ColorTuple]) -> Union[ColorHex, ColorTuple]:
    if isinstance(color, str):
        if color[0] != "#":
            raise ValueError("Fist letter of color string must be: #")

        for char in color.replace("#", ""):
            if not char in HEX_TABLE:
                try:
                    if not char.upper() in HEX_TABLE:
                        raise ValueError(f"Letter {char} is not allowed for color strings")
                    else:
                        continue
                except:
                    pass

                raise ValueError(f"Letter {char} is not allowed for color strings")
            
        if len(color) != ColorStringLength:
            raise ValueError(f"Length of string must be {ColorStringLength}")

        r = _str_to_nr(color[1]) * 16 + _str_to_nr(color[2]) * 1
        g = _str_to_nr(color[3]) * 16 + _str_to_nr(color[4]) * 1
        b = _str_to_nr(color[5]) * 16 + _str_to_nr(color[6]) * 1

        return (r, g, b)
        
    elif isinstance(color, tuple):
        if len(color) != ColorTupleLength:
            raise ValueError(f"Length of ColorTuple must be: {ColorTupleLength}")
        
        for c in color:
            if not isinstance(c, int):
                raise ValueError(f"Type of color in ColorTuple must be int not: {type(c)}")
            
        colorstr = ""
        colorstr += "#"
        for c in color:
            num = int(c)
            first_int = num // 16
            second_int = num % 16
            colorstr += _nr_to_str(first_int) + _nr_to_str(second_int)
        
        return colorstr
    
    else:
        raise ValueError("Color type must be ColorHex or ColorTuple format")
        


if __name__ == "__main__":
    print(switch_color_format("#ffaa1b"))
    print(switch_color_format((255, 170, 27)))
