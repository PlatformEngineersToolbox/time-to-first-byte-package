"""
This module handles prerequisite checks and URL validation for the URL timing analysis program.

The main purpose of this module is to ensure that all necessary commands are available
and to validate the format and reachability of the specified URL.

Functions:
- check_prerequisite: Verifies the presence of prerequisite commands and returns their paths.
- validate_url: Validates that a URL is well-formed and reachable.

Modules:
- shutil: Used to check for the presence of commands.
- sys: Provides access to system-specific parameters and functions.
- subprocess: Used to run curl commands to validate URL reachability (with security warning disabled).
- globals: Imports global constants like prerequisite_commands.
- notify: Imports utility functions like error for displaying error messages.
"""
# pylint: disable=relative-beyond-top-level

import sys

import subprocess  # nosec B404

from wolfsoftware.notify import error_message
from wolfsoftware.prereqs import check_prerequisite, PrerequisiteCheckError

from .globals import prerequisite_commands


def check_prereqs() -> dict:
    """
    Check for the presence of prerequisite commands and returns their paths.

    This function iterates through a list of prerequisite commands to verify their installation
    using `shutil.which`. It collects the full paths of the installed commands into a dictionary.
    If any commands are not found, it prints the errors and exits the program with a status code of 1.

    Returns:
        dict: A dictionary mapping each prerequisite command to its full path.

    Exits:
        If any prerequisite commands are not installed, prints the errors and exits the program.
    """
    try:
        command_paths: dict = check_prerequisite(prerequisite_commands)
        return command_paths
    except PrerequisiteCheckError as errors:
        print(error_message("Prerequisite check failed:"))
        for err in errors.errors:
            print(err)
        sys.exit(1)


def validate_url(url) -> None:
    """
    Validate the given URL to ensure it is well-formed and reachable.

    This function checks that the URL is a string and starts with 'http://' or 'https://'.
    It then uses a curl command to verify that the URL exists and is reachable. If the URL is invalid
    or unreachable, it prints an error message and exits the program with a status code of 1.

    Arguments:
        url (str): The URL to be validated.

    Exits:
        If the URL does not exist or is unreachable, prints an error message and exits the program.
    """
    if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
        print(error_message("Invalid URL - must start with http:// or https://"))
        sys.exit(1)

    command: list[str] = ['curl', '-o', '/dev/null', '--silent', '--head', '--fail', '--connect-timeout', '1', url]
    try:
        result: subprocess.CompletedProcess[str] = subprocess.run(  # nosec B603
            command, text=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if result.returncode != 0:
            print(error_message(f"{url} does not exist - aborting"))
            sys.exit(1)

    except subprocess.CalledProcessError:
        print(error_message(f"{url} does not exist - aborting"))
        sys.exit(1)

    except Exception:
        print(error_message(f"An unexpected error occurred while checking {url}"))
        sys.exit(1)
