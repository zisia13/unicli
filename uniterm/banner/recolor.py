from typing import TypeAlias, Tuple

BannerString: TypeAlias = str
ColoredBanner: TypeAlias = str
Color: TypeAlias = Tuple[int, int, int]

class BannerPainter:
    reset = "\033[0m"

    @staticmethod
    def two_color_horizontal(text: BannerString, start_color: Color, end_color: Color) -> ColoredBanner:
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

    @staticmethod
    def two_color_vertical(text: BannerString, start_color: Color, end_color: Color) -> ColoredBanner:
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
    
    @staticmethod
    def four_color_horizontal(text: BannerString, color_1: Color, color_2: Color, color_3: Color, color_4: Color) -> ColoredBanner:
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

    @staticmethod
    def four_color_vertical(text: BannerString, color_1: Color, color_2: Color, color_3: Color, color_4: Color) -> ColoredBanner:
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
