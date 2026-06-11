"""Calculator feature logic.

This module contains the pure business logic for mathematical operations.
It is completely decoupled from any specific interface (REST or MCP).
"""

def multiply(a: float, b: float) -> float:
    """Multiplies two numbers.

    Args:
        a: The first multiplier.
        b: The second multiplier.

    Returns:
        The product of a and b.
    """
    return a * b

def add_numbers(x: float, y: float) -> float:
    """Adds two numbers.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The sum of x and y.
    """
    return x + y

def subtract(a: float, b: float) -> float:
    """Subtracts the second number from the first.

    Args:
        a: The number to subtract from.
        b: The number to subtract.

    Returns:
        The difference of a and b.
    """
    return a - b

def divide(a: float, b: float) -> float:
    """Divides the first number by the second.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The quotient.

    Raises:
        ValueError: If the divisor is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
