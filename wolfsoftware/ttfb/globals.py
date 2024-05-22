"""
This module sets up global constants and version information for the URL timing analysis program.

The main purpose of this module is to define constants that are used throughout the application,
such as the program name, description, and version information. It also checks for prerequisite
commands needed for the program to run.

Modules and Constants:
- importlib.metadata: Used to retrieve package version information.
- version: The current version of the 'wolfsoftware.ttfb' package, or 'unknown' if the package is not found.
- ARG_PARSER_PROG_NAME: The program name for the argument parser.
- ARG_PARSER_DESCRIPTION: The description of the program for the argument parser.
- ARG_PARSER_EPILOG: The epilog for the argument parser.
- VERSION_STRING: A formatted string displaying the current version of the program.
- SCRIPT_TITLE: The title of the script, used in the output display.
- prerequisite_commands: A list of commands that are required for the program to run.

Exceptions:
- importlib.metadata.PackageNotFoundError: If the 'wolfsoftware.ttfb' package is not found.
"""

import importlib.metadata

try:
    version: str = importlib.metadata.version('wolfsoftware.ttfb')
except importlib.metadata.PackageNotFoundError:
    version = 'unknown'

ARG_PARSER_PROG_NAME: str = "ttfb"
ARG_PARSER_DESCRIPTION: str = "Display the time-to-first-byte for any given url."
ARG_PARSER_EPILOG: str = "The Epilog goes here"

VERSION_STRING: str = "Current version of " + ARG_PARSER_PROG_NAME + " is v" + version

SCRIPT_TITLE = "Time to First Byte Tester"
prerequisite_commands: list[str] = ["curl"]
