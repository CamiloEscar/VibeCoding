"""Unit tests for the input validator module."""

import pytest

from factorial_calculator.exceptions import InvalidInputError
from factorial_calculator.validator import InputValidator


class TestInputValidator:
    """Test suite for InputValidator class."""

    def test_validate_valid_integer(self) -> None:
        """Test validation of valid integer."""
        result = InputValidator.validate_number(5)
        assert result == 5

    def test_validate_valid_string_number(self) -> None:
        """Test validation of valid string representation of number."""
        result = InputValidator.validate_number("10")
        assert result == 10

    def test_validate_zero(self) -> None:
        """Test validation of zero."""
        result = InputValidator.validate_number(0)
        assert result == 0

    def test_validate_string_zero(self) -> None:
        """Test validation of string zero."""
        result = InputValidator.validate_number("0")
        assert result == 0

    def test_validate_large_valid_number(self) -> None:
        """Test validation of large but valid number."""
        result = InputValidator.validate_number(1000)
        assert result == 1000

    def test_validate_negative_number_raises_error(self) -> None:
        """Test that negative numbers raise InvalidInputError."""
        with pytest.raises(InvalidInputError, match="negative"):
            InputValidator.validate_number(-1)

    def test_validate_negative_string_raises_error(self) -> None:
        """Test that negative string numbers raise InvalidInputError."""
        with pytest.raises(InvalidInputError, match="negative"):
            InputValidator.validate_number("-5")

    def test_validate_non_integer_string_raises_error(self) -> None:
        """Test that non-integer strings raise InvalidInputError."""
        with pytest.raises(InvalidInputError, match="not a valid integer"):
            InputValidator.validate_number("abc")

    def test_validate_float_string_raises_error(self) -> None:
        """Test that float strings raise InvalidInputError."""
        with pytest.raises(InvalidInputError, match="not a valid integer"):
            InputValidator.validate_number("3.14")

    def test_validate_empty_string_raises_error(self) -> None:
        """Test that empty string raises InvalidInputError."""
        with pytest.raises(InvalidInputError, match="cannot be empty"):
            InputValidator.validate_number("")

    def test_validate_whitespace_string_raises_error(self) -> None:
        """Test that whitespace-only string raises InvalidInputError."""
        with pytest.raises(InvalidInputError, match="cannot be empty"):
            InputValidator.validate_number("   ")

    def test_validate_number_with_whitespace(self) -> None:
        """Test validation handles whitespace correctly."""
        result = InputValidator.validate_number("  42  ")
        assert result == 42

    def test_validate_exceeds_max_limit(self) -> None:
        """Test that numbers exceeding max limit raise InvalidInputError."""
        with pytest.raises(InvalidInputError, match="exceeds maximum"):
            InputValidator.validate_number(InputValidator.MAX_FACTORIAL_INPUT + 1)

    def test_is_valid_range_positive(self) -> None:
        """Test is_valid_range with valid positive number."""
        assert InputValidator.is_valid_range(5) is True

    def test_is_valid_range_zero(self) -> None:
        """Test is_valid_range with zero."""
        assert InputValidator.is_valid_range(0) is True

    def test_is_valid_range_max_limit(self) -> None:
        """Test is_valid_range with maximum allowed value."""
        assert InputValidator.is_valid_range(InputValidator.MAX_FACTORIAL_INPUT) is True

    def test_is_valid_range_negative(self) -> None:
        """Test is_valid_range with negative number."""
        assert InputValidator.is_valid_range(-1) is False

    def test_is_valid_range_exceeds_max(self) -> None:
        """Test is_valid_range with number exceeding max."""
        assert (
            InputValidator.is_valid_range(InputValidator.MAX_FACTORIAL_INPUT + 1)
            is False
        )

    @pytest.mark.parametrize(
        "input_value,expected",
        [
            (0, 0),
            (1, 1),
            (5, 5),
            (100, 100),
            ("0", 0),
            ("1", 1),
            ("5", 5),
            ("100", 100),
        ],
    )
    def test_validate_number_parametrized(
        self, input_value: str | int, expected: int
    ) -> None:
        """Test validation with various valid inputs."""
        assert InputValidator.validate_number(input_value) == expected

    @pytest.mark.parametrize(
        "invalid_input",
        [
            "not_a_number",
            "12.34",
            "1e5",
            "infinity",
            "nan",
            "None",
            "True",
        ],
    )
    def test_validate_invalid_strings(self, invalid_input: str) -> None:
        """Test validation with various invalid string inputs."""
        with pytest.raises(InvalidInputError):
            InputValidator.validate_number(invalid_input)
