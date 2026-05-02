import curses
import time

from zModules.zExtensions import private, public

from default import *

class Term_Select:

    #! init methods
    def __init__(self, 
                 pointer = DEFAULT_POINTER,

                 t_l = DEFAULT_TOP_LEFT,
                 t_r = DEFAULT_TOP_RIGHT,
                 b_l = DEFAULT_BOTTOM_LEFT,
                 b_r = DEFAULT_BOTTOM_RIGHT,
                 h_l = DEFAULT_HORIZONAL_LINE,
                 v_l = DEFAULT_VERTICAL_LINE,

                 u_k = DEFAULT_UP_KEYS,
                 d_k = DEFAULT_DOWN_KEYS,
                 q_k = DEFAULT_QUIT_KEYS,
                 e_k = DEFAULT_ENTER_KEYS,

                 h_t = DEFAULT_HELP_TEXT,

                 d_b_c = DEFAULT_BORDER_COLOR,
                 d_t_c = DEFAULT_TITLE_COLOR,
                 d_p_c = DEFAULT_POINTER_COLOR,
                 d_c_c = DEFAULT_CURRENT_COLOR,
                 d_o_c = DEFAULT_OTHER_COLOR,
                 d_h_t_c = DEFAULT_HELP_TEXT_COLOR
                ):
        
        self.pointer = pointer

        self.corners = {
            'tl': t_l,
            'tr': t_r,
            'bl': b_l,
            'br': b_r,
            'h': h_l, 
            'v': v_l
        }

        self.border_color = d_b_c
        self.title_color = d_t_c
        self.pointer_color = d_p_c
        self.current_color = d_c_c
        self.other_color = d_o_c
        self.help_text_color = d_h_t_c

        self.UP_keys = u_k
        self.DOWN_keys = d_k
        self.QUIT_keys = q_k
        self.ENTER_keys = e_k

        self.help_text = h_t

    @private
    def init_curses(self):
        
        stdscr = curses.initscr()
       
        curses.start_color()
        self.TS_init_color()
        self.TS_init_pair()

        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)

        curses.curs_set(0)

        return stdscr

    #! color methods
    @private
    def TS_transform_color(self, r, g, b):
        _r = int(r * 1000 / 255)
        _g = int(g * 1000 / 255)
        _b = int(b * 1000 / 255)
        return (_r, _g, _b)
    
    @private
    def TS_init_color(self):
        for color in TS_ALL_COLORS:
            color_id, color_data = color
            r = color_data[0]
            g = color_data[1]
            b = color_data[2]
            curses_r, curses_g, curses_b = self.TS_transform_color(r, g, b)
            curses.init_color(color_id, curses_r, curses_g, curses_b)

    @private
    def TS_init_pair(self):
        for pair in TS_ALL_COLOR_PAIRS:
            curses_color_pair_id, curses_fg_color, curses_bg_color = pair
            curses.init_pair(curses_color_pair_id, curses_fg_color, curses_bg_color)

    #! draw methods
    @private
    def draw(self, win, y, x, text, attr = curses.A_NORMAL):
        try:
            win.addstr(y, x, text, attr)
        except curses.error:
            pass

    @private
    def draw_rounded_border(self, stdscr):

        h, w = stdscr.getmaxyx()

        self.draw(stdscr, 0, 0, self.corners['tl'], curses.color_pair(self.border_color))
        self.draw(stdscr, 0, w - 1, self.corners['tr'], curses.color_pair(self.border_color))
        self.draw(stdscr, h - 1, 0, self.corners['bl'], curses.color_pair(self.border_color))
        self.draw(stdscr, h - 1, w - 1, self.corners['br'], curses.color_pair(self.border_color))

        for x in range(1, w - 1):
            self.draw(stdscr, 0, x, self.corners['h'], curses.color_pair(self.border_color))
            self.draw(stdscr, h - 1, x, self.corners['h'], curses.color_pair(self.border_color))

        for y in range(1, h - 1):
            self.draw(stdscr, y, 0, self.corners['v'], curses.color_pair(self.border_color))
            self.draw(stdscr, y, w - 1, self.corners['v'], curses.color_pair(self.border_color))

    #! change attr methods
    @public
    def change_UI(self, **kwargs):

        """
        :Args (all str): ..
            .. pointer
            .. corner_tl
            .. corner_tr
            .. corner_bl
            .. corner_br
            .. h_line
            .. v_line
        """

        ui_attrs = [
            "pointer",
            "corner_tl",
            "corner_tr",
            "corner_bl",
            "corner_br",
            "h_line",
            "v_line"
        ]
        for attr in ui_attrs:
            if attr in kwargs:
                if type(kwargs[attr]) == str:
                    setattr(self, attr, kwargs[attr])
                else: 
                    raise ValueError("Type of attr must str!")

    @public
    def change_colors(self, **kwargs):

        """
        :Args (all str): ..
            .. border_color
            .. title_color
            .. pointer_color
            .. current_color
            .. other_color
            .. help_text_color
        """

        color_attrs = [
            "border_color",
            "title_color",
            "pointer_color", 
            "current_color",
            "other_color",
            "help_text_color"
        ]
        for attr in color_attrs:
            if attr in kwargs:
                if type(kwargs[attr]) == int:
                    setattr(self, attr, kwargs[attr])
                else:
                    raise ValueError("Type of attr must be int!")

    @public
    def change_keybinds(self, **kwarg):
        pass                                            #todo !

    #! interface methods
    @public
    def select_interface(self, message, choices, endless = False):

        stdscr = self.init_curses()

        try:
            current = 0
            h, w = stdscr.getmaxyx()

            max_option_len = max(len(choice) for choice in choices) + 4
            menu_width = min(max_option_len + 4, w - 6)
            start_x = (w - menu_width) // 2
            start_y = max(4, (h - len(choices)) // 2)

            while True:

                stdscr.clear()
                self.draw_rounded_border(stdscr)
                
                title = f" {message} "
                title_x = (w - len(title)) // 2
                self.draw(stdscr, 2, title_x, title, curses.color_pair(self.title_color))

                for i, choice in enumerate(choices):
                    y_pos = start_y + i
                    if y_pos >= h - 2: break

                    pointer = self.pointer if i == current else "  "
                    text = pointer + choice
                    attr = curses.color_pair(self.current_color) if i == current else curses.color_pair(self.other_color)
                    self.draw(stdscr, y_pos, start_x, text, attr)

                help_x = (w - len(self.help_text)) // 2
                self.draw(stdscr, h - 3, help_x, self.help_text, curses.color_pair(self.help_text_color))

                stdscr.refresh()

                key = stdscr.getch()
                if key in self.QUIT_keys: return None
                elif key in self.UP_keys and current > 0: current -= 1
                elif key in self.DOWN_keys and current < len(choices) - 1: current += 1
                elif key in self.ENTER_keys: return choices[current]

        finally:
            if not endless:
                curses.nocbreak()
                stdscr.keypad(False)
                curses.echo()
                curses.curs_set(1)
                curses.endwin()

if __name__ == "__main__":
    import os, time
    os.system("")
    print("\033[38;2;255;0;0mDo not execute this file!")
    print("\033[38;2;255;255;255mInstead: from TermSelect.py import Term_Select!")
    time.sleep(5)
    raise PermissionError()
