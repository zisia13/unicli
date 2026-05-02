from typing import Any, TypeAlias, Tuple

BannerFormat: TypeAlias = Any
Color: TypeAlias = Tuple[int, int, int]

reset = "\033[0m"

def recolor_horizontal_2c(text: BannerFormat, start_color: Color, end_color: Color) -> BannerFormat:
    lines = text.split('\n')
    colored_lines = []
    
    for line in lines:
        if not line.strip():
            colored_lines.append("")
            continue
            
        colored_line = []
        line_length = len(line)
        
        for i, char in enumerate(line):
            ratio = i / max(line_length - 1, 1)
    
            r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
            g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
            b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)
            
            color_code = f"\033[38;2;{r};{g};{b}m"
            colored_line.append(f"{color_code}{char}")
        
        colored_lines.append("".join(colored_line))
    
    return "\n".join(colored_lines)

def recolor_vertical_2c(text: BannerFormat, start_color: Color, end_color: Color) -> BannerFormat:
    r1, g1, b1 = start_color
    r2, g2, b2 = end_color
    
    lines = text.split('\n')
    colored_lines = []
    total_lines = len(lines)
    
    for i, line in enumerate(lines):
        ratio = i / max(total_lines - 1, 1)
        r = int(r1 + (r2 - r1) * ratio)
        g = int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b1) * ratio)
        
        color_code = f"\033[38;2;{r};{g};{b}m"
        colored_lines.append(f"{color_code}{line}")
    
    return '\n'.join(colored_lines)

def recolor_horizontal_4c(text: BannerFormat, color_1: Color, color_2: Color, color_3: Color, color_4: Color) -> BannerFormat:
    lines = text.split('\n')
    colored_lines = []
    colors = [color_1, color_2, color_3, color_4]
    segment_count = len(colors) - 1
    max_segment_index = len(colors) - 2

    for line in lines:
        if not line.strip():
            colored_lines.append("")
            continue

        colored_line = []
        visible_chars = [char for char in line if char != " "]
        visible_count = len(visible_chars)
        visible_index = 0

        for char in line:
            if char == " ":
                colored_line.append(char)
                continue

            ratio = visible_index / max(visible_count - 1, 1)
            scaled = ratio * segment_count
            segment = min(int(scaled), max_segment_index)
            local_ratio = scaled - segment

            c1 = colors[segment]
            c2 = colors[segment + 1]
            r = int(c1[0] + (c2[0] - c1[0]) * local_ratio)
            g = int(c1[1] + (c2[1] - c1[1]) * local_ratio)
            b = int(c1[2] + (c2[2] - c1[2]) * local_ratio)
            color_code = f"\033[38;2;{r};{g};{b}m"
            colored_line.append(f"{color_code}{char}")
            visible_index += 1

        colored_lines.append("".join(colored_line))

    return "\n".join(colored_lines)

def recolor_vertical_4c(text: BannerFormat, color_1: Color, color_2: Color, color_3: Color, color_4: Color) -> BannerFormat:
    lines = text.split('\n')
    colored_lines = []
    colors = [color_1, color_2, color_3, color_4]
    segment_count = len(colors) - 1
    max_segment_index = len(colors) - 2
    visible_lines = [line for line in lines if line.strip()]
    visible_count = len(visible_lines)
    visible_index = 0

    for line in lines:
        if not line.strip():
            colored_lines.append(line)
            continue

        ratio = visible_index / max(visible_count - 1, 1)
        scaled = ratio * segment_count
        segment = min(int(scaled), max_segment_index)
        local_ratio = scaled - segment

        c1 = colors[segment]
        c2 = colors[segment + 1]
        r = int(c1[0] + (c2[0] - c1[0]) * local_ratio)
        g = int(c1[1] + (c2[1] - c1[1]) * local_ratio)
        b = int(c1[2] + (c2[2] - c1[2]) * local_ratio)
        color_code = f"\033[38;2;{r};{g};{b}m"
        colored_lines.append(f"{color_code}{line}")
        visible_index += 1

    return '\n'.join(colored_lines)

if __name__ == "__main__":
    import os
    os.system("")

    banner_string_1 = """
     ███████████                          ███                     █████   
    ░░███░░░░░███                        ░░░                     ░░███    
     ░███    ░███ ████████   ██████      █████  ██████   ██████  ███████  
     ░██████████ ░░███░░███ ███░░███    ░░███  ███░░███ ███░░███░░░███░   
     ░███░░░░░░   ░███ ░░░ ░███ ░███     ░███ ░███████ ░███ ░░░   ░███    
     ░███         ░███     ░███ ░███     ░███ ░███░░░  ░███  ███  ░███ ███
     █████        █████    ░░██████      ░███ ░░██████ ░░██████   ░░█████ 
    ░░░░░        ░░░░░      ░░░░░░       ░███  ░░░░░░   ░░░░░░     ░░░░░  
                                     ███ ░███                             
                                    ░░██████                              
                                     ░░░░░░                               
    """

    banner_string_2 = """
    ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗
    ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝
    ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   
    ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   
    ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   
    """

    banner_string_3 = """
           _               _                    _             _        _        _    
          / /\            / /\                /\ \           /\_\     /\ \     /\_\ 
         / /  \          / /  \              /  \ \         / / /  _  \ \ \   / / / 
        / / /\ \        / / /\ \            / /\ \ \       / / /  /\_\ \ \ \_/ / / 
       / / /\ \ \      / / /\ \ \          / / /\ \ \     / / /__/ / /  \ \___/ / 
      / / /\ \_\ \    / / /  \ \ \        / / /  \ \_\   / /\_____/ /    \___/ / 
     / / /\ \ \___\  / / /___/ /\ \      / / /    \/_/  / /\_______/      / / /
    / / /  \ \ \__/ / / /_____/ /\ \    / / /          / / /\ \ \        / / /
   / / /____\_\ \  / /_________/\ \ \  / / /________  / / /  \ \ \      / / /
  / / /__________\/ / /_       __\ \_\/ / /_________\/ / /    \ \ \    / / /
  \/_____________/\_\___\     /____/_/\/____________/\/_/      \_\_\  /_/_/
"""


    color_blue: Color = (70, 130, 255)
    color_cyan: Color = (90, 220, 255)
    color_green: Color = (60, 230, 120)
    color_purple: Color = (160, 100, 255)
    color_pink: Color = (255, 120, 210)
    color_orange: Color = (255, 170, 60)

    print(recolor_horizontal_2c(banner_string_1, color_blue, color_purple) + reset)
    print()
    print(recolor_vertical_2c(banner_string_1, color_cyan, color_green) + reset)
    print()
    print(recolor_horizontal_4c(banner_string_2, color_blue, color_cyan, color_green, color_pink) + reset)
    print()
    print(recolor_vertical_4c(banner_string_2, color_purple, color_pink, color_orange, color_blue) + reset)
    print()
    print(recolor_horizontal_4c(banner_string_3, (87, 106, 143), (183, 189, 247), (255, 248, 222), (255, 116, 68)) + reset)
