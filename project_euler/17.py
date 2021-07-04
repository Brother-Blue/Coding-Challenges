"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage."""

import inflect

inf = inflect.engine()

# From 1 to n
def num_to_word(n):
    str_len = 0
    for i in range(1, n+1):
        s = inf.number_to_words(i)
        s = s.replace(" ", "").replace("-", "")
        str_len += len(s)
    print(str_len)

if __name__ == '__main__':
    num_to_word(1000)