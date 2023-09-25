def serial_sum(n, m=None):
    if m is None:
        return sum(range(1, n + 1))
    else:
        return sum(range(n, m + 1))

# Example usage:
result1 = serial_sum(4)  # Result: 10
result2 = serial_sum(2, 4)  # Result: 9

# Print the results
print(result1)
print(result2)
