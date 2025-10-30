"""Integration tests for the factorial calculator package."""

import pytest

from factorial_calculator import (
    FactorialCalculator,
    FactorialError,
    InvalidInputError,
    OverflowError,
)
from factorial_calculator.cli import CLI


class TestPackageIntegration:
    """Integration tests for the complete package."""

    def test_package_imports(self) -> None:
        """Test that package exports correct symbols."""
        assert FactorialCalculator is not None
        assert FactorialError is not None
        assert InvalidInputError is not None
        assert OverflowError is not None

    def test_end_to_end_calculation(self) -> None:
        """Test complete calculation flow."""
        calc = FactorialCalculator()
        result = calc.calculate(5)
        assert result == 120

    def test_end_to_end_with_validation_error(self) -> None:
        """Test complete flow with validation error."""
        calc = FactorialCalculator()
        with pytest.raises(InvalidInputError):
            calc.calculate(-5)

    def test_cli_integration(self) -> None:
        """Test CLI integration with core calculator."""
        cli = CLI()
        exit_code = cli.run(["10"])
        assert exit_code == 0

    def test_multiple_calculations_with_cache(self) -> None:
        """Test multiple calculations using cache."""
        calc = FactorialCalculator()

        # First calculation
        result1 = calc.calculate(10)
        cache_size1 = calc.get_cache_size()

        # Second calculation (should use cache)
        result2 = calc.calculate(10)
        cache_size2 = calc.get_cache_size()

        assert result1 == result2
        assert cache_size1 == cache_size2

    def test_range_calculation_integration(self) -> None:
        """Test range calculation integration."""
        calc = FactorialCalculator()
        results = calc.calculate_range(1, 5)

        assert len(results) == 5
        assert results[1] == 1
        assert results[5] == 120

    def test_exception_hierarchy(self) -> None:
        """Test exception hierarchy."""
        try:
            raise InvalidInputError("test")
        except FactorialError:
            pass  # Should catch as base exception

        try:
            raise OverflowError("test")
        except FactorialError:
            pass  # Should catch as base exception

    def test_real_world_scenario_small_numbers(self) -> None:
        """Test real-world scenario with small numbers."""
        calc = FactorialCalculator()

        # Common small factorial calculations
        assert calc.calculate(0) == 1
        assert calc.calculate(1) == 1
        assert calc.calculate(2) == 2
        assert calc.calculate(3) == 6
        assert calc.calculate(4) == 24
        assert calc.calculate(5) == 120

    def test_real_world_scenario_medium_numbers(self) -> None:
        """Test real-world scenario with medium numbers."""
        calc = FactorialCalculator()

        # Medium factorial calculations
        assert calc.calculate(10) == 3628800
        assert calc.calculate(15) == 1307674368000

    def test_real_world_scenario_string_inputs(self) -> None:
        """Test real-world scenario with string inputs."""
        calc = FactorialCalculator()

        # String inputs (common from CLI)
        assert calc.calculate("5") == 120
        assert calc.calculate("10") == 3628800

    def test_performance_multiple_calculations(self) -> None:
        """Test performance with multiple calculations."""
        calc = FactorialCalculator()

        # Calculate multiple factorials
        for i in range(50):
            result = calc.calculate(i)
            assert result > 0

        # Verify cache is working (50 calculations + base cases 0 and 1)
        assert calc.get_cache_size() >= 50
