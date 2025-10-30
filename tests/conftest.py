"""Test configuration and fixtures for pytest."""

import pytest

from factorial_calculator.core import FactorialCalculator


@pytest.fixture
def calculator() -> FactorialCalculator:
    """
    Fixture that provides a fresh FactorialCalculator instance.

    Returns:
        FactorialCalculator: A new calculator instance.
    """
    return FactorialCalculator()


@pytest.fixture
def calculator_with_cache() -> FactorialCalculator:
    """
    Fixture that provides a calculator with pre-populated cache.

    Returns:
        FactorialCalculator: A calculator with cached values.
    """
    calc = FactorialCalculator()
    # Pre-populate cache
    calc.calculate(5)
    calc.calculate(10)
    return calc
