"""
This module initializes color settings for terminal output using the colorama library.

The main purpose of this module is to set up color constants for use in formatting terminal
output with various colors and styles. It initializes the colorama library to enable cross-platform
color support in the terminal.

Modules and Constants:
- colorama: A library for cross-platform colored terminal text.
- BLACK, BLUE, CYAN, GREEN, GREY, MAGENTA, RED, WHITE, YELLOW: Foreground color constants.
- BOLD: Constant for bright style text.
- RESET: Constant to reset all styles to default.

The module initializes colorama to ensure that color support is properly set up on all platforms.
"""

import colorama

colorama.init()

BLACK: str = colorama.Fore.BLACK
BLUE: str = colorama.Fore.BLUE
CYAN: str = colorama.Fore.CYAN
GREEN: str = colorama.Fore.GREEN
GREY: str = colorama.Fore.LIGHTBLACK_EX
MAGENTA: str = colorama.Fore.MAGENTA
RED: str = colorama.Fore.RED
WHITE: str = colorama.Fore.WHITE
YELLOW: str = colorama.Fore.YELLOW

BOLD: str = colorama.Style.BRIGHT
RESET: str = colorama.Style.RESET_ALL
