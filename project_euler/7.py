"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

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

def prime_index(target_index):
    cur_index = 0
    num = 2
    while cur_index < target_index:
        if is_prime(num):
            cur_index += 1
        if cur_index == target_index:
            print(num)
        num += 1

        

if __name__ == '__main__':
    prime_index(10001)