"""Unit tests for the core factorial calculator module."""

import pytest

from factorial_calculator.core import FactorialCalculator, FactorialCalculatorFactory
from factorial_calculator.exceptions import InvalidInputError


class TestFactorialCalculator:
    """Test suite for FactorialCalculator class."""

    def test_factorial_zero(self, calculator: FactorialCalculator) -> None:
        """Test factorial of zero equals 1."""
        result = calculator.calculate(0)
        assert result == 1

    def test_factorial_one(self, calculator: FactorialCalculator) -> None:
        """Test factorial of one equals 1."""
        result = calculator.calculate(1)
        assert result == 1

    def test_factorial_small_numbers(self, calculator: FactorialCalculator) -> None:
        """Test factorial calculations for small numbers."""
        assert calculator.calculate(2) == 2
        assert calculator.calculate(3) == 6
        assert calculator.calculate(4) == 24
        assert calculator.calculate(5) == 120
        assert calculator.calculate(6) == 720

    def test_factorial_ten(self, calculator: FactorialCalculator) -> None:
        """Test factorial of 10."""
        result = calculator.calculate(10)
        assert result == 3628800

    def test_factorial_twenty(self, calculator: FactorialCalculator) -> None:
        """Test factorial of 20."""
        result = calculator.calculate(20)
        assert result == 2432902008176640000

    def test_factorial_string_input(self, calculator: FactorialCalculator) -> None:
        """Test factorial calculation with string input."""
        result = calculator.calculate("5")
        assert result == 120

    def test_factorial_negative_raises_error(
        self, calculator: FactorialCalculator
    ) -> None:
        """Test that negative input raises InvalidInputError."""
        with pytest.raises(InvalidInputError, match="negative"):
            calculator.calculate(-1)

    def test_factorial_invalid_string_raises_error(
        self, calculator: FactorialCalculator
    ) -> None:
        """Test that invalid string raises InvalidInputError."""
        with pytest.raises(InvalidInputError, match="not a valid integer"):
            calculator.calculate("invalid")

    def test_caching_mechanism(self, calculator: FactorialCalculator) -> None:
        """Test that caching works correctly."""
        # Calculate factorial
        result1 = calculator.calculate(10)

        # Check cache
        assert 10 in calculator._cache
        assert calculator._cache[10] == result1

        # Calculate again and verify it uses cache
        result2 = calculator.calculate(10)
        assert result1 == result2

    def test_cache_population(self, calculator: FactorialCalculator) -> None:
        """Test that cache is populated correctly."""
        initial_size = calculator.get_cache_size()
        calculator.calculate(5)
        assert calculator.get_cache_size() > initial_size

    def test_clear_cache(self, calculator_with_cache: FactorialCalculator) -> None:
        """Test cache clearing functionality."""
        assert calculator_with_cache.get_cache_size() > 2
        calculator_with_cache.clear_cache()
        assert calculator_with_cache.get_cache_size() == 2
        assert 0 in calculator_with_cache._cache
        assert 1 in calculator_with_cache._cache

    def test_get_cache_size(self, calculator: FactorialCalculator) -> None:
        """Test cache size retrieval."""
        initial_size = calculator.get_cache_size()
        calculator.calculate(5)
        calculator.calculate(10)
        assert calculator.get_cache_size() > initial_size

    def test_calculate_range_ascending(self, calculator: FactorialCalculator) -> None:
        """Test calculating factorial range in ascending order."""
        results = calculator.calculate_range(3, 5)
        assert results == {3: 6, 4: 24, 5: 120}

    def test_calculate_range_descending(self, calculator: FactorialCalculator) -> None:
        """Test calculating factorial range in descending order."""
        results = calculator.calculate_range(5, 3)
        assert results == {3: 6, 4: 24, 5: 120}

    def test_calculate_range_single_value(
        self, calculator: FactorialCalculator
    ) -> None:
        """Test calculating factorial range with single value."""
        results = calculator.calculate_range(4, 4)
        assert results == {4: 24}

    def test_calculate_range_invalid_input(
        self, calculator: FactorialCalculator
    ) -> None:
        """Test that invalid range raises InvalidInputError."""
        with pytest.raises(InvalidInputError):
            calculator.calculate_range(-1, 5)

    def test_very_large_factorial(self, calculator: FactorialCalculator) -> None:
        """Test calculation of large factorial."""
        result = calculator.calculate(100)
        # 100! is a very large number
        assert result > 10**150
        assert isinstance(result, int)

    @pytest.mark.parametrize(
        "n,expected",
        [
            (0, 1),
            (1, 1),
            (2, 2),
            (3, 6),
            (4, 24),
            (5, 120),
            (6, 720),
            (7, 5040),
        ],
    )
    def test_factorial_parametrized(
        self, calculator: FactorialCalculator, n: int, expected: int
    ) -> None:
        """Test factorial calculation with parametrized inputs."""
        assert calculator.calculate(n) == expected

    def test_factorial_large_number_performance(
        self, calculator: FactorialCalculator
    ) -> None:
        """Test that large factorial calculations complete reasonably."""
        # This should complete without timeout
        result = calculator.calculate(500)
        assert result > 0

    def test_sequential_calculations(self, calculator: FactorialCalculator) -> None:
        """Test multiple sequential calculations."""
        results = [calculator.calculate(i) for i in range(10)]
        assert len(results) == 10
        assert results[0] == 1  # 0!
        assert results[5] == 120  # 5!
        assert results[9] == 362880  # 9!


class TestFactorialCalculatorFactory:
    """Test suite for FactorialCalculatorFactory class."""

    def test_get_calculator_singleton(self) -> None:
        """Test that factory returns singleton instance."""
        calc1 = FactorialCalculatorFactory.get_calculator(use_singleton=True)
        calc2 = FactorialCalculatorFactory.get_calculator(use_singleton=True)
        assert calc1 is calc2

    def test_get_calculator_new_instance(self) -> None:
        """Test that factory can create new instances."""
        calc1 = FactorialCalculatorFactory.get_calculator(use_singleton=False)
        calc2 = FactorialCalculatorFactory.get_calculator(use_singleton=False)
        assert calc1 is not calc2

    def test_factory_returns_calculator_instance(self) -> None:
        """Test that factory returns FactorialCalculator instance."""
        calc = FactorialCalculatorFactory.get_calculator()
        assert isinstance(calc, FactorialCalculator)

    def test_factory_calculator_functionality(self) -> None:
        """Test that calculator from factory works correctly."""
        calc = FactorialCalculatorFactory.get_calculator(use_singleton=False)
        result = calc.calculate(5)
        assert result == 120
