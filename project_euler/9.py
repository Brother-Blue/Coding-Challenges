
# Target is the sum value of a, b, c
def pythagorean_triples(target):
    # a will always be less than 1/3 of the total
    for a in range(1, (target // 3) + 1):
        # b will always be less that 1/2 of the total
        for b in range(1 + a, (target // 2) + 1):
            c = target - a - b
            if (a**2 + b**2 == c**2):
                print((a, b, c))
                print(f"Product: {a*b*c}")
                return
    
    print(f"No triple found for target: {target}")

if __name__ == '__main__':
    pythagorean_triples(1000)