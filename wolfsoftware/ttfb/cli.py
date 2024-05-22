"""
This module contains the main execution flow for the URL timing analysis program.

This program checks for the presence of required command-line tools, parses command-line
arguments, validates a given URL, and measures the timing metrics for the URL using curl.
The timing results are displayed based on the specified configuration options.

Modules and Functions:
- check_int_range: Validates that an integer value is within a specified range.
- setup_arg_parser: Sets up the command-line argument parser with necessary arguments and options.
- process_arguments: Processes and validates the command-line arguments.
- run: Main function to execute the program, coordinating all necessary steps.
- create_configuration_from_arguments: Creates a configuration object from the parsed arguments.
- process_url: Validates the URL and performs the timing analysis.
- display_timing: Displays detailed timing results for the URL.
- display_results: Displays the results header and configuration information.
- check_prerequisite: Checks for the presence of required command-line tools.
- validate_url: Validates that the URL is properly formed and reachable.
"""
# pylint: disable=relative-beyond-top-level

import argparse
import sys

from types import SimpleNamespace

from .config import create_configuration_from_arguments
from .globals import ARG_PARSER_DESCRIPTION, ARG_PARSER_EPILOG, ARG_PARSER_PROG_NAME, VERSION_STRING
from .process import process_url
from .utils import check_prereqs


def check_int_range(value) -> int:
    """
    Validate that an integer value is within the specified range (1 to 25).

    This function attempts to convert the input value to an integer and checks if it
    falls within the range of 1 to 25, inclusive. If the value is not an integer or
    is outside the specified range, it raises an `argparse.ArgumentTypeError`.

    Arguments:
        value (str): The input value to be validated.

    Returns:
        int: The validated integer value.

    Raises:
        argparse.ArgumentTypeError: If the input value is not a valid integer.
        argparse.ArgumentTypeError: If the integer value is not within the range 1 to 25.
    """
    try:
        ivalue = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"Invalid integer value: {value}") from exc
    if ivalue < 1 or ivalue > 25:
        raise argparse.ArgumentTypeError(f"Integer value must be between 1 and 25: {value}")
    return ivalue


def setup_arg_parser() -> argparse.ArgumentParser:
    """
    Set up and returns the argument parser for the program.

    This function defines and configures the argument parser with the necessary arguments and options
    for the program, including flags, exclusive flags, optional arguments, and required arguments.

    Returns:
        argparse.ArgumentParser: The configured argument parser.
    """
    parser = argparse.ArgumentParser(prog=ARG_PARSER_PROG_NAME,
                                     add_help=False,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description=ARG_PARSER_DESCRIPTION,
                                     epilog=ARG_PARSER_EPILOG)

    flags: argparse._ArgumentGroup = parser.add_argument_group(title='flags')
    exclusive_flags: argparse._ArgumentGroup = parser.add_argument_group(title='exclusive flags')
    optional: argparse._ArgumentGroup = parser.add_argument_group(title='optional')
    required: argparse._ArgumentGroup = parser.add_argument_group(title='required')

    flags.add_argument("-h", "--help", action="help", default=argparse.SUPPRESS, help="show this help message and exit")
    flags.add_argument("-d", "--debug", action="store_true", default=False, help="Very noisy")
    flags.add_argument("-v", "--verbose", action="store_true", default=False, help="Verbose output - show scan results as they come in")
    flags.add_argument('-V', '--version', action="version", version=VERSION_STRING, help="Show program's version number and exit.")

    exclusive_flags_group: argparse._MutuallyExclusiveGroup = exclusive_flags.add_mutually_exclusive_group(required=False)
    exclusive_flags_group.add_argument('-m', '--minimal', action="store_true", default=False, help="Show minimal set of timing values.")
    exclusive_flags_group.add_argument('-f', '--full', action="store_true", default=False, help="Show full set of timing values.")

    optional.add_argument("-c", "--count", type=check_int_range, default=1, help="How many times to test [1-25]")

    required.add_argument("-u", "--url", type=str, required=True, help="The URL to test")

    return parser


def process_arguments(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """
    Process the command line arguments.

    This function uses the provided argument parser to parse the command line arguments,
    validate the input, and then return the parsed arguments as a Namespace object.

    Arguments:
        parser (argparse.ArgumentParser): The argument parser configured with the necessary arguments and options.

    Returns:
        argparse.Namespace: The parsed command line arguments.
    """
    args: argparse.Namespace = parser.parse_args()

    return args


def run() -> None:
    """
    Master controller function.

    This function performs the following steps:
    1. Checks prerequisites and obtains command paths.
    2. Sets up the argument parser.
    3. Processes command-line arguments.
    4. Creates a configuration from the processed arguments.
    5. Processes a URL based on the created configuration.

    If there is an argument type error during argument processing, it prints the usage information,
    prints the error message, and exits the program with a status code of 1.
    """
    command_paths: dict = check_prereqs()
    parser: argparse.ArgumentParser = setup_arg_parser()
    try:
        args: argparse.Namespace = process_arguments(parser)
        config: SimpleNamespace = create_configuration_from_arguments(args, command_paths)
        process_url(config)
    except argparse.ArgumentTypeError as err:
        parser.print_usage()
        print(err)
        sys.exit(1)
