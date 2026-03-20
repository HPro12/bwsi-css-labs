"""
tests_1b.py

This module contains unit tests for the simple_calculator function defined in lab_1b.py.
"""

import pytest
from labs.lab_1.lab_1b import simple_calculator

def test_addition():
    assert simple_calculator("add", 5, 3) == 8                  # Test for positive numbers
    assert simple_calculator("add", -2, 2) == 0                 # Test for negative and positive number
    assert simple_calculator("add", 0, 0) == 0                  # Test for zero addition
    assert simple_calculator("add", -2, -2) == -4               # Test for negative numbers
    assert simple_calculator("add", 1e6, 1e6) == 2e6            # Test for large numbers
    assert simple_calculator("add", 1e-6, 1e-6) == 2e-6         # Test for small numbers
    assert simple_calculator("add", 2.5, 1.5) == 4.0            # Test for decimal numbers
    assert isinstance(simple_calculator("add", 5.0, 3), float)  # Test for type consistency

def test_subtraction():
    assert simple_calculator("subtract", 5, 3) == 2             # Test for positive numbers
    assert simple_calculator("subtract", -2, -2) == 0           # Test for negative numbers
    assert simple_calculator("subtract", 0, 5) == -5            # Test for zero minuend
    assert simple_calculator("subtract", 5, 0) == 5             # Test for zero subtrahend
    assert simple_calculator("subtract", 3.0, 1.5) == 1.5       # Test for decimal numbers
    assert simple_calculator("subtract", -5, -10) == 5          # Test for negative subtraction
    assert simple_calculator("subtract", 1e6, 1) == 999999      # Test for large numbers

def test_multiplication():
    assert simple_calculator("multiply", 5, 3) == 15            # Test for positive numbers
    assert simple_calculator("multiply", -2, 2) == -4           # Test for negative and positive number
    assert simple_calculator("multiply", 0, 100) == 0           # Test for multiplication by zero
    assert simple_calculator("multiply", -5, -3) == 15          # Test for negative numbers
    assert simple_calculator("multiply", 2.5, 2) == 5.0         # Test for decimal numbers
    assert simple_calculator("multiply", 1e6, 1e6) == 1e12      # Test for large numbers
    assert simple_calculator("multiply", 1e-6, 1e-6) == 1e-12   # Test for small numbers
    assert simple_calculator("multiply", -0.5, -2) == 1.0       # Test for negative decimal numbers

def test_division():
    assert simple_calculator("divide", 6, 3) == 2               # Test for positive numbers
    assert simple_calculator("divide", -4, 2) == -2             # Test for negative and positive number
    assert simple_calculator("divide", 5, 2) == 2.5             # Test for division resulting in float
    assert simple_calculator("divide", 3, 1.5) == 2.0           # Test for decimal numbers
    assert simple_calculator("divide", -6, -3) == 2             # Test for negative numbers
    assert simple_calculator("divide", 0, 3) == 0               # Test for zero numerator
    assert simple_calculator("divide", 1, 3) == 1/3             # Test for recurring decimal
    assert simple_calculator("divide", 2.5, 0.5) == 5.0         # Test for decimal numbesr
    assert simple_calculator("divide", 1e12, 1e6) == 1e6        # Test for large numbers
    assert simple_calculator("divide", 1e-12, 1e-6) == 1e-6     # Test for small numbers

def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        simple_calculator("divide", 5, 0)                       # Test division by zero for a positive number
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        simple_calculator("divide", -2, 0)                      # Test division by zero for a negative number
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        simple_calculator("divide", 0, 0)                      # Test division by zero for 0

def test_invalid_operation():
    with pytest.raises(ValueError, match="Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."):
        simple_calculator("modulus", 5, 3)              # Test for invalid operation
    with pytest.raises(ValueError, match="Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."):
        simple_calculator("", 5, 3)                     # Test for empty operation

if __name__ == "__main__":
    pytest.main()