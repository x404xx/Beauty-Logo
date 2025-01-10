from enum import Enum, auto
from os import get_terminal_size
from random import randint


class ColorMode(Enum):
    BRIGHT_BLUE = auto()
    BLACK_WHITE = auto()
    PURPLE_BLUE = auto()
    LIGHT_GREEN = auto()
    PINK_RED = auto()
    LIGHT_BLUE = auto()
    YELLOW_ORANGE = auto()
    BRIGHT_GREEN = auto()
    RANDOM = auto()


class ColorFader:
    def __init__(self, text):
        self.text = text
        self.terminal_width = get_terminal_size().columns
        self._initialize_colors()

    def _initialize_colors(self):
        self.colors = {
            ColorMode.BRIGHT_BLUE: {"red": 110, "green": 0, "blue": 255},
            ColorMode.BLACK_WHITE: {"red": 0, "green": 0, "blue": 0},
            ColorMode.PURPLE_BLUE: {"red": 40, "green": 0, "blue": 220},
            ColorMode.LIGHT_GREEN: {"red": 0, "green": 255, "blue": 100},
            ColorMode.PINK_RED: {"red": 255, "green": 0, "blue": 255},
            ColorMode.LIGHT_BLUE: {"red": 0, "green": 10, "blue": 255},
            ColorMode.YELLOW_ORANGE: {"red": 255, "green": 250, "blue": 0},
            ColorMode.BRIGHT_GREEN: {"red": 0, "green": 255, "blue": 0},
        }

    def _center_text(self, line):
        padding = (self.terminal_width - len(line)) // 2
        return " " * padding + line

    def _fade(self, line, red, green, blue):
        return f"\033[38;2;{red};{green};{blue}m{line}\033[0m"

    def _fade_color(self, line, mode):
        color = self.colors.get(mode, {"red": 0, "green": 0, "blue": 0})
        red, green, blue = color["red"], color["green"], color["blue"]

        if mode == ColorMode.BRIGHT_BLUE:
            red = max(0, red - 15)
        elif mode == ColorMode.BLACK_WHITE:
            red = green = blue = min(255, red + 20)
        elif mode == ColorMode.PURPLE_BLUE:
            red = min(255, red + 15)
        elif mode == ColorMode.LIGHT_GREEN:
            blue = min(255, blue + 15)
        elif mode == ColorMode.PINK_RED:
            blue = max(0, blue - 20)
        elif mode == ColorMode.LIGHT_BLUE:
            green = min(255, green + 15)
        elif mode == ColorMode.YELLOW_ORANGE:
            green = max(0, green - 25)
        elif mode == ColorMode.BRIGHT_GREEN:
            red = min(255, red + 30)

        self.colors[mode] = {"red": red, "green": green, "blue": blue}
        return self._fade(line, red, green, blue)

    def _random_fade(self, line):
        return self._fade(line, randint(0, 255), randint(0, 255), randint(0, 255))

    def apply_fade(self, mode):
        if mode == ColorMode.RANDOM:
            return "\n".join(
                self._random_fade(self._center_text(line))
                for line in self.text.splitlines()
            )
        else:
            return "\n".join(
                self._fade_color(self._center_text(line), mode)
                for line in self.text.splitlines()
            )
