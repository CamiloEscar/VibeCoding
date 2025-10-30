"""
Factorial Calculator Package.

A robust Python package for calculating factorials with comprehensive error handling,
input validation, and CLI interface.
"""

__version__ = "1.0.0"
__author__ = "VibeCoding"
__license__ = "MIT"

from factorial_calculator.core import FactorialCalculator
from factorial_calculator.exceptions import (
    FactorialError,
    InvalidInputError,
    OverflowError,
)

__all__ = [
    "FactorialCalculator",
    "FactorialError",
    "InvalidInputError",
    "OverflowError",
]
