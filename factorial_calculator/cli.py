"""
Command-line interface for the factorial calculator.

This module provides a CLI for interactive and argument-based
factorial calculation.
"""

import argparse
import sys
from typing import NoReturn

from factorial_calculator.core import FactorialCalculatorFactory
from factorial_calculator.exceptions import FactorialError


class CLI:
    """
    Command-line interface handler for factorial calculator.

    This class implements the Command pattern to handle user interactions
    through command-line arguments or interactive input.
    """

    def __init__(self) -> None:
        """Initialize the CLI with a calculator instance."""
        self.calculator = FactorialCalculatorFactory.get_calculator()
        self.parser = self._create_parser()

    def _create_parser(self) -> argparse.ArgumentParser:
        """
        Create and configure the argument parser.

        Returns:
            argparse.ArgumentParser: Configured argument parser.
        """
        parser = argparse.ArgumentParser(
            description="Calculate factorial of a given number",
            epilog="Example: factorial 5  or  factorial --interactive",
        )

        parser.add_argument(
            "number",
            type=str,
            nargs="?",
            help="Number to calculate factorial (non-negative integer)",
        )

        parser.add_argument(
            "-i",
            "--interactive",
            action="store_true",
            help="Run in interactive mode (prompt for input)",
        )

        parser.add_argument(
            "-v", "--version", action="version", version="factorial-calculator 1.0.0"
        )

        parser.add_argument(
            "-r",
            "--range",
            nargs=2,
            type=str,
            metavar=("START", "END"),
            help="Calculate factorials for a range of numbers",
        )

        return parser

    def run(self, args: list | None = None) -> int:
        """
        Run the CLI application.

        Args:
            args: Command-line arguments (None for sys.argv).

        Returns:
            int: Exit code (0 for success, 1 for error).
        """
        try:
            parsed_args = self.parser.parse_args(args)

            # Handle range mode
            if parsed_args.range:
                return self._handle_range_mode(
                    parsed_args.range[0], parsed_args.range[1]
                )

            # Handle interactive mode
            if parsed_args.interactive:
                return self._handle_interactive_mode()

            # Handle argument mode
            if parsed_args.number:
                return self._handle_argument_mode(parsed_args.number)

            # No arguments provided, show help
            self.parser.print_help()
            return 0

        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            return 1
        except Exception as e:
            print(f"Unexpected error: {e}", file=sys.stderr)
            return 1

    def _handle_argument_mode(self, number: str) -> int:
        """
        Handle calculation when number is provided as argument.

        Args:
            number: The number string to calculate factorial for.

        Returns:
            int: Exit code.
        """
        try:
            result = self.calculator.calculate(number)
            print(f"The factorial of {number} is: {result}")
            return 0
        except FactorialError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1

    def _handle_interactive_mode(self) -> int:
        """
        Handle interactive mode where user is prompted for input.

        Returns:
            int: Exit code.
        """
        print("=== Factorial Calculator (Interactive Mode) ===")
        print("Enter a non-negative integer to calculate its factorial.")
        print("Type 'quit' or 'exit' to leave.\n")

        while True:
            try:
                user_input = input("Enter a number: ").strip()

                if user_input.lower() in ("quit", "exit", "q"):
                    print("Goodbye!")
                    return 0

                if not user_input:
                    print("Please enter a value.\n")
                    continue

                result = self.calculator.calculate(user_input)
                print(f"Result: {user_input}! = {result}\n")

            except FactorialError as e:
                print(f"Error: {e}\n", file=sys.stderr)
            except EOFError:
                print("\nGoodbye!")
                return 0

    def _handle_range_mode(self, start: str, end: str) -> int:
        """
        Handle calculation for a range of numbers.

        Args:
            start: Starting number.
            end: Ending number.

        Returns:
            int: Exit code.
        """
        try:
            results = self.calculator.calculate_range(start, end)
            print(f"Factorials from {start} to {end}:")
            for num, factorial in sorted(results.items()):
                print(f"  {num}! = {factorial}")
            return 0
        except FactorialError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1


def main() -> NoReturn:
    """
    Entry point for the factorial calculator CLI.

    This function is called when the package is executed as a script.
    """
    cli = CLI()
    exit_code = cli.run()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
