"""
The sum of the squares of the first ten natural numbers is 385

The square of the sum of the first ten natural numbers is 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

def diff_of_squares(start, end):
    a = range(start, end+1)
    sum_of_squares = 0
    square_of_sums = 0
    for i in a:
        sum_of_squares += (i*i) # Add the square
        square_of_sums += i     # Add the sum
    square_of_sums **= 2        # Square the sums

    print(f"{square_of_sums} - {sum_of_squares} = {square_of_sums-sum_of_squares}")


if __name__ == '__main__':
    diff_of_squares(1, 100)