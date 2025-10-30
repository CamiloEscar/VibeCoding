"""
Custom exceptions for the factorial calculator package.

This module defines specific exceptions that can be raised during
factorial calculation operations.
"""


class FactorialError(Exception):
    """Base exception class for factorial calculator errors."""

    pass


class InvalidInputError(FactorialError):
    """
    Exception raised when invalid input is provided.

    This exception is raised when the input value is not a valid
    non-negative integer or exceeds acceptable bounds.
    """

    pass


class OverflowError(FactorialError):
    """
    Exception raised when factorial calculation would cause overflow.

    This exception is raised when attempting to calculate factorials
    that would exceed reasonable computational limits.
    """

    pass
