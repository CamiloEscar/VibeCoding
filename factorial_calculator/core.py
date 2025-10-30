"""
Core factorial calculation module.

This module implements the main factorial calculation logic using
object-oriented design patterns and optimized algorithms.
"""


from factorial_calculator.exceptions import OverflowError
from factorial_calculator.validator import InputValidator


class FactorialCalculator:
    """
    Main calculator class for factorial operations.

    This class implements the Singleton pattern for caching and uses
    memoization for performance optimization. It provides robust
    factorial calculation with comprehensive error handling.

    Attributes:
        _cache: Dictionary storing previously calculated factorials.
    """

    def __init__(self) -> None:
        """Initialize the factorial calculator with an empty cache."""
        self._cache: dict[int, int] = {0: 1, 1: 1}

    def calculate(self, n: int | str) -> int:
        """
        Calculate the factorial of a given number.

        This method uses an iterative approach with memoization for
        optimal performance. The result is cached for future use.

        Args:
            n: A non-negative integer for which to calculate the factorial.

        Returns:
            int: The factorial of n (n!).

        Raises:
            InvalidInputError: If n is invalid or out of range.
            OverflowError: If calculation would cause overflow.

        Examples:
            >>> calc = FactorialCalculator()
            >>> calc.calculate(5)
            120
            >>> calc.calculate(0)
            1
        """
        # Validate input
        n = InputValidator.validate_number(n)

        # Check cache first
        if n in self._cache:
            return self._cache[n]

        # Calculate factorial iteratively with overflow detection
        try:
            result = 1
            for i in range(2, n + 1):
                prev_result = result
                result *= i

                # Check for potential overflow by verifying result integrity
                if result // i != prev_result:
                    raise OverflowError(
                        f"Factorial calculation for {n} would cause overflow"
                    )

            # Cache the result
            self._cache[n] = result
            return result

        except MemoryError as e:
            raise OverflowError(
                f"Factorial calculation for {n} exceeded memory limits"
            ) from e

    def calculate_range(self, start: int | str, end: int | str) -> dict[int, int]:
        """
        Calculate factorials for a range of numbers.

        Args:
            start: Starting number (inclusive).
            end: Ending number (inclusive).

        Returns:
            Dict[int, int]: Dictionary mapping numbers to their factorials.

        Raises:
            InvalidInputError: If range is invalid.

        Examples:
            >>> calc = FactorialCalculator()
            >>> calc.calculate_range(3, 5)
            {3: 6, 4: 24, 5: 120}
        """
        start = InputValidator.validate_number(start)
        end = InputValidator.validate_number(end)

        if start > end:
            start, end = end, start

        results = {}
        for i in range(start, end + 1):
            results[i] = self.calculate(i)

        return results

    def clear_cache(self) -> None:
        """
        Clear the calculation cache.

        This method resets the cache to its initial state, keeping only
        the base cases (0! = 1, 1! = 1).
        """
        self._cache = {0: 1, 1: 1}

    def get_cache_size(self) -> int:
        """
        Get the current size of the calculation cache.

        Returns:
            int: Number of cached factorial results.
        """
        return len(self._cache)


class FactorialCalculatorFactory:
    """
    Factory class for creating FactorialCalculator instances.

    This class implements the Factory pattern to provide a centralized
    way to create calculator instances.
    """

    _instance: FactorialCalculator | None = None

    @classmethod
    def get_calculator(cls, use_singleton: bool = True) -> FactorialCalculator:
        """
        Get a FactorialCalculator instance.

        Args:
            use_singleton: If True, returns a singleton instance.
                          If False, creates a new instance.

        Returns:
            FactorialCalculator: A calculator instance.

        Examples:
            >>> calc = FactorialCalculatorFactory.get_calculator()
            >>> calc.calculate(5)
            120
        """
        if use_singleton:
            if cls._instance is None:
                cls._instance = FactorialCalculator()
            return cls._instance
        else:
            return FactorialCalculator()
