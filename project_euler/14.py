"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""

# Returns the length of the collatz sequence of a given number
def chain_creator(num):
    sequence = 0
    while num != 1:
        sequence += 1
        # Number is odd
        if num % 2 == 1:
            num = 3 * num + 1
        else:
            num //= 2
    # Count the final 1
    sequence += 1
    return sequence

# Determines the largest number for the longest collatz sequence
def collatz(num):
    max_chain = 0
    max_chain_num = 0
    for i in range(num, 0, -1):
        a = chain_creator(i)
        if max_chain < a:
            max_chain = a
            max_chain_num = i
    print(f"Number: {max_chain_num} |  Chain length: {max_chain}")

if __name__ == '__main__':
    collatz(1000000)