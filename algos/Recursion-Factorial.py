def factorial(n):
    """
    Returns the factorial of n using a simple recursive definition.
    """
    # Base case: factorial of 0 or 1 is 1
    if n <= 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    return n * factorial(n-1)


# Example usage:
if __name__ == "__main__":
    print("Factorial of 5:", factorial(5))
