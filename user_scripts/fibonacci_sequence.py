python
def fibonacci_sequence(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Example usage
print(fibonacci_sequence(10))  # Prints [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
