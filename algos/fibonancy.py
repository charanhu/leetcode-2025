# Dynamic Programming & Memoization: Fibonacci

def fib_memo(n, memo=None):
    """
    Returns the nth Fibonacci number using top-down DP (memoization).
    """
    if memo is None:
        memo = {}  # Initialize memo dictionary if not provided
    
    # If we already have fib(n) calculated, return it
    if n in memo:
        return memo[n]
    
    # Base cases for n=0 and n=1
    if n < 2:
        memo[n] = n
        return n
    
    # Recursively compute fib(n-1) and fib(n-2), then sum
    result = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    
    # Store in memo for future lookups
    memo[n] = result
    return result


# Example usage:
if __name__ == "__main__":
    for i in range(6):
        print(f"Fib({i}) =", fib_memo(i))
