"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

# Determine if an input is a palindrome
def is_palindrome(num):
    s = str(num)
    for i in range(0, (len(s) // 2)):
        # s[-i-1] the -1 is needed as s[0] is the opposite end of s[-1]
        if s[i] != s[-i-1]:
            return False
    return True

# Pass in the amount of digits
def palindrome_product(digits):
    largest_found = 0
    a = int("9" * digits)               # 999, 9_999, 99_999, ...
    b = int("1" + "0" * (digits-1))     # 100, 1_000, 10_000, ...
    for i in range(a, b, -1):
        for j in range(a, b, -1):
            if is_palindrome(i * j):
                largest_found = max(largest_found, i*j) # New largest is max between current and new found palindrome

    print(largest_found)

if __name__ == '__main__':
    palindrome_product(3)
