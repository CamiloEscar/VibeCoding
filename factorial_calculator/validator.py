"""
Input validation module for factorial calculator.

This module provides validation functionality to ensure input values
are valid for factorial calculation.
"""

from factorial_calculator.exceptions import InvalidInputError


class InputValidator:
    """
    Validator class for factorial calculator inputs.

    This class implements the Strategy pattern for input validation,
    providing comprehensive checks for factorial calculation inputs.
    """

    # Maximum safe value for factorial calculation to prevent overflow
    MAX_FACTORIAL_INPUT = 10000

    @staticmethod
    def validate_number(value: int | str) -> int:
        """
        Validate and convert input to a valid integer for factorial calculation.

        Args:
            value: The input value to validate (can be int or string).

        Returns:
            int: The validated integer value.

        Raises:
            InvalidInputError: If the input is invalid, negative, or exceeds limits.

        Examples:
            >>> InputValidator.validate_number("5")
            5
            >>> InputValidator.validate_number(10)
            10
        """
        try:
            if isinstance(value, str):
                value = value.strip()
                if not value:
                    raise InvalidInputError("Input cannot be empty")

            num = int(value)
        except ValueError as e:
            raise InvalidInputError(
                f"Invalid input: '{value}' is not a valid integer"
            ) from e

        if num < 0:
            raise InvalidInputError(
                f"Invalid input: {num} is negative. "
                "Factorial is only defined for non-negative integers"
            )

        if num > InputValidator.MAX_FACTORIAL_INPUT:
            raise InvalidInputError(
                f"Invalid input: {num} exceeds maximum allowed value "
                f"of {InputValidator.MAX_FACTORIAL_INPUT}"
            )

        return num

    @staticmethod
    def is_valid_range(value: int) -> bool:
        """
        Check if a value is within valid range for factorial calculation.

        Args:
            value: The integer value to check.

        Returns:
            bool: True if value is within valid range, False otherwise.

        Examples:
            >>> InputValidator.is_valid_range(5)
            True
            >>> InputValidator.is_valid_range(-1)
            False
        """
        return 0 <= value <= InputValidator.MAX_FACTORIAL_INPUT
