"""Calculator module that provides basic arithmetic operations."""

class Calculator:
    """Represents a calculator that can perform division."""

    def __init__(self, name):
        """
        Initialize the Calculator with a name.

        Args:
            name (str): The name of the calculator instance.
        """
        self.name = name

    def divide(self, a, b):
        """
        Divides two numbers and returns the result.

        Args:
            a (float): Dividend.
            b (float): Divisor.

        Returns:
            float: Result of the division.

        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


def generate_numbers(n):
    """
    Generate numbers from 0 to n-1.

    Args:
        n (int): Number of values to generate.

    Yields:
        int: The next number in the sequence.
    """
    for i in range(n):
        yield i
