"""Unit tests for custom exceptions module."""

import pytest

from factorial_calculator.exceptions import (
    FactorialError,
    InvalidInputError,
    OverflowError,
)


class TestExceptions:
    """Test suite for custom exception classes."""

    def test_factorial_error_is_exception(self) -> None:
        """Test that FactorialError is an Exception."""
        assert issubclass(FactorialError, Exception)

    def test_invalid_input_error_is_factorial_error(self) -> None:
        """Test that InvalidInputError inherits from FactorialError."""
        assert issubclass(InvalidInputError, FactorialError)

    def test_overflow_error_is_factorial_error(self) -> None:
        """Test that OverflowError inherits from FactorialError."""
        assert issubclass(OverflowError, FactorialError)

    def test_raise_factorial_error(self) -> None:
        """Test raising FactorialError."""
        with pytest.raises(FactorialError):
            raise FactorialError("Test error")

    def test_raise_invalid_input_error(self) -> None:
        """Test raising InvalidInputError."""
        with pytest.raises(InvalidInputError):
            raise InvalidInputError("Invalid input")

    def test_raise_overflow_error(self) -> None:
        """Test raising OverflowError."""
        with pytest.raises(OverflowError):
            raise OverflowError("Overflow occurred")

    def test_factorial_error_message(self) -> None:
        """Test FactorialError message."""
        error = FactorialError("Custom message")
        assert str(error) == "Custom message"

    def test_invalid_input_error_message(self) -> None:
        """Test InvalidInputError message."""
        error = InvalidInputError("Invalid input message")
        assert str(error) == "Invalid input message"

    def test_overflow_error_message(self) -> None:
        """Test OverflowError message."""
        error = OverflowError("Overflow message")
        assert str(error) == "Overflow message"

    def test_catch_invalid_input_as_factorial_error(self) -> None:
        """Test catching InvalidInputError as FactorialError."""
        with pytest.raises(FactorialError):
            raise InvalidInputError("Test")

    def test_catch_overflow_as_factorial_error(self) -> None:
        """Test catching OverflowError as FactorialError."""
        with pytest.raises(FactorialError):
            raise OverflowError("Test")
