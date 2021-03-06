"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?"""

# Gets the amount of divisors of a number
def get_divisors(number):
    num_divisors = 0
    for i in range(1, int(number**0.5)+1):
        if number % i == 0:
            num_divisors += 1
    num_divisors *= 2
    if num_divisors % 2 == 1:
        num_divisors += 1
    return num_divisors

# Creates a triangular number https://en.wikipedia.org/wiki/Triangular_number
def create_triangular_number(num):
    if num < 1: return 0
    return (num * (num + 1)) // 2

# Target is the number of divisors
def find_with_divisors(target):
    cur = 1
    tri_num = create_triangular_number(cur)
    divisors = get_divisors(tri_num)
    while True:
        if divisors < target:
            cur += 1
            tri_num = create_triangular_number(cur)
            divisors = get_divisors(tri_num)
        else:
            print(f"Number: {tri_num} | Divisors: {divisors}")
            return

if __name__ == '__main__':
    find_with_divisors(500)