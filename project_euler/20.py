"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!"""

# Factorial method
def factorial(num):
    return num * factorial(num - 1) if num > 1 else 1

# Return the sum of each character in the factorial string
def sum_of_factorial_digits(num):
    return sum([int(ch) for ch in str(factorial(num))])

if __name__ == '__main__':
    print(sum_of_factorial_digits(100))