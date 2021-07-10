"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""


# Return a list of divisors
def find_divisors_for(num):
    a = []
    for i in range(1, (num // 2) + 1):
        a.append(i) if num % i == 0 else None
    return a

# Find amicable numbers to an upper bound
def find_amicable_numbers(bound):
    amicable_numbers = []
    for a in range(bound + 1):
        # Skip if a is in the list since the method finds pairs
        if (a in amicable_numbers): continue
        b = sum(find_divisors_for(a))
        # d(a) = b && d(b) = a, where a ≠ b
        if sum(find_divisors_for(b)) == a and a != b:
            amicable_numbers += [a, b]
    # print(amicable_numbers)
    print(sum(amicable_numbers))

if __name__ == '__main__':
    find_amicable_numbers(10000)