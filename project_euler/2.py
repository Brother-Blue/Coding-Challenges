""""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""

a = 0
def fibonacci(cur, prev):
    if cur > 4_000_000:
        return cur
    if cur % 2 == 0:
        global a
        a += cur
        print(a)
    return fibonacci(cur + prev, cur)

if __name__ == '__main__':
    fibonacci(1, 0)