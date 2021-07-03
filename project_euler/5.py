"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

# Greatest common denominator
def gcd(a, b):
    # Euclidean algorithm go zoom
    return a if b == 0 else gcd(b, a % b)

# Least common multiple
def lcm(a, b):
    return (a * b) // gcd(a, b)

# Find the smallest multiple all values divide into evenly
def smallest_mult(min_val, max_val):
    mults = range(min_val, max_val+1)
    multiple = min_val
    for n in mults:
        multiple = lcm(multiple, n)
    return multiple

if __name__ == '__main__':
    print(smallest_mult(1, 20))
