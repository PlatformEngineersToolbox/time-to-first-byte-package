#!/usr/bin/env python
"""
This module serves as the entry point for the URL timing analysis program.

The main purpose of this module is to initiate the program execution by calling the `run` function
and handling any KeyboardInterrupt exceptions to allow for graceful termination of the program.

Functions:
- main: The main entry point of the program that calls the `run` function and handles exceptions.

Modules:
- sys: Provides access to system-specific parameters and functions.
- run: The main function that executes the core logic of the program, imported from the cli module.
- system: A function to display system notifications, imported from the notify module.
"""
# pylint: disable=relative-beyond-top-level

import sys

from wolfsoftware.notify import system_message

from .cli import run


def main() -> None:
    """
    Execute the main entry point for the program.

    This function attempts to execute the `run` function and handles a KeyboardInterrupt
    exception to gracefully exit the program.

    If a KeyboardInterrupt is detected (typically from pressing Ctrl+C), it prints an
    exit message and terminates the program with a status code of 1.
    """
    try:
        run()
    except KeyboardInterrupt:
        print(system_message("\n[*] Exiting Program\n"))
        sys.exit(1)


if __name__ == "__main__":
    main()
