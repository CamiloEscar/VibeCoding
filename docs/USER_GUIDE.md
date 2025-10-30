# Factorial Calculator - User Guide

## Introduction

The Factorial Calculator is a command-line application for calculating factorials of non-negative integers. It provides multiple modes of operation to suit different use cases.

## What is a Factorial?

The factorial of a non-negative integer n, denoted as n!, is the product of all positive integers less than or equal to n.

**Formula**: n! = n × (n-1) × (n-2) × ... × 2 × 1

**Special Cases**:
- 0! = 1 (by definition)
- 1! = 1

**Examples**:
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- 10! = 3,628,800

## Installation

### Requirements

- Python 3.12 or higher

### Installation Steps

1. **Clone or download the project**:
   ```bash
   git clone https://github.com/yourusername/VibeCoding.git
   cd VibeCoding
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install the package**:
   ```bash
   pip install -e .
   ```

4. **Verify installation**:
   ```bash
   factorial --version
   ```

## Usage Modes

### 1. Argument Mode

Calculate a single factorial by providing a number as an argument.

**Syntax**:
```bash
factorial <number>
```

**Examples**:
```bash
# Calculate 5!
factorial 5
# Output: The factorial of 5 is: 120

# Calculate 10!
factorial 10
# Output: The factorial of 10 is: 3628800

# Calculate 0!
factorial 0
# Output: The factorial of 0 is: 1
```

### 2. Interactive Mode

Enter an interactive session for calculating multiple factorials.

**Syntax**:
```bash
factorial --interactive
# or
factorial -i
```

**Example Session**:
```
$ factorial --interactive
=== Factorial Calculator (Interactive Mode) ===
Enter a non-negative integer to calculate its factorial.
Type 'quit' or 'exit' to leave.

Enter a number: 5
Result: 5! = 120

Enter a number: 10
Result: 10! = 3628800

Enter a number: 0
Result: 0! = 1

Enter a number: quit
Goodbye!
```

**Interactive Commands**:
- Enter any non-negative integer to calculate
- Type `quit`, `exit`, or `q` to exit
- Press `Ctrl+C` to cancel
- Press `Ctrl+D` (Unix) or `Ctrl+Z` (Windows) for EOF exit

### 3. Range Mode

Calculate factorials for a range of numbers.

**Syntax**:
```bash
factorial --range <start> <end>
# or
factorial -r <start> <end>
```

**Examples**:
```bash
# Calculate factorials from 3 to 5
factorial --range 3 5
# Output:
# Factorials from 3 to 5:
#   3! = 6
#   4! = 24
#   5! = 120

# Calculate factorials from 1 to 10
factorial -r 1 10
# Output:
# Factorials from 1 to 10:
#   1! = 1
#   2! = 2
#   3! = 6
#   4! = 24
#   5! = 120
#   6! = 720
#   7! = 5040
#   8! = 40320
#   9! = 362880
#   10! = 3628800
```

**Note**: The order of start and end doesn't matter; the calculator will automatically sort them.

## Valid Input

### Acceptable Values

- **Type**: Non-negative integers
- **Range**: 0 to 10,000
- **Format**: 
  - Plain numbers: `5`, `100`, `1000`
  - String numbers: `"5"`, `"100"` (quotes optional in command line)

### Invalid Inputs

The following inputs will produce an error:

1. **Negative numbers**:
   ```bash
   factorial -5
   # Error: Invalid input: -5 is negative...
   ```

2. **Non-integers**:
   ```bash
   factorial 3.14
   # Error: Invalid input: '3.14' is not a valid integer
   ```

3. **Non-numeric strings**:
   ```bash
   factorial abc
   # Error: Invalid input: 'abc' is not a valid integer
   ```

4. **Empty input** (interactive mode):
   ```bash
   Enter a number: 
   # Please enter a value.
   ```

5. **Numbers exceeding limit**:
   ```bash
   factorial 100000
   # Error: Invalid input: 100000 exceeds maximum allowed value of 10000
   ```

## Common Use Cases

### 1. Quick Calculation

When you need a single factorial value quickly:
```bash
factorial 12
```

### 2. Multiple Related Calculations

When you need to calculate several factorials:
```bash
factorial --interactive
```
Then enter your numbers one by one.

### 3. Generating a Table

When you need factorial values for a sequence:
```bash
factorial --range 1 20
```
You can redirect output to a file:
```bash
factorial --range 1 20 > factorials.txt
```

### 4. Checking Specific Values

For verification or testing:
```bash
factorial 5
factorial 10
factorial 20
```

## Tips and Tricks

### 1. Performance

The calculator uses caching, so repeated calculations are instant:
```bash
factorial 100    # First time: calculates
factorial 100    # Second time: instant (cached)
```

### 2. Large Numbers

Python handles arbitrarily large integers, so you can calculate very large factorials:
```bash
factorial 100
# Returns a 158-digit number!
```

### 3. Piping and Redirection

Combine with other command-line tools:
```bash
# Save output to file
factorial 20 > result.txt

# Use in scripts
result=$(factorial 5)
echo "5! = $result"
```

### 4. Batch Processing

Create a script to process multiple values:
```bash
#!/bin/bash
for i in {1..10}; do
    factorial $i
done
```

## Error Handling

### Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| "negative" | Negative number | Use non-negative integer |
| "not a valid integer" | Non-integer input | Enter whole number |
| "cannot be empty" | Empty input | Enter a value |
| "exceeds maximum" | Number > 10,000 | Use smaller number |

### Exit Codes

- `0`: Success
- `1`: Error (invalid input, calculation error)

## Examples by Use Case

### Mathematical Exploration
```bash
# Compare growth
factorial --range 1 10
```

### Programming/Testing
```bash
# Test edge cases
factorial 0
factorial 1
factorial 2
```

### Research/Analysis
```bash
# Generate data for analysis
factorial --range 10 20 > data.txt
```

### Interactive Learning
```bash
# Learn about factorials
factorial --interactive
```

## Keyboard Shortcuts

### Interactive Mode

- `Enter`: Submit input
- `Ctrl+C`: Cancel/Exit
- `Ctrl+D` (Unix) / `Ctrl+Z` (Windows): EOF exit
- Backspace: Delete character

### Command Line

- `↑` / `↓`: Navigate command history
- `Tab`: Auto-completion (if configured)

## Troubleshooting

### Problem: Command not found

**Symptom**: `factorial: command not found`

**Solutions**:
1. Ensure package is installed: `pip install -e .`
2. Check Python scripts directory in PATH
3. Use full path: `python -m factorial_calculator.cli`

### Problem: Import errors

**Symptom**: `ModuleNotFoundError`

**Solutions**:
1. Verify installation: `pip list | grep factorial`
2. Reinstall: `pip install -e . --force-reinstall`
3. Check Python version: `python --version` (must be 3.12+)

### Problem: Slow performance

**Symptom**: Calculation takes long time

**Possible causes**:
- Very large number (1000+)
- First calculation (not cached)

**Solutions**:
- Use smaller numbers if possible
- Subsequent calculations will be faster (cached)

## Python API

You can also use the calculator in your Python code:

```python
from factorial_calculator import FactorialCalculator

# Create calculator
calc = FactorialCalculator()

# Calculate single factorial
result = calc.calculate(5)
print(f"5! = {result}")  # Output: 5! = 120

# Calculate range
results = calc.calculate_range(1, 5)
for n, factorial in results.items():
    print(f"{n}! = {factorial}")

# Clear cache if needed
calc.clear_cache()

# Check cache size
size = calc.get_cache_size()
print(f"Cache contains {size} entries")
```

### Error Handling in Python

```python
from factorial_calculator import (
    FactorialCalculator,
    InvalidInputError,
    OverflowError
)

calc = FactorialCalculator()

try:
    result = calc.calculate(-5)
except InvalidInputError as e:
    print(f"Invalid input: {e}")
except OverflowError as e:
    print(f"Overflow: {e}")
```

## Getting Help

### Command Line Help

```bash
# Show help message
factorial --help
factorial -h

# Show version
factorial --version
factorial -v
```

### Documentation

- **User Guide**: `docs/USER_GUIDE.md` (this file)
- **README**: `README.md` - Quick start guide
- **Architecture**: `docs/ARCHITECTURE.md` - Technical details
- **API Documentation**: `docs/html/index.html` - Generated API docs

### Support

For issues, questions, or contributions:
- GitHub Issues: [repository issues page]
- GitHub Discussions: [repository discussions page]

## FAQ

**Q: What's the maximum number I can calculate?**  
A: The maximum input is 10,000, but results for very large numbers (1000+) may take time to display due to their size.

**Q: Why is there a maximum limit?**  
A: To prevent accidental resource exhaustion and maintain reasonable performance.

**Q: Can I calculate factorials of negative numbers?**  
A: No, factorials are only defined for non-negative integers (0, 1, 2, 3, ...).

**Q: Can I calculate factorials of decimals?**  
A: No, this calculator only works with integers. For gamma functions (generalization to real numbers), use a mathematical library.

**Q: Why is 0! = 1?**  
A: By mathematical convention and definition. It makes many mathematical formulas work consistently.

**Q: Is my data cached?**  
A: Yes, within a single calculator instance. The cache is cleared when the program exits.

**Q: Can I use this in my project?**  
A: Yes! This project is licensed under MIT License. See LICENSE file for details.

## Quick Reference

### Commands
```bash
factorial <number>              # Calculate single factorial
factorial -i                    # Interactive mode
factorial -r <start> <end>      # Range calculation
factorial -h                    # Show help
factorial -v                    # Show version
```

### Valid Input Range
- Minimum: 0
- Maximum: 10,000

### Exit Commands (Interactive Mode)
- `quit`
- `exit`
- `q`
- Ctrl+C
- Ctrl+D (Unix) / Ctrl+Z (Windows)

---

**Version**: 1.0.0  
**Last Updated**: 2025-01-29  
**License**: MIT
