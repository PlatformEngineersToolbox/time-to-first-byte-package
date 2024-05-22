"""
This module handles URL processing and timing information display for the URL timing analysis program.

The main purpose of this module is to validate a given URL, execute curl commands to measure various
timing metrics, and display the results in a formatted manner.

Functions:
- process_url: Validates the URL and initiates the timing display process.
- display_timing: Executes curl commands to measure and display timing metrics for the URL.

Modules:
- subprocess: Used to run curl commands to measure timing metrics.
- types.SimpleNamespace: Used to handle configuration settings.
- wolfsoftware.drawlines: Provides functions to draw formatted lines in the terminal.
- globals: Imports global constants like SCRIPT_TITLE.
- utils: Imports utility functions like validate_url.
"""
# pylint: disable=relative-beyond-top-level

import subprocess  # nosec B404

from types import SimpleNamespace

from wolfsoftware.drawlines import draw_line

from .globals import SCRIPT_TITLE
from .utils import validate_url


def process_url(config: SimpleNamespace) -> None:
    """
    Process a URL based on the provided configuration.

    This function validates the URL specified in the configuration and displays timing information.

    Arguments:
        config (SimpleNamespace): The configuration object containing the URL and other settings.
    """
    validate_url(config.url)
    display_timing(config)


def display_timing(config: SimpleNamespace) -> None:
    """
    Display timing information for the specified URL.

    This function prints formatted lines and executes curl commands to display various timing metrics
    (such as lookup time, connect time, TTFB, and total time) for the URL specified in the configuration.

    The command executed depends on the configuration:
        - Minimal: Only TTFB and total time.
        - Full: Detailed timing metrics including lookup, connect, app connect, pre-transfer, redirect, TTFB, and total time.
        - Default: A subset of the full metrics.

    Arguments:
        config (SimpleNamespace): The configuration object containing settings such as screen width, URL, command paths,
                                  verbosity, and the number of times to repeat the command.
    """
    print(draw_line(width=config.screen_width))
    print(draw_line(width=config.screen_width, text=SCRIPT_TITLE, fill_char=' '))
    print(draw_line(width=config.screen_width, text=f"Results for {config.url}", fill_char=' '))
    print(draw_line(width=config.screen_width))

    minimal_command: list[str] = [
        config.command_paths['curl'], '-L', '-o', '/dev/null', '-H', 'Cache-Control: no-cache', '-s', '-w',
        '  StartXfer Time (TTFB): %{time_starttransfer}   Total Time: %{time_total}\n',
        config.url
    ]
    full_command: list[str] = [
        config.command_paths['curl'], '-L', '-o', '/dev/null', '-H', 'Cache-Control: no-cache', '-s', '-w',
        (
            '  Lookup Time: %{time_namelookup}   Connect Time: %{time_connect}   AppCon Time: %{time_appconnect}   PreXfer Time: %{time_pretransfer}   '
            'Redirect Time: %{time_redirect}   StartXfer Time (TTFB): %{time_starttransfer}   Total Time: %{time_total}\n'
        ),
        config.url
    ]
    default_command: list[str] = [
        config.command_paths['curl'], '-L', '-o', '/dev/null', '-H', 'Cache-Control: no-cache', '-s', '-w',
        '  Lookup Time: %{time_namelookup}   Connect Time: %{time_connect}   StartXfer Time (TTFB): %{time_starttransfer}   Total Time: %{time_total}\n',
        config.url
    ]

    for _i in range(config.count):
        if config.minimal:
            subprocess.run(minimal_command, text=True, check=True)  # nosec B603
        elif config.full:
            subprocess.run(full_command, text=True, check=True)  # nosec B603
        else:
            subprocess.run(default_command, text=True, check=True)  # nosec B603

    print(draw_line(width=config.screen_width))
