def f(n):
    # Ensure n is a positive integer by taking its absolute value
    n = abs(n)

    # Extract digits of n
    digits = [int(d) for d in str(n)]

    # Filter odd digits
    odd_digits = list(filter(lambda x: x % 2 != 0, digits))

    # Check if there are no odd digits
    if not odd_digits:
        return -1

    # Return the difference between the largest and smallest odd digits
    return max(odd_digits) - min(odd_digits)

# Examples
print(f(57392))  # Output: 6 (7 - 1)
print(f(24680))  # Output: -1 (no odd digits)
print(f(-13579)) # Output: 8 (9 - 1)
print(f(0))      # Output: -1 (no odd digits)

