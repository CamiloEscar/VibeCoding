# Factorial Calculator

[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Linting: ruff](https://img.shields.io/badge/linting-ruff-red.svg)](https://github.com/charliermarsh/ruff)

A robust, production-ready Python package for calculating factorials with comprehensive error handling, input validation, and an intuitive command-line interface.

## Features

- ✨ **Clean Architecture**: Separation of concerns with modular design
- 🚀 **High Performance**: Optimized iterative algorithm with memoization
- 🛡️ **Robust Error Handling**: Comprehensive exception management
- 📝 **Type Hints**: Full MyPy type checking support
- 🧪 **High Test Coverage**: >80% code coverage with PyTest
- 🔒 **Security Audited**: Validated with Bandit security scanner
- 📚 **Well Documented**: Follows PEP 257 docstring conventions
- 🎨 **Code Quality**: PEP 8 compliant with Black and Ruff formatting

## Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/yourusername/VibeCoding.git
cd VibeCoding

# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

### Using pip (when published)

```bash
pip install factorial-calculator
```

## Quick Start

### Command Line Interface

#### Calculate a single factorial

```bash
# Using argument
factorial 5
# Output: The factorial of 5 is: 120

# Interactive mode
factorial --interactive
# Enter a number: 5
# Result: 5! = 120
```

#### Calculate a range of factorials

```bash
factorial --range 3 5
# Output:
# Factorials from 3 to 5:
#   3! = 6
#   4! = 24
#   5! = 120
```

### Python API

```python
from factorial_calculator import FactorialCalculator

# Create calculator instance
calc = FactorialCalculator()

# Calculate factorial
result = calc.calculate(5)
print(f"5! = {result}")  # Output: 5! = 120

# Calculate range
results = calc.calculate_range(3, 5)
print(results)  # Output: {3: 6, 4: 24, 5: 120}

# Using factory pattern
from factorial_calculator.core import FactorialCalculatorFactory

calc = FactorialCalculatorFactory.get_calculator()
result = calc.calculate(10)
```

## Usage Examples

### Input Validation

```python
from factorial_calculator import FactorialCalculator, InvalidInputError

calc = FactorialCalculator()

try:
    result = calc.calculate(-5)
except InvalidInputError as e:
    print(f"Error: {e}")
    # Output: Error: Invalid input: -5 is negative...
```

### Working with Cache

```python
calc = FactorialCalculator()

# First calculation
result1 = calc.calculate(100)
print(f"Cache size: {calc.get_cache_size()}")

# Cached calculation (faster)
result2 = calc.calculate(100)

# Clear cache if needed
calc.clear_cache()
```

## Development

### Setup Development Environment

```bash
# Install development dependencies
pip install -r requirements.txt

# Or install with optional dev dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests with coverage
pytest

# Run specific test file
pytest tests/test_core.py

# Run with verbose output
pytest -v

# Generate HTML coverage report
pytest --cov-report=html
```

### Code Quality Checks

```bash
# Format code with Black
black factorial_calculator tests

# Lint with Ruff
ruff check factorial_calculator tests

# Type checking with MyPy
mypy factorial_calculator

# Security audit with Bandit
bandit -r factorial_calculator
```

### Building Documentation

```bash
# Generate documentation with pdoc
pdoc factorial_calculator -o docs/html

# Or view in browser
pdoc factorial_calculator
```

## Project Structure

```
VibeCoding/
├── factorial_calculator/      # Main package
│   ├── __init__.py            # Package initialization
│   ├── core.py                # Core factorial logic
│   ├── cli.py                 # Command-line interface
│   ├── validator.py           # Input validation
│   └── exceptions.py          # Custom exceptions
├── tests/                     # Test suite
│   ├── conftest.py            # PyTest configuration
│   ├── test_core.py           # Core tests
│   ├── test_cli.py            # CLI tests
│   ├── test_validator.py     # Validator tests
│   ├── test_exceptions.py    # Exception tests
│   └── test_integration.py   # Integration tests
├── docs/                      # Documentation
├── .github/                   # GitHub configuration
│   └── workflows/             # CI/CD workflows
├── pyproject.toml             # Project configuration
├── setup.py                   # Setup script
├── requirements.txt           # Dependencies
├── LICENSE                    # MIT License
├── README.md                  # This file
├── CHANGELOG.md               # Version history
└── .gitignore                 # Git ignore rules
```

## Architecture

The project follows clean architecture principles with clear separation of concerns:

- **Core Module**: Contains the main business logic for factorial calculation
- **Validator Module**: Handles input validation and constraints
- **CLI Module**: Manages user interaction through command-line interface
- **Exceptions Module**: Defines custom exception hierarchy

### Design Patterns Used

- **Factory Pattern**: `FactorialCalculatorFactory` for instance creation
- **Strategy Pattern**: `InputValidator` for validation strategies
- **Singleton Pattern**: Optional singleton calculator instance
- **Command Pattern**: CLI command handling

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes following the code style guidelines
4. Run tests and ensure >80% coverage (`pytest`)
5. Run code quality checks (black, ruff, mypy, bandit)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Requirements

- Python 3.12 or higher
- See [requirements.txt](requirements.txt) for package dependencies

## Credits

Developed by **VibeCoding** for ING2 course - GitHub Copilot experimentation.

## Support

For issues, questions, or contributions, please visit the [GitHub repository](https://github.com/yourusername/VibeCoding).

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and changes.
