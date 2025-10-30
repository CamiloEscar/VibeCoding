# Factorial Calculator - Architecture Documentation

## Overview

The Factorial Calculator is a production-ready Python application designed to calculate factorials with comprehensive error handling, input validation, and an intuitive command-line interface. The project follows clean architecture principles and modern Python best practices.

## Architecture

### Layer Structure

```
┌─────────────────────────────────────┐
│         Presentation Layer          │
│              (CLI)                  │
├─────────────────────────────────────┤
│         Business Layer              │
│    (Core Calculator Logic)          │
├─────────────────────────────────────┤
│         Validation Layer            │
│      (Input Validator)              │
├─────────────────────────────────────┤
│         Exception Layer             │
│    (Custom Exceptions)              │
└─────────────────────────────────────┘
```

### Module Description

#### 1. Core Module (`core.py`)

**Purpose**: Contains the main factorial calculation logic.

**Classes**:
- `FactorialCalculator`: Main calculator class with memoization
- `FactorialCalculatorFactory`: Factory for creating calculator instances

**Key Features**:
- Iterative algorithm with overflow detection
- Memoization cache for performance
- Range calculation support
- Cache management utilities

**Design Patterns**:
- **Factory Pattern**: `FactorialCalculatorFactory` provides centralized instance creation
- **Singleton Pattern**: Optional singleton instance via factory

#### 2. Validator Module (`validator.py`)

**Purpose**: Provides comprehensive input validation.

**Classes**:
- `InputValidator`: Static validator with range checking

**Key Features**:
- Type validation (int/string)
- Range validation (0 to 10,000)
- Negative number detection
- Empty input handling
- Whitespace trimming

**Design Patterns**:
- **Strategy Pattern**: Encapsulates validation strategies

#### 3. CLI Module (`cli.py`)

**Purpose**: Command-line interface for user interaction.

**Classes**:
- `CLI`: Main CLI handler with argument parsing

**Modes**:
1. **Argument Mode**: `factorial 5`
2. **Interactive Mode**: `factorial --interactive`
3. **Range Mode**: `factorial --range 3 5`

**Design Patterns**:
- **Command Pattern**: Encapsulates CLI commands

#### 4. Exceptions Module (`exceptions.py`)

**Purpose**: Defines custom exception hierarchy.

**Classes**:
- `FactorialError`: Base exception
- `InvalidInputError`: Invalid input exception
- `OverflowError`: Overflow exception

**Hierarchy**:
```
Exception
└── FactorialError
    ├── InvalidInputError
    └── OverflowError
```

## Data Flow

### Argument Mode Flow

```
User Input → CLI.run()
           → CLI._handle_argument_mode()
           → FactorialCalculator.calculate()
           → InputValidator.validate_number()
           → Calculate (with cache check)
           → Return Result
           → Display to User
```

### Interactive Mode Flow

```
User → CLI.run()
     → CLI._handle_interactive_mode()
     → Loop:
         ├── Prompt User
         ├── FactorialCalculator.calculate()
         ├── Display Result
         └── Check Exit Condition
```

## Algorithm

### Factorial Calculation

```python
def calculate(n):
    # 1. Validate input
    n = InputValidator.validate_number(n)
    
    # 2. Check cache
    if n in cache:
        return cache[n]
    
    # 3. Calculate iteratively
    result = 1
    for i in range(2, n + 1):
        prev_result = result
        result *= i
        
        # 4. Overflow detection
        if result // i != prev_result:
            raise OverflowError
    
    # 5. Cache result
    cache[n] = result
    
    return result
```

### Time Complexity

- **First calculation**: O(n)
- **Cached calculation**: O(1)
- **Range calculation**: O(n × m) where n is range size, m is average number

### Space Complexity

- **Cache**: O(k) where k is number of unique calculations
- **Algorithm**: O(1) - iterative approach

## Performance Optimizations

1. **Memoization**: Cache stores previously calculated results
2. **Iterative Algorithm**: No recursion stack overhead
3. **Early Exit**: Cache check before calculation
4. **Overflow Detection**: Validates result integrity during calculation

## Security Considerations

1. **Input Validation**: All inputs validated before processing
2. **Range Limits**: Maximum input of 10,000 prevents resource exhaustion
3. **No eval()**: No dynamic code execution
4. **Type Safety**: Full type hints with MyPy validation
5. **Bandit Audit**: No security issues detected

## Error Handling

### Error Flow

```
Input Error → InputValidator.validate_number()
           → Raise InvalidInputError
           → CLI catches FactorialError
           → Display user-friendly message
```

### Exception Hierarchy Benefits

- Catch base `FactorialError` for all domain errors
- Specific handling for `InvalidInputError` vs `OverflowError`
- Clean error propagation

## Testing Strategy

### Test Coverage

- **Unit Tests**: Each module tested independently
- **Integration Tests**: End-to-end scenarios
- **Parametrized Tests**: Multiple input combinations
- **Edge Cases**: Negative numbers, zero, large numbers
- **Error Cases**: Invalid inputs, overflow scenarios

### Test Organization

```
tests/
├── conftest.py          # Fixtures
├── test_core.py         # Core logic tests
├── test_validator.py    # Validation tests
├── test_cli.py          # CLI tests
├── test_exceptions.py   # Exception tests
└── test_integration.py  # Integration tests
```

## Configuration Management

### pyproject.toml

Central configuration for:
- Package metadata
- Dependencies
- Tool configurations (Black, Ruff, MyPy, Pytest)
- Build system

### requirements.txt

Explicit dependency versions for reproducibility.

## CI/CD Pipeline

### Workflow Jobs

1. **Quality Checks**:
   - Black formatting
   - Ruff linting
   - MyPy type checking
   - Bandit security audit

2. **Tests**:
   - Multi-platform (Ubuntu, Windows, macOS)
   - Coverage reporting
   - Minimum 80% coverage enforcement

3. **Build**:
   - Package building
   - Distribution validation

4. **Documentation**:
   - pdoc API documentation generation
   - Artifact upload

5. **Integration**:
   - CLI installation verification
   - End-to-end testing

## Deployment

### Installation Methods

1. **Development**: `pip install -e .`
2. **Production**: `pip install factorial-calculator`
3. **From Source**: Clone + `pip install -r requirements.txt`

### Package Distribution

- Source distribution (.tar.gz)
- Wheel distribution (.whl)
- PyPI publishing via GitHub Actions

## Extensibility

### Adding New Features

1. **New Calculation Methods**:
   - Add method to `FactorialCalculator`
   - Add CLI command in `CLI` class
   - Add tests in `test_core.py`

2. **New Validators**:
   - Add static method to `InputValidator`
   - Add tests in `test_validator.py`

3. **New Output Formats**:
   - Add formatter class
   - Integrate with CLI
   - Add tests

### Extension Points

- Custom validators via `InputValidator`
- Alternative calculation strategies
- Multiple UI implementations (GUI, Web API)
- Custom caching strategies

## Best Practices Implemented

1. **Code Quality**:
   - PEP 8 compliance
   - Type hints (PEP 484)
   - Docstrings (PEP 257)

2. **Testing**:
   - High coverage (>80%)
   - Comprehensive test suite
   - Continuous integration

3. **Security**:
   - Input validation
   - Security audits
   - No unsafe operations

4. **Documentation**:
   - README with examples
   - API documentation
   - Architecture documentation
   - Changelog

5. **Version Control**:
   - Semantic versioning
   - Conventional commits
   - Git workflows

## Maintenance

### Code Quality Checks

```bash
# Format code
black factorial_calculator tests

# Lint code
ruff check factorial_calculator tests

# Type check
mypy factorial_calculator

# Security audit
bandit -r factorial_calculator

# Run tests
pytest
```

### Monitoring Coverage

```bash
# Generate coverage report
pytest --cov-report=html

# View report
open htmlcov/index.html
```

## Future Enhancements

1. **Performance**:
   - Parallel range calculations
   - Persistent cache (Redis, SQLite)
   - Stirling's approximation for large numbers

2. **Features**:
   - JSON/CSV output formats
   - Web API interface
   - Batch processing
   - Progress indicators for large calculations

3. **Usability**:
   - GUI interface
   - Shell completion
   - Configuration file support
   - Logging framework

## References

- [PEP 8 - Style Guide](https://pep8.org/)
- [PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [Design Patterns](https://refactoring.guru/design-patterns)
- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
