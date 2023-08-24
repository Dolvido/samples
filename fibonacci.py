def fibonacci(n):
    """
    Return the nth number in the Fibonacci sequence.

    The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones.
    It starts from 0 and 1. For example: 0, 1, 1, 2, 3, 5, 8, ...

    Parameters:
    - n (int): The position in the Fibonacci sequence.

    Returns:
    - int: The nth number in the Fibonacci sequence.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test the function
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci(i)}")

# Expected Output:
# Fibonacci(0) = 0
# Fibonacci(1) = 1
# Fibonacci(2) = 1
# Fibonacci(3) = 2
# Fibonacci(4) = 3
# Fibonacci(5) = 5
# Fibonacci(6) = 8
# Fibonacci(7) = 13
# Fibonacci(8) = 21
# Fibonacci(9) = 34
