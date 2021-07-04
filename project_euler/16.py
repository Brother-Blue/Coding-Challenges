"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?"""

# Return the sum of digits from 2^n
def sum_of_digits_power_of(n):
    s = str(2**n)
    retval = 0
    for i in range(len(s)):
        retval += int(s[i])
    print(retval)

if __name__ == '__main__':
    sum_of_digits_power_of(1000)