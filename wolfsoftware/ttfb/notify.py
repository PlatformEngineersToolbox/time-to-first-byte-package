"""
This module defines functions for printing formatted messages to the terminal.

The main purpose of this module is to provide utility functions for displaying
success, warning, error, information, and system messages with specific color
and style formatting using predefined constants.

Functions:
- success: Prints a success message formatted with bold and green text.
- warn: Prints a warning message formatted with bold and yellow text.
- error: Prints an error message formatted with bold and red text.
- info: Prints an information message formatted with bold and cyan text.
- system: Prints a system message formatted with bold and grey text.

Modules:
- constants: Imports color and style constants (CYAN, GREEN, GREY, RED, YELLOW, BOLD, RESET)
  from the constants module.
"""
# pylint: disable=relative-beyond-top-level

from .constants import CYAN, GREEN, GREY, RED, YELLOW, BOLD, RESET


def success(message: str) -> None:
    """
    Print a success message with a specific format.

    This function outputs a message indicating success, formatted with bold and green text.

    Arguments:
        message (str): The success message to be printed.
    """
    print(f'[ {BOLD}{GREEN}Success{RESET} ] {message}')


def warn(message: str) -> None:
    """
    Print a warning message with a specific format.

    This function outputs a message indicating a warning, formatted with bold and yellow text.

    Arguments:
        message (str): The warning message to be printed.
    """
    print(f'[ {BOLD}{YELLOW}Warning{RESET} ] {message}')


def error(message: str) -> None:
    """
    Print an error message with a specific format.

    This function outputs a message indicating success, formatted with bold and red text.

    Arguments:
        message (str): The error message to be printed.
    """
    print(f'[ {BOLD}{RED}Error{RESET} ] {message}')


def info(message: str) -> None:
    """
    Print an information message with a specific format.

    This function outputs a message indicating success, formatted with bold and cyan text.

    Arguments:
        message (str): The information message to be printed.
    """
    print(f'[ {BOLD}{CYAN}Info{RESET} ] {message}')


def system(message: str) -> None:
    """
    Print a system message with a specific format.

    This function outputs a message indicating success, formatted with bold and grey text.

    Arguments:
        message (str): The system message to be printed.
    """
    print(f'{BOLD}{GREY}{message}{RESET}')
