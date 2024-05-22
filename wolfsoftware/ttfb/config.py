"""
This module defines the configuration setup for the URL timing analysis program.

The main purpose of this module is to create a configuration object from the
command-line arguments and command paths. The configuration object is used to
store various settings such as verbosity, debug mode, URL, and screen width,
which are necessary for performing the timing analysis.

Functions:
- create_configuration_from_arguments: Creates and returns a configuration object
  based on parsed command-line arguments and command paths.

Modules:
- argparse.Namespace: Used for type annotation of command-line arguments.
- types.SimpleNamespace: Used to create a simple object for storing configuration settings.
"""

from argparse import Namespace

from types import SimpleNamespace


def create_configuration_from_arguments(args: Namespace, command_paths: dict) -> SimpleNamespace:
    """
    Create a configuration object from command-line arguments and command paths.

    This function takes the parsed command-line arguments and command paths to populate
    a SimpleNamespace object with the appropriate configuration settings.

    Arguments:
        args (Namespace): The parsed command-line arguments.
        command_paths (dict): A dictionary containing command paths.

    Returns:
        SimpleNamespace: A configuration object populated with the necessary settings.
                         This includes verbosity, debug mode, minimal/full configuration,
                         count, URL, screen width, and command paths.
    """
    config: SimpleNamespace = SimpleNamespace()

    config.verbose = args.verbose
    config.debug = args.debug
    config.minimal = args.minimal
    config.full = args.full
    config.count = args.count
    config.url = args.url

    if config.full:
        config.screen_width = 182
    elif config.minimal:
        config.screen_width = 58
    else:
        config.screen_width = 107

    config.command_paths = command_paths

    return config
