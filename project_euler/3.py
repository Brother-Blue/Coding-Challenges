"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

import math

# Checks if a number is considered prime
def is_prime(num):
    for i in range(2, math.floor(math.sqrt(num))):
        if num % i == 0:
            return False
    return True

# Iterates through [3-n]
def find_largest_prime_factor(num):
    upper_val = math.floor(math.sqrt(num))
    prime_val = 0
    for i in range(3, upper_val): # Ignore pseudo-primes (1, 2)
        if is_prime(i) and num % i == 0: # Check for prime status and divisibility
            prime_val = i
    print(prime_val)

if __name__ == '__main__':
    find_largest_prime_factor(600851475143)