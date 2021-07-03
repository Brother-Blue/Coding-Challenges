""""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

# Checks if a number is considered prime
def is_prime(num):
    # Quick checks
    if num == 2 or num == 3: return True
    if num < 2 or num % 2 == 0: return False
    if num < 9: return True
    if num % 3 == 0: return False

    cur = 5
    end = int(num**0.5)
    while cur <= end:
        if num % cur == 0: return False
        if num % (cur+2) == 0: return False
        cur += 6
    return True 

# Sums all prime values up to a given max value
def sum_primes(max_val):
    retval = 0
    for i in range(2, max_val):
        if is_prime(i):
            retval += i
    print(retval)

if __name__ == '__main__':
    sum_primes(2_000_000)