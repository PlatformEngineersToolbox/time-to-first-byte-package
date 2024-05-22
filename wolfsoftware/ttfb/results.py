"""
This module handles the display of results for the URL timing analysis program.

The main purpose of this module is to format and display the results header and configuration
information for the specified URL.

Functions:
- display_results: Displays custom formatted lines and configuration details for the URL.

Modules:
- types.SimpleNamespace: Used to handle configuration settings.
- utils: Imports utility functions like draw_custom_line for custom line drawing.
"""
# pylint: disable=relative-beyond-top-level

from types import SimpleNamespace

from .utils import draw_custom_line


def display_results(config: SimpleNamespace) -> None:
    """
    Display the results header and configuration information for the specified URL.

    This function prints custom formatted lines and the configuration details.
    It uses `draw_custom_line` to display the header and the URL being tested, and
    prints the configuration object.

    Arguments:
        config (SimpleNamespace): The configuration object containing settings such as the URL and other details.
    """
    draw_custom_line()
    draw_custom_line("Time to First Byte Tester", "center", " ", color="cyan")
    draw_custom_line(f"Results for: {config.url}", "center", " ")
    draw_custom_line()
    print(f"Config: {config}")
    draw_custom_line()
