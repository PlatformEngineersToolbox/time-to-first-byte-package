"""
This module defines a custom exception for specific error handling within the program.

The main purpose of this module is to create a custom exception class that allows for more
granular and descriptive error handling tailored to the application's domain logic.

Classes:
- CustomException: A custom exception class used for specific error scenarios in the application.
"""


class CustomException(Exception):
    """
    A custom exception class for specific error handling within the program.

    This class is used to define exceptions that are specific to the application's
    domain logic, allowing for more granular and descriptive error handling.

    Inherits from:
        Exception: The base class for all built-in exceptions.
    """
